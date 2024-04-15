from http import HTTPStatus as status
from uuid import UUID, uuid4

import sqlalchemy as sa
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from rinha_de_backend_2023.connection import getSession
from rinha_de_backend_2023.models import Person
from rinha_de_backend_2023.schemes import NewPersonScheme

app = FastAPI()


# POST /pessoas – para criar um recurso pessoa.
@app.post("/pessoas")
def createPerson(newPerson: NewPersonScheme, session: Session = Depends(getSession)):
    db_person = Person(
        id=uuid4(),
        nickname=newPerson.nickname,
        name=newPerson.name,
        birthDate=newPerson.birthDate,
        stack=newPerson.stack
    )

    session.add(db_person)
    session.commit()
    session.refresh(db_person)

    return db_person


# GET /pessoas/[:id] – para consultar um recurso criado com a requisição anterior.
@app.get("/pessoas/{id}")
def getPerson(id: UUID, session: Session = Depends(getSession)):
    db_user = session.scalar(sa.select(Person).where(Person.id == id))

    if not db_user:
        raise HTTPException(status_code=status.NOT_FOUND, detail="Person not found")

    return db_user


# GET /pessoas?t=[:termo da busca] – para fazer uma busca por pessoas.
@app.get("/pessoas")
def searchOnPersons(t: str, session: Session = Depends(getSession)):
    # Select p.id from Pessoas p where p.nickname like '%termo%' or p.name like '%termo%' or p.stack like '%termo%'
    db_matches = session.scalars(
        sa.select(Person)
            .where(Person.nickname.like(f'%{t}%')
                    | Person.name.like(f'%{t}%')
                    | sa.func.array_to_string(Person.stack, ' ').like(f'%{t}%')
            )
    ).all()

    return db_matches


# GET /contagem-pessoas – endpoint especial para contagem de pessoas cadastradas.
@app.get("/contagem-pessoas")
def countPersons(session: Session = Depends(getSession)):
    res = session.scalar(sa.select(sa.func.count(1)).select_from(Person))
    return res
