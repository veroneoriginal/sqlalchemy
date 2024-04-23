# Блог про экзотических птиц

from config import engine, Base
from sqlalchemy.orm import Session
from models import User, Post, Comment, Tag


def main():
    Base.metadata.create_all(bind=engine)
    session = Session()
    try:
        # Здесь могут быть добавлены операции с базой данных
        # Например, создание начальных данных
        user = User(name="Tomas Shelbi", email="tomas@example.com")
        session.add(user)
        session.commit()
    except Exception as e:
        # Откат транзакции в случае ошибки
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Обязательное закрытие сессии
        session.close()


if __name__ == '__main__':
    main()
