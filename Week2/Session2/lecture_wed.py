# class BankAccount:
#     def __init__(self):
#         pass

#     def withdrawal(self, amount):
#         pass

# class User:
#     def __init__(self):
#         self.name = "Sal"
#         self.bank_account = BankAccount()

# sal = User()
# sal.bank_account.withdrawal(20)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hi my name is {self.name} I am {self.age} years old")

sal = Person("Sal", 29)
# sal.greeting()

class Superhero(Person):
    def __init__(self, superhero_name, real_name, age, power):
        super().__init__(real_name, age)
        self.superhero_name = superhero_name
        self.power = power

    def greeting(self):
        # super().greeting()
        print(f"Hi my name is {self.superhero_name} and my super power is {self.power}")

class Teacher(Person):
    bootcamp_name = "Coding Dojo"
    def __init__(self, name, age, stack):
        super().__init__(name, age)
        self.stack = stack
    def greeting(self):
        print(f"Hi my name is {self.name} and I teach {self.stack}")

    @classmethod
    def set_bootcamp_name(cls, name):
        cls.bootcamp_name = name

    @classmethod
    def create_random_teacher(cls):
        return Teacher("Random", 30, "Java")

    @staticmethod
    def is_valid_stack(name):
        if name == 'Python' or name == 'Java':
            return True
        return False


print(Teacher.bootcamp_name)
Teacher.set_bootcamp_name("Coding Dojo Inc.")
print(Teacher.bootcamp_name)

sal_the_instructor = Teacher("Sal The Instructor", 29, "Python")
bob_the_instructor = Teacher("Bob The Instructor", 35, "Java")
phony_the_instructor = Teacher("Phony The Instructor", 29, "Phony")

print(f"Is {sal_the_instructor.name}'s stack in the curriculum?: {Teacher.is_valid_stack(sal_the_instructor.stack)}")
print(f"Is {phony_the_instructor.name}'s stack in the curriculum?: {Teacher.is_valid_stack(phony_the_instructor.stack)}")


spider_man = Superhero("Spider-Man", "Peter Parker", 16, "Super Strength")
my_list = [sal, spider_man, sal_the_instructor]    
for item in my_list:
    #item = my_list[0] -> item = sal
    #item = my_list[1] -> item = spider_man
    item.greeting()