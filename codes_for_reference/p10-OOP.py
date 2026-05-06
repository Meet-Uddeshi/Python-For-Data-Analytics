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
from multiprocessing.pool import worker


class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())



# inheritance
# inheritance means it uses the parent class details.
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#
# Parent class is the class being inherited from, also called base class.
#
# Child class is the class that inherits from another class, also called derived class.
# types of inheritance:
# 1. single level: it only has 1 parent and 1 child classmethod
# 2. Multilevel: it has 1 parent class 1 child class and 1 sub child class in it.
# 3. MUltiple : it has 1 parent class and more than 2 child class in it.

# java and c++ doesnot support multiple inheritance it requires interface to worker(
# code reusability
# less complex
# less length of code
# CHILD CLASS CAN ONLY HAVE ONE PARENT CLASS WHEREAS PARENT CLASS CAN HAVE MULTIPE CHILD CLASS.

# Super(). - keyword used to inherit the parent class properties(parameters,methods/ function , variables, sub-class)
# init - is the constructor which used for distinct dat iteration(line by line)

# Encapsulation: data protection
# Polymorphism - method overloading and overriding, constructor

class