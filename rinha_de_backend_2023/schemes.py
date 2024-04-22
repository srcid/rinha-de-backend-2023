from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class NewPersonScheme(BaseModel):
    nickname: str = Field(alias="apelido")
    name: str = Field(alias="nome")
    birthDate: datetime = Field(alias="nascimento")
    stack: Optional[list[str]]


class PersonScheme(NewPersonScheme):
    id: UUID

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
