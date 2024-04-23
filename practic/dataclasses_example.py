# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name} is {self.age} years'
#
#
# man_1 = People('Oleg', 25)
# man_2 = People('Tom', 72)
#
# print(man_1)
# print(man_2)


# образец с pydantic-ом
from pydantic import BaseModel, EmailStr


class People(BaseModel):
    name: str
    age: int
    mail: EmailStr  # Используем EmailStr для проверки формата email

    def __str__(self):
        return f'{self.name} is {self.age} years'


man_1 = People(name='Oleg', age='25', mail='oleg@example.com')
man_2 = People(name='Tom', age=35, mail='tom@example.com')

print(man_1)
print(man_2)
