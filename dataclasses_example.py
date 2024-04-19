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

from pydantic import BaseModel
from pydantic.fields import Field, Ma

class People(BaseModel):
    name: str
    age: int
    mail: Email

    def __str__(self):
        return f'{self.name} is {self.age} years'



man_1 = People(name='Oleg',age='25')
man_2 = People(name='Tom',age=35)

print(man_1)
print(man_2)

