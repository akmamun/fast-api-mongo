from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


if __name__ == "main":
    app.run()
