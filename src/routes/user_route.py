from typing import Optional
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def index():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
