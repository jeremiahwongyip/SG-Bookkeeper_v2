# SG Bookkeeper

<div align="center">

<!-- Replace with actual logo if available -->
<img src="https://raw.githubusercontent.com/nordeim/SG-Bookkeeper/refs/heads/main/home_screen.png" alt="SG Bookkeeper Logo" width="600"/>

**Singapore-Focused Small Business Accounting Software**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PySide6 6.9+](https://img.shields.io/badge/UI-PySide6_6.9-green.svg)](https://doc.qt.io/qtforpython/)
[![PostgreSQL 14+](https://img.shields.io/badge/DB-PostgreSQL_14+-blue.svg)](https://www.postgresql.org/)
[![SQLAlchemy 2.0+](https://img.shields.io/badge/ORM-SQLAlchemy_2.0-orange.svg)](https://www.sqlalchemy.org/)
[![Asyncpg](https://img.shields.io/badge/Async-Asyncpg-purple.svg)](https://github.com/MagicStack/asyncpg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[Key Features](#key-features) • [Technology Stack](#technology-stack) • [Installation](#installation) • [Usage](#usage-guide) • [Project Structure](#project-structure) • [Contributing](#contributing) • [Roadmap](#roadmap) • [License](#license)

</div>

## Overview

SG Bookkeeper is a comprehensive, cross-platform desktop application designed to meet the accounting and bookkeeping needs of small to medium-sized businesses (SMBs) in Singapore. Built with Python and leveraging the power of PySide6 for a modern user interface and PostgreSQL for robust data management, it offers professional-grade financial tools tailored to Singapore's regulatory environment.

The application features a double-entry accounting core, GST management, interactive financial reporting, modules for essential business operations (Customer, Vendor, Product/Service Management, Sales & Purchase Invoicing), and comprehensive User/Role/Permission administration. Its goal is to provide an intuitive, powerful, and compliant solution that empowers business owners and accountants.

### Why SG Bookkeeper?

-   **Singapore-Centric**: Designed with Singapore Financial Reporting Standards (SFRS), GST regulations (including the 9% rate), and IRAS compliance considerations at its core.
-   **Professional Grade**: Implements a full double-entry system, detailed audit trails (via database triggers), and robust data validation using Pydantic DTOs.
-   **User-Friendly Interface**: Aims for an intuitive experience for users who may not be accounting experts, while providing depth for professionals. Most core modules have functional UIs with features like advanced product search in invoices.
-   **Open Source & Local First**: Transparent development. Your financial data stays on your local machine or private server, ensuring privacy and control. No subscription fees.
-   **Modern & Performant**: Utilizes asynchronous operations for a responsive UI and efficient database interactions, with a dedicated asyncio event loop.

## Key Features

*(Status: Implemented, UI Implemented, Backend Implemented, Foundational (DB/Models ready), Planned)*

### Core Accounting
-   **Comprehensive Double-Entry Bookkeeping** (Implemented)
-   **Customizable Hierarchical Chart of Accounts** (Implemented - UI for CRUD)
-   **General Ledger with detailed transaction history** (Implemented - Report generation, on-screen view, export, with dimension filtering options)
-   **Journal Entry System** (Implemented - UI for General Journal with Journal Type filter; transaction-specific JEs generated on posting of source documents)
-   **Multi-Currency Support** (Foundational - Models, CurrencyManager exist. UI integration in transactions pending.)
-   **Fiscal Year and Period Management** (Implemented - UI in Settings for FY creation and period auto-generation.)
-   **Budgeting and Variance Analysis** (Foundational - Models exist. UI/Logic planned.)

### Singapore Tax Compliance
-   **GST Tracking and Calculation** (Backend Implemented - `TaxCode` setup, `TaxCalculator` for line items. Sales/Purchase Invoice Dialogs use it.)
-   **GST F5 Return Data Preparation & Finalization** (Implemented - Backend for data prep & finalization with JE settlement. UI in Reports tab.)
-   **Income Tax Estimation Aids** (Planned)
-   **Withholding Tax Management** (Foundational)

### Business Operations
-   **Customer Management** (Implemented - Full CRUD and listing UI.)
-   **Vendor Management** (Implemented - Full CRUD and listing UI.)
-   **Product and Service Management** (Implemented - Full CRUD and listing UI.)
-   **Sales Invoicing and Accounts Receivable** (Implemented - Draft CRUD, Posting with financial JE & inventory (WAC) JE creation, List View UI, Dialog with "Save & Approve" and advanced product search.)
-   **Purchase Invoicing and Accounts Payable** (Implemented - Draft CRUD, Posting with financial JE & inventory (WAC based on purchase cost) JE creation, List View UI, Dialog with advanced product search.)
-   **Payment Processing and Allocation** (Foundational)
-   **Bank Account Management and Reconciliation Tools** (Foundational - UI is a stub.)
-   **Inventory Control (Weighted Average Cost)** (Implemented - `InventoryMovement` records created on posting Sales/Purchase invoices for 'Inventory' type products; COGS JEs for sales.)

### Reporting & Analytics
-   **Standard Financial Statements**: Balance Sheet, Profit & Loss, Trial Balance, General Ledger (Implemented - UI in Reports tab with options for comparative/zero-balance, on-screen view, PDF/Excel export with enhanced formatting for all four statements. GL includes dimension filtering.)
-   **Cash Flow Statement** (Planned)
-   **GST Reports** (Implemented - See GST F5 above.)
-   **Customizable Reporting Engine** (Planned - `ReportEngine` has enhanced exports; further customization planned)
-   **Dashboard with Key Performance Indicators (KPIs)** (Planned - UI is a stub.)

### System & Security
-   **User Authentication** (Implemented - Login, password hashing)
-   **Role-Based Access Control (RBAC)** (Implemented - UI for managing Users, Roles, and assigning Permissions to Roles.)
-   **Granular Permissions System** (Implemented - Backend checks via `SecurityManager.has_permission()`, permissions seeded.)
-   **Comprehensive Audit Trails** (Implemented - Via DB triggers and `app.current_user_id`.)
-   **PostgreSQL Database Backend** (Implemented)
-   **Data Backup and Restore Utilities** (Planned)

## Technology Stack
-   **Programming Language**: Python 3.9+ (up to 3.12)
-   **UI Framework**: PySide6 6.9.0+
-   **Database**: PostgreSQL 14+
-   **ORM**: SQLAlchemy 2.0+ (Async ORM with `asyncpg`)
-   **Async DB Driver**: `asyncpg`
-   **Data Validation (DTOs)**: Pydantic V2 (with `email-validator`)
-   **Password Hashing**: `bcrypt`
-   **Reporting Libraries**: `reportlab` (PDF), `openpyxl` (Excel)
-   **Dependency Management**: Poetry
-   **Date/Time Utilities**: `python-dateutil`

## Installation

This guide is for developers setting up the application from source. End-user installers are planned for future releases.

### Prerequisites
-   Python 3.9 or higher (check with `python --version`)
-   PostgreSQL Server 14 or higher (running and accessible)
-   Poetry (Python packaging and dependency management tool). Install via `pip install poetry` or preferred method (e.g., `pipx install poetry`).
-   Git (for cloning the repository)

### Developer Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/sg_bookkeeper.git # Replace with your actual repository URL
    cd sg_bookkeeper
    ```

2.  **Set Up Python Virtual Environment & Install Dependencies:**
    Using Poetry is highly recommended.
    ```bash
    poetry install
    ```
    This command creates a virtual environment (typically `.venv` in the project root if one doesn't exist) and installs all dependencies specified in `pyproject.toml`.

3.  **Prepare PostgreSQL Database User and Database:**
    *   Connect to your PostgreSQL instance as a superuser (e.g., `postgres`):
        ```bash
        psql -U postgres
        ```
    *   Create a dedicated database user for the application (replace `YourSecurePassword123!` securely):
        ```sql
        CREATE USER sgbookkeeper_user WITH PASSWORD 'YourSecurePassword123!';
        -- The database itself (sg_bookkeeper) will be created by the db_init.py script if it doesn't exist,
        -- provided the connecting user (e.g., postgres) has CREATEDB rights.
        -- Alternatively, create it manually:
        -- CREATE DATABASE sg_bookkeeper OWNER sgbookkeeper_user;
        \q
        ```

4.  **Configure Database Connection (`config.ini`):**
    *   The application expects `config.ini` in a platform-specific user configuration directory.
        *   Linux: `~/.config/SGBookkeeper/config.ini`
        *   macOS: `~/Library/Application Support/SGBookkeeper/config.ini`
        *   Windows: `C:\Users\<YourUser>\AppData\Roaming\SGBookkeeper\config.ini`
    *   Create this directory if it doesn't exist.
    *   Copy the following example content into `config.ini` in that location, adjusting values as necessary:
        ```ini
        [Database]
        username = sgbookkeeper_user ; User for application runtime
        password = YourSecurePassword123!
        host = localhost
        port = 5432
        database = sg_bookkeeper
        echo_sql = False
        pool_min_size = 2
        pool_max_size = 10
        pool_recycle_seconds = 3600

        [Application]
        theme = light
        language = en
        last_opened_company_id = 1 ; Default company settings ID from initial_data.sql
        ```
    *   Ensure `username`, `password`, `host`, `port`, and `database` match your PostgreSQL setup.

5.  **Initialize the Database Schema and Seed Initial Data:**
    *   This step requires PostgreSQL administrative privileges (e.g., user `postgres`) to create the database (if not existing) and extensions.
    *   Run the database initialization script using Poetry. Replace `YOUR_POSTGRES_ADMIN_PASSWORD` with the password for your PostgreSQL admin user.
    ```bash
    poetry run sg_bookkeeper_db_init --user postgres --password YOUR_POSTGRES_ADMIN_PASSWORD --dbname sg_bookkeeper --drop-existing
    ```
    *   **`--drop-existing`**: Use this flag with caution. It will delete and recreate the `sg_bookkeeper` database, ensuring a clean setup. Omit it if you want to preserve an existing database (the script might then fail if tables conflict).
    *   This script executes `scripts/schema.sql` (DDL) and `scripts/initial_data.sql` (DML for seeding).

6.  **Grant Privileges to Application User (if `sgbookkeeper_user` didn't create the DB):**
    *   If `db_init.py` was run by an admin user (e.g., `postgres`) and created the database, connect as that admin user to `sg_bookkeeper` database:
        ```bash
        psql -U postgres -d sg_bookkeeper
        ```
    *   Execute the following `GRANT` commands (replace `sgbookkeeper_user` if you used a different application username):
        ```sql
        GRANT USAGE ON SCHEMA core, accounting, business, audit TO sgbookkeeper_user;
        GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA core TO sgbookkeeper_user;
        GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA accounting TO sgbookkeeper_user;
        GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA business TO sgbookkeeper_user;
        GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA audit TO sgbookkeeper_user;
        GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA core TO sgbookkeeper_user;
        GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA accounting TO sgbookkeeper_user;
        GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA business TO sgbookkeeper_user;
        GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA audit TO sgbookkeeper_user;
        GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA core TO sgbookkeeper_user;
        GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA accounting TO sgbookkeeper_user;
        GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA audit TO sgbookkeeper_user;

        ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA core GRANT ALL ON TABLES TO sgbookkeeper_user;
        ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA accounting GRANT ALL ON TABLES TO sgbookkeeper_user;
        ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA business GRANT ALL ON TABLES TO sgbookkeeper_user;
        ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA audit GRANT ALL ON TABLES TO sgbookkeeper_user;
        ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA core GRANT USAGE, SELECT ON SEQUENCES TO sgbookkeeper_user;
        ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA accounting GRANT USAGE, SELECT ON SEQUENCES TO sgbookkeeper_user;
        ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA business GRANT USAGE, SELECT ON SEQUENCES TO sgbookkeeper_user;
        ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA audit GRANT USAGE, SELECT ON SEQUENCES TO sgbookkeeper_user;
        \q
        ```

7.  **Compile Qt Resources (Recommended for consistent icon loading):**
    The application attempts to use compiled resources first (`app/resources_rc.py`).
    ```bash
    poetry run pyside6-rcc resources/resources.qrc -o app/resources_rc.py
    ```

8.  **Run the Application:**
    Ensure your `config.ini` points to the correct application database user (`sgbookkeeper_user` if you followed the example).
    ```bash
    poetry run sg_bookkeeper
    ```

## Usage Guide

The application provides a range of functional modules accessible via tabs in the main window:

-   **Dashboard Tab**: (Placeholder) Intended for an overview of financial health.
-   **Accounting Tab**:
    -   **Chart of Accounts**: View, add, edit, and (de)activate accounts.
    -   **Journal Entries**: List, filter (including by Journal Type), create, edit drafts, view, post, and reverse general journal entries.
-   **Sales Tab**: Create, view, filter, edit draft, post Sales Invoices (with financial and inventory JEs), and use advanced product search.
-   **Purchases Tab**: Create, view, filter, edit draft, and post Purchase Invoices (with financial and inventory JEs), and use advanced product search.
-   **Customers Tab**: View, search, filter, add, edit, and toggle active status for customers.
-   **Vendors Tab**: View, search, filter, add, edit, and toggle active status for vendors.
-   **Products & Services Tab**: Manage products and services (Inventory, Non-Inventory, Service types) with list view, filters, add/edit dialog.
-   **Banking Tab**: (Placeholder) For bank account management and reconciliation.
-   **Reports Tab**:
    -   **GST F5 Preparation**: Prepare, view, save draft, and finalize GST F5 returns.
    *   **Financial Statements**: Generate Balance Sheet, Profit & Loss, Trial Balance, or General Ledger. View in structured tables/trees. Export to PDF/Excel with enhanced formatting. GL reports support filtering by up to two dimensions. BS/P&L reports support comparative periods and zero-balance account options.
-   **Settings Tab**:
    -   **Company**: Configure company-wide information.
    -   **Fiscal Years**: Manage Fiscal Years and their periods.
    -   **Users**: Manage user accounts (add, edit, toggle active, change password, assign roles).
    *   **Roles & Permissions**: Manage roles (add, edit, delete) and assign system permissions to roles.

Upon first run (after DB initialization), an `admin` user is created with the password `password`. You will be prompted to change this password on first login.

## Project Structure

```
sg_bookkeeper/
├── app/
│   ├── __init__.py
│   ├── main.py                     # Main application entry point (QApplication, asyncio bridge)
│   ├── core/                       # Core components (ApplicationCore, DBManager, Config, Security)
│   ├── common/                     # Common utilities, enums
│   ├── models/                     # SQLAlchemy ORM models (organized by schema: core, accounting, etc.)
│   ├── services/                   # Data access services (repositories)
│   ├── accounting/                 # Business logic managers for accounting module
│   ├── tax/                        # Business logic managers for tax module
│   ├── business_logic/             # Managers for Customers, Vendors, Products, Invoices
│   ├── reporting/                  # Logic managers for generating reports
│   ├── ui/                         # PySide6 UI components (organized by module)
│   │   ├── accounting/
│   │   ├── customers/
│   │   ├── vendors/
│   │   ├── products/
│   │   ├── sales_invoices/
│   │   ├── purchase_invoices/
│   │   ├── reports/
│   │   ├── settings/
│   │   ├── shared/                 # Shared UI components like ProductSearchDialog
│   │   └── ... (other ui modules)
│   ├── utils/                      # General utility functions, Pydantic DTOs, helpers
│   └── resources_rc.py             # Compiled Qt resources (if generated)
├── data/                           # Default data templates (CoA, report templates, tax codes)
├── docs/                           # Project documentation (like this README, TDS)
├── resources/                      # UI assets (icons, images, .qrc file)
├── scripts/                        # Database initialization and utility scripts (db_init.py, schema.sql, initial_data.sql)
├── tests/                          # Automated tests (planned)
├── .gitignore
├── pyproject.toml                  # Poetry configuration for dependencies and project metadata
├── poetry.lock
├── README.md                       # This file
└── LICENSE
```

## Database Schema
The application uses a PostgreSQL database with a schema organized into four main parts: `core`, `accounting`, `business`, and `audit`. This schema is designed to be comprehensive, supporting a wide range of accounting and business functionalities. For the complete schema details, including table structures, views, functions, and triggers, please refer to `scripts/schema.sql`.

## Development
-   **Formatting**: Code is formatted using Black. Run `poetry run black .`
-   **Linting**: Flake8 is used for linting. Run `poetry run flake8 .`
-   **Type Checking**: MyPy can be used. Run `poetry run mypy app scripts`
-   **Testing**: Pytest is set up. Run tests with `poetry run pytest`. (Test coverage needs improvement).

## Contributing
Contributions are welcome! Please follow standard open-source contribution practices:
1.  Fork the repository.
2.  Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature-name`).
3.  Make your changes, ensuring to add relevant tests where applicable.
4.  Run linters, formatters, and tests to ensure code quality.
5.  Commit your changes with descriptive messages following conventional commit guidelines if possible.
6.  Push to your branch (`git push origin feature/your-feature-name`).
7.  Submit a Pull Request against the `main` (or `develop`) branch of the original repository.

Please adhere to standard coding practices and ensure your contributions align with the project's goals and architectural patterns.

## Roadmap

### Recently Completed
-   Implemented full posting logic (Financial JE & Inventory Movements using WAC) for Purchase Invoices.
-   Enhanced Sales & Purchase Invoice dialogs with an advanced product search popup.
-   Improved PDF/Excel export formatting for Trial Balance and General Ledger reports.
-   Added Journal Type filter to Journal Entries list and Dimension filters to General Ledger report.

### Current Focus / Next Steps (Previously Medium-Term)
-   **Banking Module**:
    *   Implement UI for Bank Account management (CRUD operations).
    *   Develop functionality for basic bank transaction entry.
-   **Payments Module**:
    *   Implement UI and backend logic for recording customer and vendor payments.
    *   Develop functionality for allocating payments to sales and purchase invoices.
-   **GST F5 Enhancements**:
    *   Improve export options for GST F5 data (e.g., consider IAF format for IRAS).
-   **Audit Log UI**:
    *   Implement a UI section (likely in Settings or a dedicated Audit tab) to view and filter the `audit.audit_log` and `audit.data_change_history`.

### Long-term
-   Bank Reconciliation features.
-   Advanced reporting and analytics, dashboard KPIs.
-   Inventory Control enhancements (e.g., stock movements beyond invoicing, valuation methods like FIFO/Weighted Avg if WAC proves insufficient).
-   Multi-company support (major architectural consideration).
-   Cloud synchronization options (optional).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
