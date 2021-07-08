
class TodoController:

    def get_todos(self) -> list:
        data = {"title":"data"}
        return dict(status=200, data=data), 200
