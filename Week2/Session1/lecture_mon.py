# def greeting(name):
#     # name = "Sal"
#     # print(f"Welcome Sal!")
#     return f"Welcome {name}!"

# print(greeting("Sal"))
# #print("Welcome Sal!")

# Class
# Attributes 
# Characteristics tied to a single instance of a class
# Methods
# Functions that usually manipulate attributes of the class (business logic)

class Person:
    #constructor method - used to create a single instance of the class
    #instance method
    def __init__(self, name, jump=3, physical=2, shoot=5):
        self.name = name
        self.jump = jump
        self.physical = physical
        self.shoot = shoot
        self.dojo = "Coding Dojo"
    
    # Hi, my name is Sal
    def welcome_message(self):
        #self.name
        print(f"Hi, my name is {self.name}")
        return self

    # Jump: 3 Physical: 2 Shoot: 5
    def stats(self):
        print("Player Stats")
        print(f"Jump: {self.jump}")
        print(f"Physical: {self.physical}")
        print(f"Shoot: {self.shoot}")
        return self

    def jumpTrain(self, hrs):
        self.jump += hrs
        return self
    
    def wentToSpace(self, hrs):
        self.jump -= hrs
        return self

    @classmethod
    def future_method(cls):
        pass

    @staticmethod
    def static_method():
        pass


emily = Person("Emily")
emily.welcome_message()
emily.stats()
print(emily.jumpTrain(2).jumpTrain(1).jumpTrain(3).stats().wentToSpace(1).stats())

# bob = Person("Bob", jump=1, shoot=9)
# bob.welcome_message()
# bob.stats()
# max_jump_stat = 10
# carol = Person("Carol", max_jump_stat, 9)
# carol.welcome_message()
# carol.stats()






