**#To-Do List Application**
A simple and intuitive To-Do List application built with Python's Tkinter library for the GUI and SQLite for persistent task storage. This application helps you manage tasks with categories, due dates, and priority levels, allowing easy organization of daily activities.

**Features**

Add Tasks: Add tasks with a description, category, due date, and priority level (High, Medium, Low).

View Tasks: View all tasks, or filter tasks to see only completed or pending ones.

Search Tasks: Quickly search tasks by their name or category using the search bar.

Toggle Theme: Switch between dark and light themes to match your preference.

Mark Tasks as Complete: Mark tasks as completed to keep track of what’s done.

Persistent Storage: All tasks are saved in an SQLite database, ensuring data is saved even after closing the app.


**Prerequisites**

Python 3.6+
Tkinter (Usually included with Python)
SQLite (Included in Python’s standard library)
tkcalendar: Install using pip install tkcalendar

**Usage Instructions**

1. Add a Task
Enter a task description in the Task field.
Specify the Category for better organization.
Select a Due Date from the date picker.
Choose a Priority from the drop-down menu (High, Medium, Low).
Click Add Task to save it.

2. View All Tasks
Click on View All Tasks in the sidebar to display a list of all tasks.
Tasks are displayed with their description, category, due date, and priority level.

3. View Completed Tasks
Click View Completed Tasks in the sidebar to see tasks that have been marked as complete.

4. View Pending Tasks
Click View Pending Tasks in the sidebar to view tasks that are yet to be completed.

5. Search Tasks
Use the Search bar in the sidebar to find tasks by their description or category.
The list of tasks will update as you type, showing only those that match the search term.

6. Mark Tasks as Complete
Select a task from the list and click Mark as Complete (add this button in your application).
Completed tasks will no longer appear in the pending tasks view.

7. Toggle Dark/Light Theme
Click Toggle Theme in the sidebar to switch between dark and light modes.
This changes the background color, text color, and button styles for a better visual experience.

8. Close the Application
Close the application by clicking the window close button (X) or selecting Exit.
The application safely saves your tasks and closes the database connection.


**Database Structure**
The application uses an SQLite database with the following table structure:

Table Name: tasks

Column Name	Type	Description

id	       INTEGER	Primary key, unique task ID
task	    TEXT	Description of the task
category	TEXT	Category of the task (e.g., Work, Home)
due_date	TEXT	Due date of the task
priority	TEXT	Priority level (High, Medium, Low)
completed	INTEGER	Status (0 = Pending, 1 = Completed)

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Acknowledgments**
Thanks to the Python community for their extensive libraries and documentation.
Special thanks to the creators of tkcalendar for providing a simple date picker widget for Tkinter.
