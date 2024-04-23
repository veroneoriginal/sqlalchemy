# Выбрать все посты конкретного пользователя с 2-мя любыми тегами


from sqlalchemy.orm import Session
from config import engine
from models import Post, Tag  # Импортируем модели Post и Tag из вашего модуля

# Создаем подключение к базе данных
session = Session(bind=engine)

# Идентификатор пользователя и теги, по которым производится выборка
user_id = 4
tag_names = ['#отдел', '#легко']

# Запрос на выборку постов конкретного пользователя с двумя тегами

posts = session.query(Post).\
        join(Post.tags).\
        filter(Post.user_id == user_id).\
        filter(Tag.name.in_(tag_names)).\
        all()

# session.query(Post) - нужно выполнить запрос, возвращающий объекты типа Post
# join(Post.tags).\ - указывается необходимость выполнения SQL JOIN между таблицами Post и Tag.

# filter(Post.user_id == user_id).\
# добавляет условие к запросу, так что будут возвращены только те посты,
# user_id которых равен заданному user_id. Это уточнение позволяет выбирать посты конкретного пользователя.


# filter(Tag.name.in_(tag_names)).\
# условие фильтрации добавляет еще один критерий — возвращение постов,
# у которых есть теги с именами, указанными в списке tag_names.
# Tag.name.in_(tag_names) генерирует SQL выражение, которое проверяет, входит ли имя каждого тега в список tag_names.

# all()
# Завершает построение запроса и выполняет его, возвращая список всех постов,
# которые удовлетворяют заданным условиям. Если таких постов нет, вернется пустой список.


# Закрываем сессию
session.close()

print('\n')
print(len(posts))
print(type(posts))
print(type(posts[0]))
print('\n')

# Выводим посты
for post in posts:
    print(post.title)
    print(post.content)
