import tracker
import savings
import visualization
import database

def main_menu():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Set Savings Goal")
        print("5. Visualize Spending")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            tracker.add_income()
        elif choice == "2":
            tracker.add_expense()
        elif choice == "3":
            tracker.view_summary()
        elif choice == "4":
            savings.set_goal()
        elif choice == "5":
            visualization.visualize_data()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    database.initialize_database() 
    main_menu()
