from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "main":
    app.run()
