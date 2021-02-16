from fastapi import FastAPI
from .routes import todo_route, user_route

app = FastAPI()


app.include_router(todo_route.router)
app.include_router(user_route.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "main":
    app.run()
