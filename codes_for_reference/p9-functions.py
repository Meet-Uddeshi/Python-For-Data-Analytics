# function are re-usable. user defined functions can be made. parameterise and non parameterise function.
# def keyword is used to define any new function or initialise
# complexity is less and logical error is easily identified.
# void  - non-returnable value
#int - returnable value
# . operator is used to call function
# -> operator  - function return value which data type
# can be called in any of the files in your project.
# piece wise code as in one after teh other functions is run
#Arguments before / are positional-only, and arguments after * are keyword-only
# # calling a function:
# def my_function():
#   print("Hello in the new world")
# my_function()

# return the values
# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back:
# def my_greeting():
#     return "Good morning"
# message = my_greeting()
# print(message)

# If a function doesn't have a return statement, it returns None by default.
# def my_greeting():
#     print("Good morning")
# message = my_greeting()
# print(message)

# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
# def my_function():
#   pass

# Arguments
# Information can be passed into functions as arguments.
#
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.

# def my_function(fname):
#   print(fname + " Shah")
#
# my_function("Hardik")
# my_function("Rohit")
# my_function("Sachin")

# def my_function(name): # name is a parameter
#   print("Hello", name)
# my_function("Emil") # "Emil" is an argument

# By default, a function must be called with the correct number of arguments.
# If your function expects 2 arguments, you must call it with exactly 2 arguments.

# def my_function(city, country):
#   print(city + "," + country)
#
# my_function("Mumbai", "India")

# If you try to call the function with the wrong number of arguments, you will get an error as one of the arguement is missing
# def my_function(fname, lname):
#   print(fname + " " + lname)
#
# my_function("Emil")

# Default Parameter Values
# def my_function(name = "friend"):
#   print("Hello", name)
#
# my_function("Emil")
# my_function("Tobias")
# my_function()
# my_function("Linus")

# Keyword Arguments
# def my_function(animal,name):
#     print("I have a ", animal)
#     print("my animal is", "two years old and his name is", name)
#
# my_function(animal = "Cat", name="buddy")

# Positional Arguments
#
# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)
#
# my_function("dog", "Buddy")
#
# def my_function(bike, name):
#   print("I have a", bike)
#   print("My", bike + "'s name is", name)
# my_function("Activa", "Buddy")

# Mixing Positional and Keyword Arguments
#
# def my_function(animal, name, age):
#   print("I have a", age, "year old", animal, "named", name)
#
# my_function("dog", name = "Buddy", age = 5)

# Passing Different Data Types
#
# def my_function(fruits):
#   for fruit in fruits:
#     print(fruit)
#
# my_fruits = ["apple", "banana", "cherry"]
# my_function(my_fruits)

# Return Values
#
# def my_function(x, y):
#   return x + y
#
# result = my_function(5, 3)
# print(result)


# Returning Different Data Types.
# Functions can return any data type, including lists, tuples, dictionaries, and more.

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])