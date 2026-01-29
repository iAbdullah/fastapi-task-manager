from fastapi import APIRouter
from schemas.models import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def create_user(user: UserCreate):
    return {"message": "User registered", "user": user}