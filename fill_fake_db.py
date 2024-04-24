# В этом модуле добавляем данные в базу
from fake_data import FakeInfo
from config import Base, engine
from sqlalchemy.orm import Session


def play_db(count_users):
    Base.metadata.create_all(engine)

    instance_FakeInfo = FakeInfo(count_users)

    with Session(engine) as session:
        for user in instance_FakeInfo.list_random_user:
            session.add(user)
        session.commit()

    print('\nБаза наполнена.')


# Base.metadata.drop_all(engine)
play_db(150)


# # Проверка того, что данные добавлены
# with Session(engine) as session:
#     users = session.query(User).all()
#     for user in users:
#         print(f"{user.login}, {user.email}, {user.password},{user.date_of_registration}")
