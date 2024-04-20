from fake_data import FakeInfo
from config import Base, engine
from sqlalchemy.orm import Session
from models import User


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

instance_FakeInfo = FakeInfo(4)

with Session(engine) as session:

    for user in instance_FakeInfo.list_random_user:
        session.add(user)

    session.commit()

# Проверка того, что данные добавлены
with Session(engine) as session:
    users = session.query(User).all()
    for user in users:
        print(f"{user.login}, {user.email}, {user.password},{user.date_of_registration}")
