#Create a Staff class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methods
from person import *
class Staff(Person):
    
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def giveRaise(self, salary, amount):
        self.salary = salary + amount

    def info(self, salary):
        return (f"Hey Students My name is {self.name} and I make ")