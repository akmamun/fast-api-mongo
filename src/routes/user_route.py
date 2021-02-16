from typing import Optional
from fastapi import APIRouter

router = APIRouter()


@router.get("/user/{user_id}")
def read_item(user_id: int, q: Optional[str] = None):
    return {"user_id": user_id, "q": q}
