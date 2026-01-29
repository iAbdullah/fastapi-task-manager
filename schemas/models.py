from pydantic import BaseModel, Field, field_validator
from typing import List, Literal, Annotated, Optional

class Profile(BaseModel):
    bio: Optional[str] = None
    phone: str

class UserCreate(BaseModel):
    username: str
    email: str
    role: Literal["admin", "manager", "team_member"]
    profile: Profile

class TaskCreate(BaseModel):
    title: Annotated[str, Field(min_length=3)]
    description: str
    priority: Literal["Low", "Medium", "High"]
    status: Literal["Todo", "Doing", "Done"] = "Todo"

    @field_validator('title')
    @classmethod
    def title_must_be_capitalized(cls, v: str) -> str:
        if not v[0].isupper():
            raise ValueError('title must be capitalized')
        return v