class Human:

    def __int__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name


class Cat:
    def make_noise(self):
        pass


class Lion(Cat):
    def __init__(self):
        self.color = 'yellow'
        self.age = 17
        self.speed = 60
        self.character = 'Pride'

    def make_noise(self):
        print('Roar')


class Cheetah(Cat):
    def __init__(self):
        self.color = 'black'
        self.age = 12
        self.speed = 120
        self.character = 'friendly'

    def make_noise(self):
        print('Meow')


king = Lion()
sweet_cheetah = Cheetah()
king.make_noise()
print(king.color)
sweet_cheetah.make_noise()
