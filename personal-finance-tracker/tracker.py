import sqlite3
from database import get_connection

def add_income():
    category = input("Enter income source (e.g., Salary, Freelance): ")
    amount = float(input("Enter amount: "))
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO transactions (type, category, amount) VALUES (?, ?, ?)", 
                   ("Income", category, amount))
    conn.commit()
    conn.close()
    
    print("Income added successfully!")

def add_expense():
    category = input("Enter expense category (e.g., Rent, Groceries): ")
    amount = float(input("Enter amount: "))
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO transactions (type, category, amount) VALUES (?, ?, ?)", 
                   ("Expense", category, amount))
    conn.commit()
    conn.close()
    
    print("Expense added successfully!")

def view_summary():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'Income'")
    total_income = cursor.fetchone()[0] or 0.0
    
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'Expense'")
    total_expenses = cursor.fetchone()[0] or 0.0
    
    balance = total_income - total_expenses
    
    conn.close()
    
    print(f"\nTotal Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Balance: {balance}")
