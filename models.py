from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func, Table
from sqlalchemy.orm import relationship, mapped_column, Mapped, Session
from config import Base, engine
from typing import List
from fake_data import FakeInfo


class User(Base):
    # Этот класс представляет пользователя моего блога
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    # Хранение паролей в зашифрованном виде
    password: Mapped[str] = mapped_column(String, nullable=False)
    date_of_registration: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    posts: Mapped[List["Post"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    comments: Mapped[List["Comment"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        # воспроизводство экземпляра класса
        return f"<User(login='{self.login}', email='{self.email}', date_of_registration='{self.date_of_registration}')>"


class Comment(Base):
    # Класс для комментариев к постам
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(primary_key=True)
    text_of_comment: Mapped[str] = mapped_column(nullable=False)
    # внешний ключ, связывающий с постом
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    # внешний ключ, связывающий с пользователем
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    post: Mapped["Post"] = relationship(back_populates="comments")
    user: Mapped["User"] = relationship(back_populates="comments")


# Определение вспомогательной таблицы для связи многие ко многим между постами и тегами
association_table_post_tags = Table(
    'post_tags',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True))


class Post(Base):
    # Этот класс представляет собой отдельные посты или статьи в блоге
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    # взаимоотношения с другими классами
    user: Mapped["User"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")
    tags: Mapped[List["Tag"]] = relationship(secondary=association_table_post_tags, back_populates='posts')


class Tag(Base):
    # Класс для категоризации постов.
    # Каждый тег имеет название, и посты могут быть связаны с одним или несколькими тегами.
    __tablename__ = 'tags'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    posts: Mapped[List["Post"]] = relationship(secondary=association_table_post_tags, back_populates='tags')


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

instance_FakeInfo = FakeInfo(4)

with Session(engine) as session:
    for user_data in instance_FakeInfo.list_random_user:
        man = User(**user_data)
        session.add(man)
    session.commit()

# Проверка того, что данные добавлены
with Session(engine) as session:
    users = session.query(User).all()
    for user in users:
        print(f"{user.login}, {user.email}, {user.password},{user.date_of_registration}")
