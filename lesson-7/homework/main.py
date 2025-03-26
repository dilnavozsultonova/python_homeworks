class Car:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def move(self):
        print("Car is moving")

d = Car('BMW',32424)
print(d.name)