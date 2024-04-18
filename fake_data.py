from faker import Faker
from pprint import pprint
from config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, func


class FakeInfo:
    def __init__(self, count_users):
        self.fake = Faker('ru_RU')
        self.list_random_user = []
        self.count_users = count_users
        self.take_random_data()

    def take_random_data(self):
        for i in range(self.count_users):
            login = self.fake.first_name()
            email = self.fake.email()
            password = self.fake.password()
            date_of_registration = self.fake.date_between(start_date='-10y', end_date='today')
            self.list_random_user.append((login, email, password, date_of_registration))


class User(Base):
    # Этот класс представляет пользователя моего блога
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    # Хранение паролей в зашифрованном виде
    password: Mapped[str] = mapped_column(String, nullable=False)
    date_of_registration: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    def __init__(self, login, email, password, date_of_registration):
        self.login = login
        self.email = email
        self.password = password
        self.date_of_registration = date_of_registration

    def __str__(self):
        return f'User - {self.login}, {self.email}, {self.password}, {self.date_of_registration}'


if __name__ == '__main__':
    instance_FakeInfo = FakeInfo(4)

    for user_data in instance_FakeInfo.list_random_user:
        man = User(*user_data)
        print(man)
