# duck typing = concept where the class of an objectis less important than the methods/attributes which that class might have. The class type is not checked if minimym methods/attributes are present. "If it walks like a duck, and it quacks like a duck, then it must be a duck"


class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")


class Chicken:

    def walk(self):
        print("This chiken is walking")

    def talk(self):
        print("This chiken is clucking")


class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)
