import datetime
from abc import ABC, abstractmethod


class PieceOfArt(ABC):
    total_exhibits = 0

    def __init__(self, name, author, genre, creation_year: int):
        self.__name = name
        self.author = author
        self.genre = genre
        self.creation_year = creation_year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, alternative_name):
        self.__name = alternative_name

    @staticmethod
    def how_many_years_ago(created_year):
        difference = datetime.datetime.now().year - created_year
        return f"This piece of art was created {difference} years ago"

    @abstractmethod
    def information_booklet(self):
        pass

    @abstractmethod
    def move_to_exhibition(self):
        pass


class Painting(PieceOfArt):
    def __init__(self, name, author, genre, creation_year: int, paint_type):
        super().__init__(name, author, genre, creation_year)
        self.paint_type = paint_type

    def __prepare_for_exhibition(self):
        print("\nThis painting is ready for exhibition")

    def move_to_exhibition(self):
        self.__prepare_for_exhibition()
        PieceOfArt.total_exhibits += 1
        print("It was added to the exhibition. Total:", PieceOfArt.total_exhibits)

    def information_booklet(self):
        print(f"This is {self.name} and was created by {self.author} in {self.creation_year}")
        print(f"It's written in the the genre of {self.genre} using {self.paint_type}")


class Sculpture(PieceOfArt):
    def __init__(self, name, author, genre, creation_year: int, material):
        super().__init__(name, author, genre, creation_year)
        self.material = material

    def move_to_exhibition(self):
        print("\nSculpture is ready for the exhibition")
        PieceOfArt.total_exhibits += 1
        print("It was added to the exhibition. Total:", PieceOfArt.total_exhibits)

    def information_booklet(self):
        print(f"This sculpture is called {self.name} and was created by {self.author} in {self.creation_year}")
        print(f"It is made of {self.material}")


painting1 = Painting("The Treachery of Images", "Rene Magritte", "Surrealism", 1929, "Oil")
painting2 = Painting("Saturn Devouring His Son", "Francisco Goya", "Romanticism", 1823, "Oil on canvas")
sculpture1 = Sculpture("The Kiss", "Auguste Rodin", "Modern", 1889, "Marble")
sculpture2 = Sculpture("The Thinker", "Auguste Rodin", "Modern", 1902, "Bronze")

painting1.move_to_exhibition()
painting1.information_booklet()
print(painting1.how_many_years_ago(1929))
painting1.name = "Pipe"
print("Alternative name:", painting1.name)

sculpture1.move_to_exhibition()
sculpture1.information_booklet()
print(sculpture1.how_many_years_ago(1889))
sculpture1.name = "Le Baiser"
print("Name in French:", sculpture1.name)

print("\nTotal amount of exhibits:", PieceOfArt.total_exhibits)
