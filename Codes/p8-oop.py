#oop- object oriented programme
# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code
#Classes - it is a group of variables, methods, functions and so on.... ex- fruits
#object- it is instance of class    ex-Apple, Banana, Mango
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#objects can be changed based on its properties but class can not be changed.
# class aditi:
#     fruits= ("apple", "banana", "orange")
#
# a1=aditi()
# print(a1.fruits)


#abstraction is used for data hiding, means showing only the essential features
#abc- abstraction base class is used for python oop and its necessary to import it

# from abc import ABC, abstractmethod
#
# class Greet(ABC):
#     @abstractmethod
#     def say_hello(self):
#         pass  # Abstract method
#
# class English(Greet):
#     def say_hello(self):
#         return "Hello!"
#
# g = English()
# print(g.say_hello())
#
# #These properties are declared with @property decorator and marked as abstract using @abstractmethod.
# #Subclasses must implement these properties.
#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @property
#     @abstractmethod
#     def species(self):
#         pass  # Abstract property, must be implemented by subclasses
#
# class Dog(Animal):
#     @property
#     def species(self):
#         return "Canine"
#
# # Instantiate the concrete subclass
# dog = Dog()
# print(dog.species)

# Encapsulation
# Putting data and functions inside one class
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def display(self):
#         return f"{self.name} scored {self.marks}"
#
# s1 = Student("Aditi", 90)
# print(s1.display())


# Abstraction
# Show only important things, hide complexity
# class ATM:
#     def withdraw(self, amount):
#         if amount > 0:
#             return "Transaction Successful"
#         else:
#             return "Invalid Amount"


#Inheritance
# One class can use another class’s features
# class Animal:
#     def speak(self):
#         return "Animal speaks"
#
# class Dog(Animal):
#     def bark(self):
#         return "Dog barks"
#
# d = Dog()
# print(d.speak())   # from parent
# print(d.bark())    # from child



#Polymorphism
#One method works differently for different objects
# class Bird:
#     def sound(self):
#         return "Some sound"
#
# class Parrot(Bird):
#     def sound(self):
#         return "Parrot talks"
#
# class Crow(Bird):
#     def sound(self):
#         return "Crow caws"
#
# p = Parrot()
# c = Crow()
#
# print(p.sound())
# print(c.sound())
