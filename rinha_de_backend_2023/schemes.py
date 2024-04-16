from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class NewPersonScheme(BaseModel):
    nickname: str
    name: str
    birthDate: datetime
    stack: Optional[list[str]] = Field([], nullable=True)
    
    model_config = ConfigDict(from_attributes=True)


class PersonScheme(NewPersonScheme):
    id: UUID
