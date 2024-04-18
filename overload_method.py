class People:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        # отображение объекта в print
        return f'Имя {self.name}, возраст {self.age}, город {self.city}'

    def __repr__(self):
        # воспроизводство экземпляра класса
        return f'People(name="{self.name}", age="{self.age}", city="{self.city}")'



man = People('Tom', 35, 'Moscow')
print(f'{man!r}')
print(f'{man}')
# print(man.__str__())
# print(man.__repr__())
#
# man_1 = People('Jon', 30, 'Deli')
# print(man_1)
# print(man_1.__repr__())
#
# print([man, man_1])
