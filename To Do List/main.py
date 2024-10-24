from tkinter import *
import sqlite3

root = Tk()
root.title("To-Do List App")
root.geometry("400x400")

conn = sqlite3.connect('todolist.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, task TEXT NOT NULL)''')

def add_task():
    task = task_entry.get()
    if task:
        c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        task_entry.delete(0, END)
        populate_tasks()

def delete_task():
    task_id = task_list.get(ACTIVE).split('.')[0]
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    populate_tasks()

def populate_tasks():
    task_list.delete(0, END)
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    for task in tasks:
        task_list.insert(END, f"{task[0]}. {task[1]}")

# Task entry
task_entry = Entry(root, width=50)
task_entry.pack(pady=10)

# Add task button
add_task_button = Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Task list
task_list = Listbox(root, width=50, height=15)
task_list.pack(pady=10)

# Delete task button
delete_task_button = Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

# Populate tasks on startup
populate_tasks()

# Run the main loop
root.mainloop()

conn.close()
