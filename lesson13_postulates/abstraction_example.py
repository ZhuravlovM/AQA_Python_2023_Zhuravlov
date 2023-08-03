from abc import ABC, abstractmethod


class Employee(ABC):
    a = 5

    def __init__(self, salary, position):
        self.salary = salary
        self.position = position

    @abstractmethod
    def do_work(self):
        pass

    def do_another_work(self):
        print(2 + 5)


class Engineer(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('i`m working')

    def _deploy_program(self):
        print('program is deploying rn')

    def __create_new_framework(self):
        print('framework is done')

    def __create_ifrastructure(self):
        print('infrastructure is done')

    def deploy(self):
        self.__create_new_framework()
        self.__create_ifrastructure()


class Programmer(Engineer):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('i`m writing programms')


class ToyotaEmployee(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('I`m doing Toyota stuff')


class RenaultEmployee(Employee):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('I`m doing Renault stuff')


# employee = Employee('worker', 2000)

toyota_employee = ToyotaEmployee('worker', 2100)

engi = Engineer(2, '1')
engi._deploy_program()
prog = Programmer(3, 5)
prog._deploy_program()
engi.deploy()
prog.deploy()


class Car(ABC):

    def __init__(self, wheels, color, fuel):
        self.wheels = wheels
        self.color = color
        self.fuel = fuel

    @abstractmethod
    def go_straight(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

    def open_window(self):
        print('window is opened')


class Electro(Car):

    def __init__(self, wheels, color, fuel):
        super().__init__(wheels, color, fuel)

    def go_straight(self):
        print('car is going straight')

    def refuel(self):
        print('car is charged')


class Gasoline(Car):

    def __init__(self, wheels, color, fuel):
        super().__init__(wheels, color, fuel)

    def go_straight(self):
        print('car is going straight')

    def refuel(self):
        print('car is refueled')


gasoline_car = Gasoline(4, 'red', 'gasoline')
electro_car = Electro(4, 'green', 'electricity')
gasoline_car.go_straight()
gasoline_car.refuel()
gasoline_car.open_window()
electro_car.go_straight()
electro_car.refuel()
electro_car.open_window()
