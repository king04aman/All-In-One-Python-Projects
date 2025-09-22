import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("Habit Tracker")
    root.geometry("400x300")

    tk.Label(root, text="Habit Tracker App").pack(pady=10)
    
    tk.Label(root, text="Enter Habit:").pack(pady=5)
    habit_entry = tk.Entry(root)
    habit_entry.pack(pady=5)

    def add_habit():
        habit = habit_entry.get()
        if habit == "":
            messagebox.showerror("Error", "Please enter a habit")
        else:
            print(f"Added habit: {habit} (placeholder)")

    tk.Button(root, text="Add Habit", command=add_habit).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

    # habit_tracker.py (continued)
def show_streaks():
    print("Showing habit streaks (placeholder)")
