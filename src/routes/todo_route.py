from fastapi import APIRouter

router = APIRouter()


@router.get("/todos/")
async def read_users():
    return [{"title": "Doding Someting", "details": "Doding Someting"}]
