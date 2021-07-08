from fastapi.routing import APIRoute

from src.servers.controllers.todo_controller import ProductController


def index():
    return {"message": "base route of service"}


routes = [
    APIRoute('/', index, methods=["GET"]),
    APIRoute('/todo', TodoController().get_todos, methods=["GET"])
]
