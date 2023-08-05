from abc import ABC, abstractmethod


class Road(ABC):
    def __init__(self, name, cover: int, length: int, bridges: int, crossroads: int):
        self.__name = name
        self.cover = cover
        self.length = length
        self.bridges = bridges
        self.crossroads = crossroads

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @abstractmethod
    def add_bridge(self):
        pass

    @staticmethod
    def length_between_bridges(length, bridges):
        bridges_gap = length / bridges
        return bridges_gap


class Highway(Road):
    def __init__(self, name, cover: int, length: int, bridges: int, crossroads: int):
        super().__init__(name, cover, length, bridges, crossroads)
        self.cover = 1

    def __prepare_for_bridge(self):
        print("Preparations done")

    def __prepare_docs(self):
        print("Docs are ready")

    def add_bridge(self):
        self.__prepare_for_bridge()
        self.__prepare_docs()
        self.bridges += 1
        print("Bridge added", self.bridges)


class Village(Road):
    def __init__(self, name, cover: int, length: int, bridges: int, crossroads: int):
        super().__init__(name, cover, length, bridges, crossroads)
        self.cover = 0

    def __prepare_for_bridge(self):
        print("Preparations done")

    def __prepare_docs(self):
        print("Docs are ready")

    def add_bridge(self):
        self.__prepare_for_bridge()
        self.__prepare_docs()
        self.bridges += 1
        print("Bridge added", self.bridges)


highway1 = Highway('e13', 1, 370, 4, 1)
village1 = Village('45', 0, 768, 2, 2)

highway1.add_bridge()
village1.add_bridge()

print(highway1.length_between_bridges(123, 2))

village1.name = 'e29'
print(village1.name)
