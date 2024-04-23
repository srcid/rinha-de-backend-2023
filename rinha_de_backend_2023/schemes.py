from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, constr


class NewPersonScheme(BaseModel):
    nickname: str = Field(alias="apelido", max_length=32, pattern=r"^\w+$")
    name: str = Field(alias="nome", max_length=100, pattern=r"^[^\d\W]+( [^\d\W]+)*$")
    birthDate: datetime = Field(alias="nascimento")
    stack: Optional[list[constr(max_length=32)]]


class PersonScheme(NewPersonScheme):
    id: UUID

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
