"""
Mit Datenbank:
ID, Date, Description, Amount, Category
Basic Funktionen: update, delete, view all, view summary, view summary for month
Advanced Funktionen: set budget, export to CSV
"""

# EXPENSE TRACKER
import sqlite3
from datetime import date
import sys

def create_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

create_db()

def help():
    pass

def create(description, amount, category=None):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (date, description, amount, category)
        VALUES (?, ?, ?, ?) 
        """,(str(date.today()), description, float(amount), category))
    conn.commit()
    conn.close()
    print(f"Expense added: {description} - {amount} - {category}")

# Command Line
description = sys.argv[1]
amount = sys.argv[2]
category = sys.argv[3] if len(sys.argv) > 3 else None

create(description, amount, category)

def modify():
    pass

def delete():
    pass

def view_all():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No expenses found.")
        return

    print(f"{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':<10} {'Category'}")
    print("-" * 55)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<12} {row[2]:<20} {row[3]:<10} {row[4] or 'N/A'}")

def view_sum():
    pass

def view_month():
    pass

def set_budget():
    pass

def compare_budget():
    pass

def export_csv():
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 app.py <command>")
    else:
        command = sys.argv[1]

        if command == "add":
            description = sys.argv[2]
            amount = sys.argv[3]
            category = sys.argv[4] if len(sys.argv) > 4 else None
            create(description, amount, category)

        elif command == "view":
            view_all()

        else:
            print(f"Unknown command: {command}")