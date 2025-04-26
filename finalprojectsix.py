# Project 6: Build_Compose_and_Decorate_A_Complete_Traditional_OOP Practice_Series
# Instructor: Areej Shah

# 1. Using self
# Assignment:
# Create a class Student with Attributes name and marks. Use the self keyword to initialize these valuesvia a constructor. Add a method display() that prints student details.

#solution:
class Student:
    def __init__(self, name, marks):
       self.name = name
       self.marks = marks

    def display(self):
        print(f"Student Name {self.name}")
        print(f"Marks: {self.marks}")

student1 = Student("Areej", 85)
student1.display()


# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

#solution:
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_counter(cls):
        print(f"My total created objects are: {cls.count}")

obj1= Counter()
obj2= Counter()
obj3= Counter()
obj4= Counter()

Counter.display_counter()


# 3. Public Variable and Methods
# Assignment:
# Create a class car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

#solution:
class Car:
    def __init__(self, brand):
        self.brand = brand 

    def start(self):
        print(f"{self.brand} is strating...!")

my_car = Car("Audi")
print(my_car.brand)
my_car.start()


# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

#solution:
class Bank:
    bank_name = "UBL"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def disply(self):
        print(f"Account Holder: {self.account_holder} , Bank: {self.bank_name}")

account1 = Bank("Ali")
account2 = Bank("Hamza")

account1.disply()
account2.disply()

Bank.change_bank_name("Default Bank")

account1.disply()
account2.disply()
        