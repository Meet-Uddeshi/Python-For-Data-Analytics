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
import time

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

# from abc import ABC, abstractmethod
# from multiprocessing.pool import worker
#
#
# class Greet(ABC):
#     @abstractmethod
#     def say_hello(self):
#         pass
#
# class English(Greet):
#     def say_hello(self):
#         return "Hello!"
#
# g = English()
# print(g.say_hello())
#


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

# in the below example code if we have single child class then it will be defined as simple/single layer.
# if we have two or more child class then it wil be multiple inheritance
# if we have one child class and one or more  sub class in it then it will be under multilevel.
# class Parent:
#     def greet(self):
#         print("Hello from Parent")
#
# class Child(Parent):
#     pass
# class Child2(Parent):
#     pass
# class SubChild(Child,Child2):
#     pass
#
# c = Child()
# c.greet()  # Output: Hello from Parent

# Encapsulation:
# Encapsulation is about protecting data inside a class. type of encapsultion are as follows:
# 1.Private Properties - Get Set method is used.It is defined or update as double undercore.
# Get - value to be printed
# Set - used to update
# 2.Protected Variable - it is only for the particular file only.It is defined or updated as single underscore
#3. public can be used in whole project
#4. default - also in whole project
# Why Use Encapsulation?
# Encapsulation provides several benefits:
#
# Data Protection: Prevents accidental modification of data
# Validation: You can validate data before setting it
# Flexibility: Internal implementation can change without affecting external code
# Control: You have full control over how data is accessed and modified

# Get Method:
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age
#
#   def get_age(self):
#     return self.__age
#
# p1 = Person("Tobias", 25)
# print(p1.get_age())

# Set Method:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age
#
#   def get_age(self):
#     return self.__age
#
#   def set_age(self, age):
#     if age > 0:
#       self.__age = age
#     else:
#       print("Age must be positive")
#
# p1 = Person("Tobias", 25)
# print(p1.get_age())
#
# p1.set_age(26)
# print(p1.get_age())

# Protected method:

# class Person:
#   def __init__(self, name, salary):
#     self.name = name
#     self._salary = salary # Protected property
#
# p1 = Person("Linus", 50000)
# print(p1.name)
# print(p1._salary) # Can access, but shouldn't
#
# class Calculator:
#   def __init__(self):
#     self.result = 0
#
#   def __validate(self, num):
#     if not isinstance(num, (int, float)):
#       return False
#     return True
#
#   def add(self, num):
#     if self.__validate(num):
#       self.result += num
#     else:
#       print("Invalid number")
#
# calc = Calculator()
# calc.add(10)
# calc.add(5)
# print(calc.result)

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects
# or classes.
#
# Compile time method overloading - not supported in python
# run time method overriding  - in run time method overriding function remains same however, the output chnages.
# The self parameter is a reference to the current instance of the class.
#   self keword is used to define particular paramtere in the code.
# everytime ehrnever we take input from user or write a code for OOP we always need to define the objet.
# in the below example student1 and student2 are the objects.
# *args - means if it is agruement of methods and function the there can be multiple arguements in teh list .
# *kargs - means if its dictionary format or json format.
# class student:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
#
# student1_name = input("Enter the name: ")
# student1_age = int(input("Enter the age: "))
# student2_name = input("Enter the name: ")
# student2_age = int(input("Enter the age: "))
#
# student1 = student(student1_name,student1_age)
# student2 = student(student2_name,student2_age)
#
# print(student1.name,student1.age)
# print(student2.name,student2.age)
#
# # compile time polymor
#
# class calc:
#   def add(self,num1 = 1,num2 = 2, *args):
#     result = num1 + num2
#     for num in args:
#       result += num
#     return result
#
# meet = calc()
# print(meet.add(3,4,5,6,7,8,9))


# method and function is one and the same.

# run time polymer:
# In the below example : we have amd a class Animal and method /funtion  which returns some value.not
# going ahead we mad e a nother class of DOg and cat where we have inheritted the animal calss and then we have called the sound function or method.
# So if we create a object of  dog or cat anywhere in project it will give us the value defined in the code exampe "bark" in case of Dog and "meow" in case of cat.
# after that we made a variable animal wherein we stored the values and printed the same.
class Animal:
  def sound(self):
    return "Some generic sound"


class Dog(Animal):
  def sound(self):
    return "Bark"


class Cat(Animal):
  def sound(self):
    return "Meow"


# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
  print(animal.sound())