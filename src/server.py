from fastapi import FastAPI
from .routes import todo_route, user_route, index_route

app = FastAPI()


app.include_router(index_route.router)
app.include_router(todo_route.router)
app.include_router(user_route.router)


if __name__ == "main":
    app.run()
