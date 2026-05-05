# OOP stands for Object-Oriented Programming.
# Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
# blue print of all functions.
# Advantages of OOP
# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code
# 4 pillars of OOP:
#
# Python Inheritance
# Polymorphism
# Encapsulation
# Abstrction



# Classes and objects are the two core concepts in object-oriented programming.
#
# A class defines what an object should look like, and an object is created based on that class. For example:
#
# Class - Objects
# Fruit - Apple, Banana, Mango
# Car - Volvo, Audi, Toyota
#
# in the above fruit and car is class defined and Apple, banana, AUdi etc is objects and Shimla apple, kashmiri apple
# are the properties
# Objects and properties can be changed but class cannot be changed.

# create class:

# abstarction is used for data hiding and to show only essential data or operations.

# class cars:
#     x = ("Volvo", "Audi", "Toyota")
#
# y =cars()
# print(y.x)

#
# ABC is base clase - Abstarction Base Class used for OOP
# only class i=needs to defiend no value needs to be taken

from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())



