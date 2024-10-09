import matplotlib.pyplot as plt
from database import get_connection

def bar_chart_expense():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type = 'Expense' GROUP BY category")
    rows = cursor.fetchall()
    conn.close()
    
    if rows:
        categories = [row[0] for row in rows]
        amounts = [row[1] for row in rows]
        
        plt.bar(categories, amounts)
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Spending by Category')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No expenses recorded yet.")

def pie_chart_expense():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type = 'Expense' GROUP BY category")
    rows = cursor.fetchall()
    conn.close()
    
    if rows:
        categories = [row[0] for row in rows]
        amounts = [row[1] for row in rows]
        
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        plt.title('Spending by Category')
        plt.tight_layout()
        plt.show()
    else:
        print("No expenses recorded yet.")

def line_chart_expense_over_time():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT date, SUM(amount) FROM transactions WHERE type = 'Expense' GROUP BY date")
    rows = cursor.fetchall()
    conn.close()
    
    if rows:
        dates = [row[0] for row in rows]
        amounts = [row[1] for row in rows]
        
        plt.plot(dates, amounts, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title('Expenses Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No expenses recorded yet.")

def stacked_bar_chart_income_expense():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT date, SUM(amount) FROM transactions WHERE type = 'Income' GROUP BY date")
    income_rows = cursor.fetchall()

    cursor.execute("SELECT date, SUM(amount) FROM transactions WHERE type = 'Expense' GROUP BY date")
    expense_rows = cursor.fetchall()
    
    conn.close()

    if income_rows and expense_rows:
        income_dates = [row[0] for row in income_rows]
        income_amounts = [row[1] for row in income_rows]
        expense_dates = [row[0] for row in expense_rows]
        expense_amounts = [row[1] for row in expense_rows]

        plt.bar(income_dates, income_amounts, label='Income')
        plt.bar(expense_dates, expense_amounts, bottom=income_amounts, label='Expense')

        plt.xlabel('Date')
        plt.ylabel('Amount')
        plt.title('Income vs Expenses Over Time')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()
    else:
        print("Not enough data to generate this chart.")

def histogram_expense_distribution():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT amount FROM transactions WHERE type = 'Expense'")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        amounts = [row[0] for row in rows]

        plt.hist(amounts, bins=10)
        plt.xlabel('Expense Amount')
        plt.ylabel('Frequency')
        plt.title('Expense Distribution')
        plt.tight_layout()
        plt.show()
    else:
        print("No expenses recorded yet.")

def visualize_data():
    print("\n--- Visualization Menu ---")
    print("1. Bar Chart (Spending by Category)")
    print("2. Pie Chart (Spending by Category)")
    print("3. Line Chart (Expenses Over Time)")
    print("4. Stacked Bar Chart (Income vs Expenses)")
    print("5. Histogram (Expense Distribution)")
    
    choice = input("Select a visualization option (1-5): ")

    if choice == "1":
        bar_chart_expense()
    elif choice == "2":
        pie_chart_expense()
    elif choice == "3":
        line_chart_expense_over_time()
    elif choice == "4":
        stacked_bar_chart_income_expense()
    elif choice == "5":
        histogram_expense_distribution()
    else:
        print("Invalid choice. Please select a valid option.")
