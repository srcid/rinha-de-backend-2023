from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic.dataclasses import dataclass
from sqlalchemy import ARRAY, Computed, String, text
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
    nickname: Mapped[str] = mapped_column(String(32), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    birthDate: Mapped[datetime] = mapped_column("birth_date")
    stack: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String(32)))
    search: Mapped[str] = mapped_column(
        String,
        Computed(
            text("nickname || ' ' || name || ' ' || coalesce(stack)"), persisted=True
        ),
        default=None,
    )
