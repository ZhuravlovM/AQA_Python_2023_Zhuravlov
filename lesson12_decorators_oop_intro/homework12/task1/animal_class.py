class Penguin:
    def __init__(self, name, species, food, colour):
        self.name = name
        self.species = species
        self.food = food
        self.colour = colour

    def acquaintance(self):
        print(f"Це {self.name}, пінгвін породи : {self.species}")

    def hunt(self):
        print(f"Улюблена їжа {self.name} : це {self.food}")

    def appearance(self):
        print(f"Колір оперення {self.name} : {self.colour}")

    @staticmethod
    def penguin_info():
        print("Пінгвіни – безкрилі водоплавні створіння живуть тільки в землях південної півкулі")


penguin = Penguin("Фредді", "королівський", "кальмар", "чорно-білий")

print(penguin.acquaintance())
print(penguin.hunt())
print(penguin.appearance())

penguin.penguin_info()
