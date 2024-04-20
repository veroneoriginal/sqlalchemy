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
                password=self.fake.password(),
                posts=[
                    Post(
                        title=self.fake.catch_phrase(),
                        content=self.fake.text(max_nb_chars=50),
                        comments=[Comment(text_of_comment=self.fake.paragraph())],
                        tags=[Tag(name=f"#{self.fake.word()}")]
                    )
                ]
            )
            self.list_random_user.append(user)


#         self.list_with_post = []
#         self.list_with_comment = []
#         self.list_with_tag = []
#         self.count_users = count_users
#         self.take_random_data()
#         # self.get_random_text_for_post()
#         self.get_random_text_for_comment()
#         self.get_random_tag()
#
#
# def take_random_data(self):
#     """Метод генерит случайные данные для класса User в модуле models"""
#     for i in range(self.count_users):
#         login = self.fake.first_name()
#         email = self.fake.email()
#         password = self.fake.password()
#         posts = [
#             Post()
#         ]
#
#         data = {
#             'login': login,
#             'email': email,
#             'password': password
#         }
#         self.list_random_user.append(data)
#
#
# def get_random_text_for_post(self):
#     """Метод генерит случайные данные для класса Post в модуле models"""
#     for i in range(self.count_users):
#         title = self.fake.catch_phrase()
#         content = self.fake.text(max_nb_chars=50)
#         data_post = {
#             'title': title,
#             'content': content
#         }
#         self.list_with_post.append(data_post)
#
#
# def get_random_text_for_comment(self):
#     """Метод генерит случайные данные для класса Comment в модуле models"""
#     for i in range(self.count_users):
#         text_of_comment = self.fake.paragraph()
#         self.list_with_comment.append(text_of_comment)
#
#
# def get_random_tag(self):
#     """Метод генерит случайные теги для класса Tag в модуле models"""
#     for i in range(4):
#         tag = "#" + self.fake.word()
#         self.list_with_tag.append(tag)


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
        # print(user_data)
        man = User(**user_data)
        # print(man)
