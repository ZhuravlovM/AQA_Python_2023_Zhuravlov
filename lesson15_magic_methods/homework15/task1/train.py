class Train:

    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def __len__(self):
        return len(self.cars)

    def __str__(self):
        car_info = '\n'.join(str(car) for car in self.cars)
        return f"\nTrain info:\n{car_info}"

    def print_passengers(self):
        for car in self.cars:
            car.print_passengers()


class TrainCar:

    def __init__(self, number, capacity):
        self.number = number
        self.passengers = []
        self.capacity = capacity

    def add_passenger(self, name, destination, place):
        if len(self.passengers) < self.capacity:
            passenger = {
                "name": name,
                "destination": destination,
                "place": place
            }
            self.passengers.append(passenger)
        else:
            print("Train car is full, cannot add more passengers.")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"Train Car {self.number} ({len(self.passengers)} passengers)"

    def print_passengers(self):
        for passenger in self.passengers:
            print('"name": "{}",\n"destination": "{}",\n"place": {}\n'.format(
                passenger["name"], passenger["destination"], passenger["place"]))


car1 = TrainCar(1, capacity=10)
car2 = TrainCar(2, capacity=10)
car3 = TrainCar(3, capacity=10)

car1.add_passenger("Rick Wright", "Liverpool", 9)
car1.add_passenger("Roger Daltrey", "London", 1)
car2.add_passenger("Paul McCartney", "Liverpool", 3)
car3.add_passenger("Liam Gallagher", "Manchester", 7)
car3.add_passenger("Johnny Marr", "Manchester", 2)
car3.add_passenger("Robbie Williams", "Stoke-on-Trent", 4)

train = Train()
train.add_car(car1)
train.add_car(car2)
train.add_car(car3)


print(len(car1))
print(len(car2))
print(len(car3))

print("Number of cars:", len(train))

print(train, "\n")

train.print_passengers()
