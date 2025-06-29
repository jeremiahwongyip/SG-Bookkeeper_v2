# File: app/services/core_services.py
from typing import List, Optional, Any, TYPE_CHECKING
from sqlalchemy import select, update, text
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.core.sequence import Sequence
from app.models.core.configuration import Configuration
from app.models.core.company_setting import CompanySetting

if TYPE_CHECKING:
    from app.core.database_manager import DatabaseManager
    from app.core.application_core import ApplicationCore


class SequenceService:
    def __init__(self, db_manager: "DatabaseManager"):
        self.db_manager = db_manager

    async def get_sequence_by_name(self, name: str) -> Optional[Sequence]:
        async with self.db_manager.session() as session:
            stmt = select(Sequence).where(Sequence.sequence_name == name)
            result = await session.execute(stmt)
            return result.scalars().first()

    async def get_next_sequence(self, sequence_name: str) -> str:
        """
        Generates the next number in a sequence by calling the database function.
        """
        # This simplifies the Python-side logic significantly, relying on the robust DB function.
        db_func_call = text("SELECT core.get_next_sequence_value(:seq_name);")
        async with self.db_manager.session() as session:
            result = await session.execute(db_func_call, {"seq_name": sequence_name})
            next_val = result.scalar_one_or_none()
            if next_val is None:
                raise RuntimeError(f"Database function get_next_sequence_value failed for sequence '{sequence_name}'.")
            return str(next_val)

    async def save_sequence(self, sequence_obj: Sequence, session: Optional[AsyncSession] = None) -> Sequence:
        async def _save(sess: AsyncSession):
            sess.add(sequence_obj)
            await sess.flush()
            await sess.refresh(sequence_obj)
            return sequence_obj

        if session:
            return await _save(session)
        else:
            async with self.db_manager.session() as new_session: # type: ignore
                return await _save(new_session)

class ConfigurationService:
    def __init__(self, db_manager: "DatabaseManager"):
        self.db_manager = db_manager
    
    async def get_config_by_key(self, key: str) -> Optional[Configuration]:
        async with self.db_manager.session() as session:
            stmt = select(Configuration).where(Configuration.config_key == key)
            result = await session.execute(stmt)
            return result.scalars().first()

    async def get_config_value(self, key: str, default_value: Optional[str] = None) -> Optional[str]:
        """Fetches a configuration value by key, returning default if not found."""
        config_entry = await self.get_config_by_key(key)
        if config_entry and config_entry.config_value is not None:
            return config_entry.config_value
        return default_value

    async def save_config(self, config_obj: Configuration) -> Configuration:
        async with self.db_manager.session() as session:
            session.add(config_obj)
            await session.flush()
            await session.refresh(config_obj)
            return config_obj

class CompanySettingsService:
    def __init__(self, db_manager: "DatabaseManager", app_core: Optional["ApplicationCore"] = None):
        self.db_manager = db_manager
        self.app_core = app_core

    async def get_company_settings(self, settings_id: int = 1) -> Optional[CompanySetting]:
        async with self.db_manager.session() as session:
            return await session.get(CompanySetting, settings_id)

    async def save_company_settings(self, settings_obj: CompanySetting) -> CompanySetting:
        if self.app_core and self.app_core.current_user:
            settings_obj.updated_by_user_id = self.app_core.current_user.id # type: ignore
        async with self.db_manager.session() as session:
            session.add(settings_obj)
            await session.flush()
            await session.refresh(settings_obj)
            return settings_obj
