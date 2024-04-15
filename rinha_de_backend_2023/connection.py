from settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(settings.DB_URI, echo=True)


def getSession():
    with Session(engine) as s:
        yield s
