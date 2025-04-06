import tkinter as tk
from tkinter import messagebox, font

# Initialize the main app window
app = tk.Tk()
app.title("To-Do List Notebook")
app.geometry("450x500")
app.config(bg="#f0f4f8")

# Set custom fonts and colors
header_font = font.Font(family="Helvetica", size=18, weight="bold")
task_font = font.Font(family="Arial", size=12)
button_color = "#4CAF50"
button_hover_color = "#45a049"
task_complete_color = "#2e8b57"
notebook_color = "#FFF8DC"  # Light beige to mimic a notebook page

# Task list to hold tasks
todo_list = []

# Functions to manage tasks
def add_task(event=None):
    """Add a new task with a checkbox to mark as completed. Handles duplicates and empty/whitespace inputs."""
    task_text = entry_task.get().strip()  # Strip leading/trailing whitespace
    if not task_text:
        messagebox.showwarning("Input Error", "Task cannot be empty or just spaces!")
        return

    if any(task["task"].lower() == task_text.lower() for task in todo_list):
        messagebox.showwarning("Duplicate Task", "This task already exists in your to-do list!")
        return

    if len(task_text) > 100:  # Optional: Limit task length to 100 characters
        messagebox.showwarning("Input Error", "Task cannot exceed 100 characters!")
        return

    # Add task if it passes all checks
    task_var = tk.BooleanVar()
    task_frame = tk.Frame(task_list_frame, bg=notebook_color, padx=5, pady=3)

    checkbox = tk.Checkbutton(
        task_frame,
        text=task_text,
        variable=task_var,
        command=lambda: toggle_complete(task_var, checkbox),
        font=task_font,
        bg=notebook_color,
        fg="black",
        selectcolor="white",
        activeforeground=button_color
    )

    checkbox.pack(anchor="w", pady=2)
    todo_list.append({"task": task_text, "completed": task_var, "frame": task_frame})
    task_frame.pack(anchor="w", padx=10, pady=5, fill="x")
    entry_task.delete(0, tk.END)

def toggle_complete(task_var, checkbox):
    """Update the checkbox color when the task is marked complete or incomplete."""
    if task_var.get():
        checkbox.config(fg=task_complete_color, font=task_font)
    else:
        checkbox.config(fg="black", font=task_font)

def delete_completed_tasks(event=None):
    """Delete only ticked tasks from the list."""
    global todo_list
    for task in todo_list[:]:
        if task["completed"].get():
            task["frame"].destroy()
            todo_list.remove(task)
    update_task_list()

def update_task_list():
    """Refresh the display of tasks."""
    for widget in task_list_frame.winfo_children():
        widget.destroy()
    for task in todo_list:
        task["frame"].pack(anchor="w", padx=10, pady=5, fill="x")

def on_hover(button, color):
    """Change button color on hover."""
    button.config(bg=color)

# Header
header = tk.Label(app, text="My Notebook To-Do List", font=header_font, bg="#f0f4f8", fg=button_color)
header.pack(pady=10)

# Notebook look-alike frame for tasks with lines
task_list_frame = tk.Canvas(app, bg=notebook_color, bd=0, highlightthickness=0)
task_list_frame.pack(expand=True, fill="both", padx=15, pady=10)

# Draw lines to mimic notebook paper
for i in range(0, 500, 20):
    task_list_frame.create_line(10, i, 440, i, fill="#d3d3d3")

# Frame for entry, add, and delete buttons
frame_task = tk.Frame(app, bg="#f0f4f8")
frame_task.pack(pady=15)

# Entry for new tasks
entry_task = tk.Entry(frame_task, width=30, font=task_font, relief="solid", bd=1)
entry_task.pack(side=tk.LEFT, padx=10)
entry_task.bind("<Return>", add_task)  # Bind Enter key to add_task

# "+" button for adding tasks
button_add_task = tk.Button(frame_task, text="+", command=add_task, font=("Arial", 20, "bold"), bg=button_color, fg="white",
                            relief="flat", width=3, height=1)
button_add_task.pack(side=tk.LEFT)
button_add_task.bind("<Enter>", lambda e: on_hover(button_add_task, button_hover_color))
button_add_task.bind("<Leave>", lambda e: on_hover(button_add_task, button_color))

# Delete button for deleting only completed tasks
button_delete_task = tk.Button(app, text="Delete completed task", command=delete_completed_tasks, font=task_font,
                               bg=button_color, fg="white", relief="flat", padx=10, pady=5)
button_delete_task.pack(pady=10)
button_delete_task.bind("<Enter>", lambda e: on_hover(button_delete_task, button_hover_color))
button_delete_task.bind("<Leave>", lambda e: on_hover(button_delete_task, button_color))
app.bind("<Delete>", delete_completed_tasks)  # Bind Delete key to delete_completed_tasks

# Run the main loop
app.mainloop()
