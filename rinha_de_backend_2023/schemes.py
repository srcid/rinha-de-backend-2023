from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class NewPersonScheme(BaseModel):
    nickname: str
    name: str
    birthDate: datetime
    stack: Optional[list[str]] = Field([], nullable=True)


class PersonScheme(NewPersonScheme):
    id: UUID
