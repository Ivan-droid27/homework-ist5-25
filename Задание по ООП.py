# Суперкласс - Животное (Мать)
class Animal:
    def __init__(self, name, age, color, weight, habitat):
        self.n = name        # имя животного
        self.a = age         # возраст
        self.c = color       # цвет
        self.w = weight      # вес
        self.h = habitat     # среда обитания

    def sound(self, s):
        return f'{self.n} издает звук: {s}'

    def __str__(self):
        return f'Имя - {self.n}\nВозраст - {self.a}\nЦвет - {self.c}\nВес - {self.w} кг\nСреда обитания - {self.h}'

class Mammal(Animal):
    def __init__(self, name, age, color, weight, habitat, fur_type, warm_blooded):
        super().__init__(name, age, color, weight, habitat)
        self.fur = fur_type
        self.wb = warm_blooded

    def feed_milk(self):
        return f'{self.n} кормит детёнышей молоком.'

    def __str__(self):
        return super().__str__() + f'\nТип шерсти - {self.fur}\nТеплокровное - {"Да" if self.wb else "Нет"}'

class Reptile(Mammal):
    def __init__(self, name, age, color, weight, habitat, fur_type, warm_blooded, venomous):
        super().__init__(name, age, color, weight, habitat, fur_type, warm_blooded)
        self.v = venomous

    def shed_skin(self):
        return f'{self.n} сбрасывает кожу.'

    def __str__(self):
        return super().__str__() + f'\nЯдовитое - {"Да" if self.v else "Нет"}'
# Объект суперкласса Animal
animal_1 = Animal(name='Тигр', age=5, color='оранжевый', weight=220, habitat='лес')
print(animal_1)
print(animal_1.sound('рррррр! "Звуки тигра"'))
print('-' * 20)

# Объект млекопитающего
mammal_1 = Mammal(name='Медведь', age=10, color='коричневый', weight=300, habitat='тайга', fur_type='густая', warm_blooded=True)
print(mammal_1)
print(mammal_1.feed_milk())
print(mammal_1.sound('ррр! "Звуки медведя"'))
print('-' * 20)

# Объект пресмыкающегося
reptile_1 = Reptile(name='Кобра', age=3, color='черная', weight=5, habitat='джунгли', fur_type='нет', warm_blooded=False, venomous=True)
print(reptile_1)
print(reptile_1.shed_skin())
print(reptile_1.sound('шшшшш! ,"Звуки змеи"'))
print('-' * 20)
