import sqlite3

# Database setup

def initialize_db():
    conn = sqlite3.connect("../electricity_bills.db")
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

# Function to calculate bill

def calculate_bill(units):
    if units <= 100:
        bill = units * 3.00
    elif units <= 300:
        bill = (100 * 3.00) + ((units - 100) * 5.50)
    elif units <= 600:
        bill = (100 * 3.00) + (200 * 5.50) + ((units - 300) * 6.50)
    else:
        bill = (100 * 3.00) + (200 * 5.50) + (300 * 6.50) + ((units - 600) * 7.50)
    return bill + 50  # Adding fixed charge


# Function to add a new bill entry

def add_bill():
    while True:
        bill_number = input("Enter 9-digit bill number: ")
        if len(bill_number) == 9 and bill_number.isdigit():
            break
        else:
            print("Enter a valid 9-digit Bill ID")

    name = input("Enter customer name: ")
    units = float(input("Enter units consumed: "))
    amount = calculate_bill(units)

    conn = sqlite3.connect("../electricity_bills.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bills (bill_number, name, units, amount, status) VALUES (?, ?, ?, ?, ?)",
                   (bill_number, name, units, amount, "Pending"))
    conn.commit()
    conn.close()
    print(f"Bill added for {name} with Bill Number {bill_number}. Total Amount: ₹{amount:.2f}")


# Function to view all bills

def view_bills():
    conn = sqlite3.connect("../electricity_bills.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills")
    bills = cursor.fetchall()
    conn.close()

    print("\nElectricity Bill Details:")
    for bill in bills:
        print(
            f"ID: {bill[0]}, Bill Number: {bill[1]}, Name: {bill[2]}, Units: {bill[3]}, Amount: ₹{bill[4]:.2f}, Status: {bill[5]}")


# Function to update payment status

def update_status():
    bill_id = int(input("Enter bill ID to update: "))
    status = input("Enter new status (Paid/Pending): ")
    conn = sqlite3.connect("../electricity_bills.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE bills SET status = ? WHERE id = ?", (status, bill_id))
    conn.commit()

    cursor.execute("SELECT * FROM bills WHERE id = ?", (bill_id,))
    updated_bill = cursor.fetchone()
    conn.close()

    if updated_bill:
        print(f"Bill ID {updated_bill[0]} status successfully updated to {updated_bill[5]}.")
    else:
        print("Error: Bill ID not found or update failed.")


# Function to delete a bill

def delete_bill():
    bill_id = int(input("Enter bill ID to delete: "))
    conn = sqlite3.connect("../electricity_bills.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bills WHERE id = ?", (bill_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Bill ID {bill_id} successfully deleted.")
    else:
        print("Error: Bill ID not found or deletion failed.")

    conn.close()


if __name__ == "__main__":
    initialize_db()
    while True:
        print("\nElectricity Bill Management System")
        print("1. Add Bill")
        print("2. View Bills")
        print("3. Update Payment Status")
        print("4. Delete Bill")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_bill()
        elif choice == "2":
            view_bills()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_bill()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")