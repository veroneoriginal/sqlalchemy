from faker import Faker
from pprint import pprint

fake = Faker('ru_RU')
fake.seed_instance(431)
first_name = fake.first_name()
email = fake.email()
password = fake.password()
title = fake.catch_phrase()
content = fake.text(max_nb_chars=200)
text_of_comment = fake.paragraph()
tag = "#" + fake.word()

one_people = (f'first_name={first_name}, email={email}, password={password}, title={title},' 
              f'\ncontent={content}, \ntext_of_comment={text_of_comment}, \ntag={tag}')
pprint(one_people)
