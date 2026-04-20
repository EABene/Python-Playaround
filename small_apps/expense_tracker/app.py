"""
Mit Datenbank:
ID, Date, Description, Amount, Category
Basic Funktionen: update, delete, view all, view summary, view summary for month
Advanced Funktionen: set budget, export to CSV
"""

# EXPENSE TRACKER
import sqlite3

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

def create ():
    pass

def modify():
    pass

def delete():
    pass

def view_all():
    pass

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

