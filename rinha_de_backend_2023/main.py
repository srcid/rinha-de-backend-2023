from http import HTTPStatus as status
from uuid import UUID, uuid4

import sqlalchemy as sa
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from rinha_de_backend_2023.connection import getSession
from rinha_de_backend_2023.models import Person
from rinha_de_backend_2023.schemes import NewPersonScheme, PersonScheme

app = FastAPI()


# POST /pessoas – para criar um recurso pessoa.
@app.post("/pessoas", status_code=status.CREATED)
def createPerson(
    newPerson: NewPersonScheme, session: Session = Depends(getSession)
) -> PersonScheme:
    db_person = Person(
        id=uuid4(),
        nickname=newPerson.nickname,
        name=newPerson.name,
        birthDate=newPerson.birthDate,
        stack=newPerson.stack,
    )

    session.add(db_person)

    try:
        session.commit()
        session.refresh(db_person)

        return db_person

    except IntegrityError as err:
        raise HTTPException(
            status_code=status.UNPROCESSABLE_ENTITY, detail="Nickname already exists."
        )


# GET /pessoas/[:id] – para consultar um recurso criado com a requisição anterior.
@app.get("/pessoas/{id}", status_code=status.OK)
def getPerson(id: UUID, session: Session = Depends(getSession)) -> PersonScheme:
    db_user = session.scalar(sa.select(Person).where(Person.id == id))

    if not db_user:
        raise HTTPException(status_code=status.NOT_FOUND, detail="Person not found")

    return db_user


# GET /pessoas?t=[:termo da busca] – para fazer uma busca por pessoas.
@app.get("/pessoas")
def searchOnPersons(t: str, session: Session = Depends(getSession)):
    db_matches = session.scalars(
        sa.select(Person).where(Person.search.contains(t))
    ).all()

    return [ PersonScheme.model_validate(match) for match in db_matches ]


# GET /contagem-pessoas – endpoint especial para contagem de pessoas cadastradas.
@app.get("/contagem-pessoas")
def countPersons(session: Session = Depends(getSession)):
    return session.scalar(sa.select(sa.func.count(1)).select_from(Person))
