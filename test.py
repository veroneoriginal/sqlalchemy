from pathlib import Path
from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).parent
db_file_path = BASE_DIR / "birds_blog.sqlite3"

DB_URL = f'sqlite:///{db_file_path}'
DB_ECHO = True

# Связь между Python-приложением и БД
engine = create_engine(
    url=DB_URL,
    echo=DB_ECHO
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id}, email_address={self.email_address})"


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    verone_original = User(name="veroneoriginal", fullname="Veron Var",
                           addresses=[Address(email_address="verone@example.com")])

    new_user = User(name="new_user", fullname="")

    session.add_all([spongebob, sandy, patrick, verone_original, new_user])
    session.commit()



