from fastapi.routing import APIRoute

from src.servers.controllers.todo_controller import TodoController


def index():
    return {"message": "base route of service"}


TodoController = TodoController()
routes = [
    APIRoute('/', index, methods=["GET"]),
    APIRoute('/todos', TodoController.save_todo, methods=["POST"]),
    APIRoute('/todos', TodoController.get_todos, methods=["GET"])

]
