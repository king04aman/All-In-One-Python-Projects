# from main import add_entry, search_entries
# import datetime

# def display_menu():
#     print("\n=== My Personal Journal ===")
#     print("1. Create New Journal Entry")
#     print("2. Search Journal Entries")
#     print("3. Exit")

# def get_mood():
#     mood = None
#     while mood not in ["happy", "sad", "neutral"]:
#         mood = input("How are you feeling today? (happy, sad, neutral): ").lower()
#     return mood

# def get_tags():
#     tags = input("Add tags (comma-separated, e.g., work, personal): ")
#     return tags

# def create_new_entry(user_id):
#     mood = get_mood()
#     content = input("Write your journal entry: ")
#     tags = get_tags()
#     add_entry(user_id, mood, content, tags)
#     print("Your entry has been saved!")

# def search_journal_entries(user_id):
#     print("\nSearch Entries")
#     print("1. Search by keyword")
#     print("2. Search by date")
#     choice = input("Choose a search option: ")

#     if choice == '1':
#         search_term = input("Enter a keyword to search for: ")
#         results = search_entries(user_id, search_term=search_term)
#     elif choice == '2':
#         date_str = input("Enter a date (YYYY-MM-DD) to search: ")
#         try:
#             date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
#         except ValueError:
#             print("Invalid date format. Please use YYYY-MM-DD.")
#             return
#         results = search_entries(user_id, date=date)
#     else:
#         print("Invalid option.")
#         return

#     if results:
#         for entry in results:
#             print(f"\nDate: {entry[2]}")
#             print(f"Mood: {entry[3]}")
#             print(f"Tags: {entry[5]}")
#             print(f"Entry: {entry[4]}")
#             print("-" * 40)
#     else:
#         print("No entries found for your search criteria.")

# def main_ui():
#     user_id = input("Enter your user ID to start: ")

#     while True:
#         display_menu()
#         choice = input("Select an option (1-3): ")

#         if choice == '1':
#             create_new_entry(user_id)
#         elif choice == '2':
#             search_journal_entries(user_id)
#         elif choice == '3':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main_ui()
import tkinter as tk
from tkinter import messagebox
from journal_app import add_entry, search_entries
from datetime import datetime

class JournalApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Personal Journal")
        self.geometry("400x400")

        self.label = tk.Label(self, text="Personal Journal", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.add_button = tk.Button(self, text="Add New Entry", command=self.add_entry)
        self.add_button.pack(pady=5)

        self.search_button = tk.Button(self, text="Search Entries", command=self.search_entries)
        self.search_button.pack(pady=5)

    def add_entry(self):
        self.new_window = tk.Toplevel(self)
        self.new_window.title("Add New Entry")

        mood_label = tk.Label(self.new_window, text="Mood (happy, sad, neutral):")
        mood_label.pack(pady=5)
        self.mood_entry = tk.Entry(self.new_window)
        self.mood_entry.pack(pady=5)

        content_label = tk.Label(self.new_window, text="Write your journal entry:")
        content_label.pack(pady=5)
        self.content_entry = tk.Text(self.new_window, height=5, width=30)
        self.content_entry.pack(pady=5)

        tags_label = tk.Label(self.new_window, text="Tags (comma-separated):")
        tags_label.pack(pady=5)
        self.tags_entry = tk.Entry(self.new_window)
        self.tags_entry.pack(pady=5)

        submit_button = tk.Button(self.new_window, text="Submit", command=self.save_entry)
        submit_button.pack(pady=10)

    def save_entry(self):
        mood = self.mood_entry.get()
        content = self.content_entry.get("1.0", tk.END)
        tags = self.tags_entry.get()

        if mood and content:
            add_entry("user_1", mood, content, tags)
            messagebox.showinfo("Success", "Journal entry saved!")
            self.new_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def search_entries(self):
        self.search_window = tk.Toplevel(self)
        self.search_window.title("Search Entries")

        search_label = tk.Label(self.search_window, text="Search by keyword or date (YYYY-MM-DD):")
        search_label.pack(pady=5)
        self.search_entry = tk.Entry(self.search_window)
        self.search_entry.pack(pady=5)

        search_button = tk.Button(self.search_window, text="Search", command=self.perform_search)
        search_button.pack(pady=10)

    def perform_search(self):
        search_term = self.search_entry.get()
        results = search_entries("user_1", search_term=search_term)

        if results:
            result_window = tk.Toplevel(self)
            result_window.title("Search Results")

            for result in results:
                result_label = tk.Label(result_window, text=f"Date: {result[2]}, Mood: {result[3]}, Tags: {result[5]}")
                result_label.pack()
                content_label = tk.Label(result_window, text=f"Entry: {result[4]}")
                content_label.pack(pady=5)
        else:
            messagebox.showinfo("No Results", "No journal entries found.")

if __name__ == "__main__":
    app = JournalApp()
    app.mainloop()
