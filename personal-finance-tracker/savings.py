from database import get_connection

def set_goal():
    goal_amount = float(input("Enter your savings goal: "))
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT OR REPLACE INTO savings_goal (id, goal_amount) VALUES (1, ?)", (goal_amount,))
    conn.commit()
    conn.close()
    
    print(f"Savings goal of {goal_amount} set successfully!")

def track_savings_progress(balance):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT goal_amount FROM savings_goal WHERE id = 1")
    goal_row = cursor.fetchone()
    conn.close()
    
    if goal_row:
        goal_amount = goal_row[0]
        remaining = goal_amount - balance
        if remaining > 0:
            print(f"You need to save {remaining} more to reach your goal.")
        else:
            print(f"Congratulations! You've reached your savings goal.")
    else:
        print("No savings goal set.")
