# Abstract classes prevent users from creating an object ofthat class

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stopped the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You stopped the motorcycle")

    def stop(self):
        pass


car = Car()
motorcycle = Motorcycle()
