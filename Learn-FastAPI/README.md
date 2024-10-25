# FastAPI CRUD and Authentication Example

This directory contains two FastAPI applications: one for basic CRUD operations (task management) and another for user authentication using JWT (JSON Web Tokens).

## Overview

1. **Task Management API (`fastapi-curd.py`)**:
   - Implements basic CRUD operations for managing tasks.
   - Tasks have attributes like `id`, `title`, `description`, and `completed`.

2. **User Authentication API (`fastapi-tutorial.py`)**:
   - Implements user registration, login, and token-based authentication.
   - Uses JWT for secure access and stores user information in a simulated database.

## Installation

To run the applications, ensure you have Python and FastAPI installed. You can install FastAPI and Uvicorn using pip:

```bash
pip install fastapi uvicorn python-jose passlib[bcrypt]
```

## Running the Applications

You can run each application separately.

### Task Management API

To run the task management API:

```bash
python fastapi-curd.py
```

The API will be available at `http://localhost:8000/tasks/`.

### User Authentication API

To run the user authentication API:

```bash
python fastapi-tutorial.py
```

The API will be available at `http://localhost:8000/token` for login and `http://localhost:8000/users/me/` for user information.

## API Endpoints

### Task Management API Endpoints

- **Create Task**: `POST /tasks/`
- **Retrieve All Tasks**: `GET /tasks/`
- **Retrieve Specific Task**: `GET /tasks/{task_id}`
- **Update Task**: `PUT /tasks/{task_id}`
- **Delete Task**: `DELETE /tasks/{task_id}`

### User Authentication API Endpoints

- **Token Generation**: `POST /token`
- **Get Current User**: `GET /users/me/`
- **Get Current User's Items**: `GET /users/me/items`

## Author
- [king04aman](https://github.com/king04aman)
