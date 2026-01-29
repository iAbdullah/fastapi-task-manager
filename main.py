from fastapi import FastAPI
from routers import users, tasks

app = FastAPI(title="Task Management System")

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Task API"}