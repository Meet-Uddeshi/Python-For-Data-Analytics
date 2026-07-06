# Topic: OOP - Object-Oriented Programming.
# OOPs is used for code reusability and security. OOPs is like a blue print of all functions. It provides a clear structure to programs, makes code easier to maintain, reuse, and debug, helps keep your code DRY (Don't Repeat Yourself)

#  4 pillars of OOP:
# 1. Inheritance
# 2. Polymorphism
# 3. Encapsulation
# 4. Abstrction

# Class and Objects: 
# Class defines what an object should look like, and an object is created based on that class. For example:
# Class - Objects
# Fruit - Apple, Banana, Mango
# Car - Volvo, Audi, Toyota

# Example
class cars:
    x = ("Volvo", "Audi", "Toyota")

y =cars()
print(y.x)

# 1. Abstraction: 
# It is used for data hiding and to show only essential data or operations.

# Example
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


# 2. Inheritance:
# It means to use the properties of the parent class to child class. Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

# Super function:
# super() is used to access:
# parent class constructor
# parent class methods
# parent class variables

# Types of inheritance:
# 1. Single level - One child inherits one parent
# 2. Multilevel - Child inherits from another child class
# 3. Multiple - One child inherits multiple parents
# 4. Hierarchical - Multiple children inherit same parent
# 5. Hybrid - Combination of multiple inheritance types

# 1. Single level:
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()

d.sound() 
d.bark()

# 2. Multilevel:
class Grandfather:
    def house(self):
        print("Grandfather's House")

class Father(Grandfather):
    def car(self):
        print("Father's Car")

class Son(Father):
    def bike(self):
        print("Son's Bike")

s = Son()

s.house()
s.car()
s.bike()

# 3. Multiple:
class Father:
    def skills1(self):
        print("Programming")

class Mother:
    def skills2(self):
        print("Cooking")

class Child(Father, Mother):
    def skills3(self):
        print("Gaming")

c = Child()

c.skills1()
c.skills2()
c.skills3()

# 4. Hierarchical:
class Parent:
    def property(self):
        print("Parent Property")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()

c1.property()
c2.property()

# 5. Hybrid 
class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C(A):
    def method_c(self):
        print("Class C")

class D(B, C):
    def method_d(self):
        print("Class D")

obj = D()

obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()

# 3. Encapsulation:
# It is used for:
# Data hiding
# Security
# Controlled access
# Better maintainability
# Prevent accidental modification of data

# Self Keyword: 
# Self represents the current object (instance) of the class.It is used to access:
# Instance variables
# Instance methods

# Accessible Keywords
# Public: Accessible everywhere
# Protected: Accessible inside class and subclass
# Private: Accessible only inside class

# Example
class BankAccount:

    def __init__(self, name, balance):
        self.name = name            # public variable
        self._bank = "SBI"          # protected variable
        self.__balance = balance    # private variable

    # Public method to access private data
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Balance: {self.__balance}")

acc = BankAccount("Meet", 5000)

# Accessing public variable
print(acc.name)

# Accessing protected variable
print(acc._bank)

# Accessing private variable directly (Not Recommended)
print(acc.__balance)   # ERROR

# Access through public methods
acc.show_balance()

acc.deposit(2000)
acc.show_balance()

acc.withdraw(3000)
acc.show_balance()

# 4. Polymorphism: 
# Polymorphism is a fundamental concept of Object-Oriented Programming (OOP) that allows the same method, function, or interface to perform different actions depending on the object or situation. The word polymorphism means “many forms.” In programming, it enables flexibility and reusability because a single method name can behave differently for different classes. For example, a sound() method can produce different outputs for Dog, Cat, and Bird objects. Polymorphism improves scalability, reduces code duplication, and supports abstraction in software design. There are 2 types of polymorphrism:

# 1. Compiletime Polymorphism - Method Overloading 
# 2. Runtim Polymorphism - Method Overriding

# 1. Compiletime Polymorphism - Method Overloading
# Compile-time polymorphism, also known as method overloading, occurs when multiple methods perform different tasks based on different parameters. The decision about which method to execute is made before the program runs. Languages like Java and C++ support true method overloading by allowing multiple methods with the same name but different parameter lists. Python does not support true compile-time polymorphism directly, but it can simulate it using default arguments or variable-length arguments (*args). In this type of polymorphism, the behavior changes depending on the number or type of arguments passed to the method.

# Example
class Calculator:

    def add(self, a, b, c=0):
        print("Addition:", a + b + c)

obj = Calculator()

# Calling with 2 arguments
obj.add(10, 20)

# Calling with 3 arguments
obj.add(10, 20, 30)

# 2. Runtim Polymorphism - Method Overriding
# Runtime polymorphism, also known as method overriding, occurs when a child class provides a different implementation of a method already defined in the parent class. The method that gets executed is determined during program execution based on the object type. This is achieved through inheritance and dynamic method dispatch. For example, if both Dog and Cat classes override the sound() method of the Animal class, Python decides at runtime which version of sound() should execute. Runtime polymorphism is widely used in real-world applications because it enables extensibility, loose coupling, and flexible architecture design.

# Example
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

class Cat(Animal):

    def sound(self):
        print("Cat meows")

# Object creation
d = Dog()
c = Cat()

# Runtime decision
d.sound()
c.sound()