#function
# funcations can be called in entire project
#use - code reusability, logical error can be identified easily, def keyword, functions can be parameterised / non parameterised
# return value - intiger, non return value- void
#return- dynamic, static,
#. operator- function call
#-> operator- return value of function would be in which data type
# piece vise code

#Function with Parameters
# def greet(name):
#     print("Hello", name)
#
# greet("Aditi")
# greet("Rahul")
#
# #Function with Return Value
# def add(a, b):
#     return a + b
#
# result = add(5, 3)
# print(result)

# num1= float(input("Enter a number 1: "))
# num2 = float(input("Enter a number 2: "))
# oper=input("Enter your operator: ")
# space= oper.strip()
#
# def calc(num1, space, num2 ):
#     if space == "+":
#         return num1 + num2
#     elif space == "-":
#         return num1 - num2
#     elif space == "*":
#         return num1 * num2
#     elif space == "/":
#         return num1 / num2
#     elif space == "%":
#         return num1 % num2
#     else:
#         return "Please enter a valid operator"
# result = calc(num1, space, num2)
# print(result)
# print("your first number is", num1, ", your second number is", num2, "and your operator is", oper,". therefore, your result is", result )


# #Function with Default Parameters
# def greet(name="Guest"):
#     print("Hello", name)
#
# greet()
# greet("Aditi")
#
# #Function with Multiple Arguments (*args)
# def total(*numbers):
#     print(sum(numbers))

# total(1, 2, 3)
# total(5, 10, 15, 20)
#
# #Function with Keyword Arguments (**kwargs)
# def info(**data):
#     print(data)
#
# info(name="Aditi", age=22)
#
# #Local Scope
# def my_func():
#     x = 10   # local variable
#     print(x)
# my_func()
# # print(x) ❌ Error (x not accessible outside)
#
# #Global Scope
# x = 20  # global variable
# def my_func():
#     print(x)
# my_func()
# print(x)
#
# #Modify Global Variable
# x = 10
# def change():
#     global x
#     x = 50
#
# change()
# print(x)
#
# #Enclosing Scope (Nested Functions)
# def outer():
#     x = 10
#
#     def inner():
#         print(x)  # accessing outer variable
#
#     inner()
# outer()
#
# #Nonlocal Keyword
# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x = 20
#
#     inner()
#     print(x)
# outer()
#
# #Decorator
# def my_decorator(func):
#     def wrapper(name):
#         print("Before")
#         func(name)
#         print("After")
#     return wrapper
#
# @my_decorator
# def greet(name):
#     print("Hello", name)
#
# greet("Aditi")

#lambda - key word
# one line function, less complex, faster execusion
# when you know what exactly you wanna do one particular expression then use lambda
# when you wanna do multiple expressions then use def

import math

circle_area = lambda r: math.pi * r * r
circle_circumference = lambda r: 2 * math.pi * r
circle_diameter = lambda r: 2 * r

rectangle_area = lambda l, w: l * w
rectangle_perimeter = lambda l, w: 2 * (l + w)
rectangle_diagonal = lambda l, w: math.sqrt(l * l + w * w)

triangle_area = lambda b, h: 0.5 * b * h
triangle_perimeter = lambda a, b, c: a + b + c
triangle_hypotenuse = lambda a, b: math.sqrt(a * a + b * b)

square_area = lambda s: s * s
square_perimeter = lambda s: 4 * s
square_diagonal = lambda s: math.sqrt(2) * s

sphere_volume = lambda r: (4 / 3) * math.pi * r * r * r
sphere_surface = lambda r: 4 * math.pi * r * r

cylinder_volume = lambda r, h: math.pi * r * r * h
cylinder_surface = lambda r, h: 2 * math.pi * r * (r + h)


def get_shape():
    print("\n1. Circle  2. Rectangle  3. Triangle  4. Square  5. Sphere  6. Cylinder")
    return input("Enter shape number: ")


def get_function(shape):
    if shape == "1":
        print("1. Area  2. Circumference  3. Diameter")
    elif shape == "2":
        print("1. Area  2. Perimeter  3. Diagonal")
    elif shape == "3":
        print("1. Area  2. Perimeter  3. Hypotenuse")
    elif shape == "4":
        print("1. Area  2. Perimeter  3. Diagonal")
    elif shape == "5":
        print("1. Volume  2. Surface Area")
    elif shape == "6":
        print("1. Volume  2. Surface Area")
    return input("Enter function number: ")


def calculate(shape, function):
    if shape == "1":
        r = float(input("Enter radius: "))
        if function == "1":
            return circle_area(r)
        elif function == "2":
            return circle_circumference(r)
        elif function == "3":
            return circle_diameter(r)

    elif shape == "2":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        if function == "1":
            return rectangle_area(l, w)
        elif function == "2":
            return rectangle_perimeter(l, w)
        elif function == "3":
            return rectangle_diagonal(l, w)

    elif shape == "3":
        if function == "1":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            return triangle_area(b, h)
        elif function == "2":
            a = float(input("Enter side A: "))
            b = float(input("Enter side B: "))
            c = float(input("Enter side C: "))
            return triangle_perimeter(a, b, c)
        elif function == "3":
            a = float(input("Enter side A: "))
            b = float(input("Enter side B: "))
            return triangle_hypotenuse(a, b)

    elif shape == "4":
        s = float(input("Enter side: "))
        if function == "1":
            return square_area(s)
        elif function == "2":
            return square_perimeter(s)
        elif function == "3":
            return square_diagonal(s)

    elif shape == "5":
        r = float(input("Enter radius: "))
        if function == "1":
            return sphere_volume(r)
        elif function == "2":
            return sphere_surface(r)

    elif shape == "6":
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        if function == "1":
            return cylinder_volume(r, h)
        elif function == "2":
            return cylinder_surface(r, h)

    return "Invalid choice!"


def main():
    print("===== GEOMETRY CALCULATOR =====")
    while True:
        shape = get_shape()
        if shape == "0":
            print("Goodbye!")
            break
        function = get_function(shape)
        result = calculate(shape, function)
        print("Result =", result)

main()

meet = get_shape()
shape = get_function(meet)
cal = calculate(shape, meet)
print(cal)

#operation vise functions- space

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))


def fib(n):
    try:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    except Exception as e:
        print("Error:", e)

num = int(input("Enter a number: "))
print("Fibonacci:", fib(num))