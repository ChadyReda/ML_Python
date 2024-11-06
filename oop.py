# ------ inheretence ---------

class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
    
    def print_name(self):
        print(self.firstname, self.lastname)

person = Person(firstname="reda", lastname="dehbi")


class Student(Person):
    def __init__(self, fname, lname, year) -> None: 
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "To the class of", self.graduation_year)


student = Student(fname="chady", lname="dehbi", year=2022)

# -------- Polymorphism ---------

# the ability of a function to perfom on deferent inputs ex: len()

x = "Hello world"
print(len(x)) # 11

tuple = ("apple", "sumsung", "cherry")
print(len(tuple)) # 3

dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(dict)) # 3


# class polymorphism

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")


class Car(Vehicle):
    # override the method move
    def move(self):
        print("Drive!")
class Boat(Vehicle):
    # override the method move
    def move(self):
        print("Sail!")
class Plan(Vehicle):
    # override the method move 
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Tooring 20")
plan = Plan("Boesing", "747")

for x in (car1, boat, plan):
    x.move()