# в этом модуле генерим рандомные данные для наполнения бд

from faker import Faker
from config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func
from models import Post, Comment, Tag, User


class FakeInfo:
    def __init__(self, count_users):
        self.fake = Faker('ru_RU')
        self.fake.seed_instance(4321)
        self.list_random_user = []

        for _ in range(count_users):
            user = User(
                login=self.fake.first_name(),
                email=self.fake.email(),
                password=self.fake.password(), )

            post = Post(
                title=self.fake.catch_phrase(),
                content=self.fake.text(max_nb_chars=50),
                user=user)  # Привязка поста к пользователю

            comment = Comment(
                text_of_comment=self.fake.paragraph(),
                user=user,
                post=post)

            tag = Tag(name=f"#{self.fake.word()}")

            post.tags.append(tag)
            user.posts.append(post)
            self.list_random_user.append(user)


if __name__ == '__main__':

    class User(Base):
        # Этот класс представляет пользователя моего блога
        __tablename__ = 'users'
        id: Mapped[int] = mapped_column(primary_key=True)
        login: Mapped[str] = mapped_column(String, unique=True, nullable=False)
        email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
        # Хранение паролей в зашифрованном виде
        password: Mapped[str] = mapped_column(String, nullable=False)
        date_of_registration: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

        def __str__(self):
            return f'User - {self.login}, {self.email}, {self.password}, {self.date_of_registration}'


    instance_FakeInfo = FakeInfo(4)

    for user_data in instance_FakeInfo.list_random_user:
        man = User(**user_data)
