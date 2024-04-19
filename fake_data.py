from faker import Faker

from config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func


class FakeInfo:
    def __init__(self, count_users):
        self.fake = Faker('ru_RU').seed_instance(4321)
        self.list_random_user = []
        self.count_users = count_users
        self.take_random_data()

    def take_random_data(self):
        for i in range(self.count_users):
            login = self.fake.first_name()
            email = self.fake.email()
            password = self.fake.password()
            data = {
                'login': login,
                'email': email,
                'password': password
            }
            self.list_random_user.append(data)


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
