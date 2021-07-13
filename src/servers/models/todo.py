
from pydantic import BaseModel, Field, validator

from src.db.repository import Repository


class Todos(Repository):
    # async def index(self, add):
    #     await add([('', "")])

    def collection(self):
        return 'todos'

    def saveTodo(self, title: str, description: str):
        data = {"title": title,
                "description": description}

        return self.save(data=data, collection_name=self.collection())
