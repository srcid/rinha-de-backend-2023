from datetime import datetime
from uuid import UUID

from pydantic.dataclasses import dataclass
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


class Base(
    MappedAsDataclass,
    DeclarativeBase,
    dataclass_callable=dataclass,
):
    pass


class Person(Base):
    __tablename__ = "person"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(32))
    name: Mapped[str] = mapped_column(String(100))
    birthDate: Mapped[datetime] = mapped_column(nullable=False)
