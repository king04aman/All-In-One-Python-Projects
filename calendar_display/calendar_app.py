import tkinter as tk
from tkinter import messagebox
import calendar

def main():
    root = tk.Tk()
    root.title("Calendar App")
    root.geometry("300x150")
    
    tk.Label(root, text="Enter Year:").pack(pady=5)
    year_entry = tk.Entry(root)
    year_entry.pack(pady=5)
    
    def show_calendar():
        year = year_entry.get()
        if not year.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid year")
            return
        display_calendar(year)
    
    tk.Button(root, text="Show Calendar", command=show_calendar).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)
    
    root.mainloop()

def display_calendar(year):
    try:
        year = int(year)
        if year < 1:
            raise ValueError
        cal = calendar.TextCalendar()
        cal_str = cal.formatyear(year)
        messagebox.showinfo(f"Calendar for {year}", cal_str)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive year")


def show_calendar(year):
    try:
        year = int(year)
        if year < 1:
            raise ValueError
        cal = calendar.TextCalendar()
        cal_str = cal.formatyear(year)
        messagebox.showinfo(f"Calendar for {year}", cal_str)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive year")

        display_calendar(year)