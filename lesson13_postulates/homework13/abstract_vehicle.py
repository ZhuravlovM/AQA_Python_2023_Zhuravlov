from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def engine_start(self):
        pass

    @abstractmethod
    def engine_stop(self):
        pass

    @abstractmethod
    def reach_limiter(self):
        pass


class Subaru(Vehicle):

    def __init__(self, make, model, year, wheels_number):
        super().__init__(make, model, year)
        self.wheels_number = wheels_number

    def engine_start(self):
        print("Engine started")

    def engine_stop(self):
        print("Engine stopped")

    def reach_limiter(self):
        print("Stu-tu-tu")


class Impreza(Subaru):

    def __init__(self, make, model, year, wheels_number, turbo=True):
        super().__init__(make, model, year, wheels_number)
        self.turbo = turbo

    def get_info(self):
        print(f"Make:{self.make}, Model:{self.model}, Year:{self.year}, Wheels:{self.wheels_number}")

    def is_turbo(self):
        if self.turbo:
            print("This Impreza is turbo-charged")
        else:
            print("This Impreza is not turbo-charged")


impreza = Impreza(make="Subaru", model="Impreza", year=2004, wheels_number=4, turbo=True)

impreza.get_info()
impreza.is_turbo()
impreza.engine_start()
impreza.reach_limiter()
impreza.engine_stop()
