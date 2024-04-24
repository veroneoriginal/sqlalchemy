# Выбрать все посты конкретного пользователя с 2-мя любыми тегами
from sqlalchemy import select
from sqlalchemy.orm import Session
from config import engine
from models import User, Post, Tag  # Импортируем модели Post и Tag из модуля

# Создаем подключение к базе данных
session = Session(bind=engine)

# Идентификатор пользователя и теги, по которым производится выборка
tag_names = ['#угол', '#спорт']


def get_posts_by_user_id(user_id):
    # Запрос на выборку постов конкретного пользователя с двумя тегами
    stmt = (select(Post).where(Post.user_id == user_id))
    user_posts = session.scalars(stmt).all()

    # Закрываем сессию
    session.close()
    print(len(user_posts))
    # Выводим посты
    for post in user_posts:
        print(f'{post.user_id=}')
        print(f'{post.title=}')
        print(f'{post.content=}')


# get_posts_by_user_id(7)
# get_posts_by_user_id(15)
# get_posts_by_user_id(17)
# get_posts_by_user_id(71)


def get_posts_by_tag(tag_name):
    # Запрос на посты, у которых есть определенный тег
    # первый вариант
    stmt = (select(Post)
            .join(Post.tags)
            .where(Tag.name == tag_name))
    posts_tag = session.scalars(stmt).all()

    # # второй вариант
    # posts_tag = session.query(Post).join(Post.tags).filter(Tag.name == tag_name).all()

    # Закрываем сессию
    session.close()
    print(len(posts_tag))

    for post in posts_tag:
        print(f'{post.title=}')
        print(f'{post.content=}')
        print(f'{post.user_id=}')


get_posts_by_tag('#металл')
get_posts_by_tag('#монета')
get_posts_by_tag('#висеть')
