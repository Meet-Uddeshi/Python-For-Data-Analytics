#function
# funcations can be called in entire project
#use - code reusability, logical error can be identified easily, def keyword, functions can be parameterised / non parameterised
# return value - intiger, non return value- void
#return- dynamic, static,
#. operator- function call
#-> operator- return value of function would be in which data type
# piece vise code

#Function with Parameters
def greet(name):
    print("Hello", name)

greet("Aditi")
greet("Rahul")

#Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

#Function with Default Parameters
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Aditi")

#Function with Multiple Arguments (*args)
def total(*numbers):
    print(sum(numbers))

total(1, 2, 3)
total(5, 10, 15, 20)

#Function with Keyword Arguments (**kwargs)
def info(**data):
    print(data)

info(name="Aditi", age=22)

#Local Scope
def my_func():
    x = 10   # local variable
    print(x)
my_func()
# print(x) ❌ Error (x not accessible outside)

#Global Scope
x = 20  # global variable
def my_func():
    print(x)
my_func()
print(x)

#Modify Global Variable
x = 10
def change():
    global x
    x = 50

change()
print(x)

#Enclosing Scope (Nested Functions)
def outer():
    x = 10

    def inner():
        print(x)  # accessing outer variable

    inner()
outer()

#Nonlocal Keyword
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)
outer()

#Decorator
def my_decorator(func):
    def wrapper(name):
        print("Before")
        func(name)
        print("After")
    return wrapper

@my_decorator
def greet(name):
    print("Hello", name)

greet("Aditi")


