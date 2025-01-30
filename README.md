# Electricity Bill Management System

This is a simple command-line based Electricity Bill Management System implemented in Python using SQLite for database management. It allows users to add new bill entries, view existing bills, update payment status, and delete bills.

## Features

*   **Add Bill:** Adds a new electricity bill record to the database. It takes the bill number (9 digits), customer name, and units consumed as input. The bill amount is calculated based on a tiered pricing structure.
*   **View Bills:** Displays all the electricity bills stored in the database, including their ID, bill number, customer name, units consumed, amount, and payment status.
*   **Update Payment Status:** Allows users to update the payment status (Paid/Pending) of a specific bill by providing the bill ID.
*   **Delete Bill:** Deletes a bill record from the database based on the bill ID.
*   **Data Persistence:** Uses SQLite database to store bill information persistently.

## How to Use

1.  **Clone the Repository:** (If applicable, if you are hosting this on GitHub)

    ```bash
    git clone [invalid URL removed]  # Replace with your repo URL
    cd electricity_bill_management
    ```

2.  **Run the Script:**

    ```bash
    python electricity_bill_management.py
    ```

3.  **Follow the Menu:** The program will present a menu with options to add, view, update, delete bills, or exit. Follow the on-screen prompts to interact with the system.

## Database Design

The system uses an SQLite database file named `electricity_bills.db`. The database contains one table named `bills` with the following schema:

| Column Name | Data Type | Constraints | Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier for each bill |
| bill_number | TEXT | UNIQUE NOT NULL | 9-digit bill number |
| name | TEXT | NOT NULL | Customer name |
| units | REAL | NOT NULL | Units of electricity consumed |
| amount | REAL | NOT NULL | Calculated bill amount |
| status | TEXT | NOT NULL | Payment status (Paid/Pending) |

## Installation

No special installation is required beyond having Python 3 installed. The SQLite database file is created automatically when the script is run for the first time.

## Code Explanation (Key Parts)

**Database Initialization:**

```python
import sqlite3

def initialize_db():
    conn = sqlite3.connect("electricity_bills.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bills (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        bill_number TEXT UNIQUE NOT NULL,
                        name TEXT NOT NULL,
                        units REAL NOT NULL,
                        amount REAL NOT NULL,
                        status TEXT NOT NULL)''')
    conn.commit()
    conn.close()