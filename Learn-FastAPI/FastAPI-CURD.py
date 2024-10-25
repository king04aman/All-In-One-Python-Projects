from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

# Define a Pydantic model for Task
class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

# Initialize an empty list to store tasks
tasks = []

# Create a new task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()  # Assign a UUID to the task
    tasks.append(task)  # Add the task to the tasks list
    return task

# Retrieve all tasks
@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks

# Retrieve a specific task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
    
    # Raise HTTPException if task not found
    raise HTTPException(status_code=404, detail="Task not found")

# Update a specific task by ID
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: Task):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[idx] = updated_task
            return updated_task
    
    # Raise HTTPException if task not found
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a specific task by ID
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
    
    # Raise HTTPException if task not found
    raise HTTPException(status_code=404, detail="Task not found")

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
