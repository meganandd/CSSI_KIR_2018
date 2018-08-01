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
