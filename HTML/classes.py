car = {
    "make" : "toyota",
    "num_wheels" : 4,
    "model" : "camry",
    "year" : 1994,
    "num_miles" : 0
    }

class Student(object):
    name = ""
    course_list = []
    age = ""
    gpa = ""

    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def can_drive(self):
        if self.age > 16:
            return True
        else:
            return False

    def go_to_school(self):
        self.gpa += 0.1

    def enroll_in_course(self, course):
        course_list.append(course)

class CSSI_Student(Student):
    works_at_google = True

teddy = Student("Neill", 41, 0.0)
print(teddy.age)
print(teddy.name)
teddy.go_to_school()
print(teddy.gpa)
print(teddy.can_drive())

class Wizard:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def __str__(self):
        nameInfo = "Name: " + self.name
        healthStatus = "Health: " + str(self.health)
        return nameInfo + " " + healthStatus

    def changeName(self, newName):
        self.name = newName
    def eat(self):
        self.health = self.health + 5
        print("ENERGY!")
    def attack(self, otherPlayer):
        print("Expelliarmus! Harry was hit!!!!")
        otherPlayer.health = otherPlayer.health - 10

harry = Wizard("Harry", 50)
voldemort = Wizard("Voldy", 100)
print(harry)
print(voldemort)
voldemort.attack(harry)
print(harry)
harry.eat()
harry.eat()
harry.eat()
print(harry)
voldemort.changeName("The Dark Lord")
print(voldemort)
