import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
import os

# ==============================
# Hardcoded admin credentials
# ==============================
USERNAME = "admin"
PASSWORD = "password123"

# File to store student data
DATA_FILE = "students.csv"

# Ensure CSV exists
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Roll No", "Name", "Address", "DOB"])
    df.to_csv(DATA_FILE, index=False)

# ==============================
# Helper functions
# ==============================
def get_students():
    return pd.read_csv(DATA_FILE)

def save_students(df):
    df.to_csv(DATA_FILE, index=False)

def generate_roll_no():
    df = get_students()
    if df.empty:
        return 1
    else:
        return df["Roll No"].max() + 1

# ==============================
# Student operations
# ==============================
def add_student():
    name = simpledialog.askstring("Input", "Enter student name:")
    address = simpledialog.askstring("Input", "Enter student address:")
    dob = simpledialog.askstring("Input", "Enter student DOB (YYYY-MM-DD):")

    if name and address and dob:
        roll_no = generate_roll_no()
        df = get_students()
        df.loc[len(df)] = [roll_no, name, address, dob]
        save_students(df)
        messagebox.showinfo("Success", f"Student {name} added with Roll No {roll_no}")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def update_student():
    roll_no = simpledialog.askinteger("Input", "Enter roll number to update:")
    df = get_students()

    if roll_no in df["Roll No"].values:
        name = simpledialog.askstring("Input", "Enter new name (leave blank to keep same):")
        address = simpledialog.askstring("Input", "Enter new address (leave blank to keep same):")
        dob = simpledialog.askstring("Input", "Enter new DOB (leave blank to keep same):")

        idx = df.index[df["Roll No"] == roll_no][0]

        if name:
            df.at[idx, "Name"] = name
        if address:
            df.at[idx, "Address"] = address
        if dob:
            df.at[idx, "DOB"] = dob

        save_students(df)
        messagebox.showinfo("Success", f"Student with Roll No {roll_no} updated!")
    else:
        messagebox.showerror("Error", "Roll number not found!")

def delete_student():
    roll_no = simpledialog.askinteger("Input", "Enter roll number to delete:")
    df = get_students()

    if roll_no in df["Roll No"].values:
        df = df[df["Roll No"] != roll_no]
        save_students(df)
        messagebox.showinfo("Deleted", f"Student with Roll No {roll_no} deleted!")
    else:
        messagebox.showerror("Error", "Roll number not found!")

def search_student():
    choice = simpledialog.askstring("Search", "Search by 'roll' or 'name'?").lower()
    df = get_students()

    if choice == "roll":
        roll_no = simpledialog.askinteger("Input", "Enter roll number:")
        result = df[df["Roll No"] == roll_no]
    elif choice == "name":
        name = simpledialog.askstring("Input", "Enter name:")
        result = df[df["Name"].str.contains(name, case=False, na=False)]
    else:
        messagebox.showerror("Error", "Invalid choice!")
        return

    if not result.empty:
        messagebox.showinfo("Result", result.to_string(index=False))
    else:
        messagebox.showinfo("Result", "No matching student found.")

# ==============================
# Login + Dashboard
# ==============================
def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == USERNAME and entered_password == PASSWORD:
        messagebox.showinfo("Login Success", "Welcome, Admin!")
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("Student Management System")
    dashboard.geometry("400x400")

    tk.Label(dashboard, text="Student Management System",
             font=("Arial", 14, "bold")).pack(pady=15)

    tk.Button(dashboard, text="Add Student", command=add_student, width=25).pack(pady=5)
    tk.Button(dashboard, text="Update Student", command=update_student, width=25).pack(pady=5)
    tk.Button(dashboard, text="Delete Student", command=delete_student, width=25).pack(pady=5)
    tk.Button(dashboard, text="Search Student", command=search_student, width=25).pack(pady=5)
    tk.Button(dashboard, text="Exit", command=dashboard.quit, width=25).pack(pady=10)

    dashboard.mainloop()

# ==============================
# Main Login Window
# ==============================
root = tk.Tk()
root.title("Admin Login")
root.geometry("300x200")

tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()
