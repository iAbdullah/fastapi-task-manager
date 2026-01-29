from fastapi import APIRouter, Query
from typing import Annotated
from schemas.models import TaskCreate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
async def get_tasks(priority: Annotated[str | None, Query()] = None):
    return {"message": "Fetching tasks", "filter": priority}

@router.post("/")
async def create_new_task(task: TaskCreate):
    return {"message": "Task created successfully", "task": task}