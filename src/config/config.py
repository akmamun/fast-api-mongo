from src.config.database import db
from src.config.model import model


def config():
    return dict(
        **db(),
        **model()
    )
