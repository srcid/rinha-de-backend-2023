from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from rinha_de_backend_2023.settings import settings

engine = create_engine(settings.DB_URI, echo=not settings.FASTAPI_PRODUCTION)


def getSession():
    with Session(engine) as s:
        yield s
