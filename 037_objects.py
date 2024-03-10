from car import Car

car_1 = Car("Chevy", "Corvet", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

car_1.wheels = 2

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print(car_1.wheels)
car_1.drive()
car_1.stop()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
print(car_2.wheels)
car_2.drive()
car_2.stop()

print(Car.wheels)

Car.wheels = 6
print(car_1.wheels)
print(car_2.wheels)