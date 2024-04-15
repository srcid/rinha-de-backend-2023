from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class NewPersonScheme(BaseModel):
    nickname: str
    name: str
    birthDate: datetime
    stack: Optional[list[str]] = Field(None, nullable=True)


class PersonScheme(NewPersonScheme):
    id: UUID
