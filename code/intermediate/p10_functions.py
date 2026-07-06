# Topic: User can create UDF(User Define Functions). It is used for modular code design, less complexity and code reusability. Keyword "def" is used for creating function. Function can be parameterized and non-parameterized. It uses return keyword to return any type of value after processing of function which can store in variable.

# Operators
# . (dot operator) = to call any function
# -> (arrow operator) = to define return value data typpe. It is optional to use.

# 1) Non-parameterized function
def my_function():
  print("Hello in the new world")
my_function()

# 2) Parameterized function
def my_greeting():
    return "Good morning"
message = my_greeting()
print(message)

# pass: function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement.
def my_function():
  pass

# Arguments / Parameters: information can be passed into functions as arguments.
def my_function2(fname):
  print(fname + " Shah")

my_function2("Hardik")
my_function2("Rohit")
my_function2("Sachin")

# Default Parameter Values
def my_function3(name = "friend"):
  print("Hello", name)

my_function3("Emil")
my_function3("Tobias")
my_function3()
my_function3("Linus")

# Passing Different Data Types
def my_function4(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function4(my_fruits)

# return: It uses return keyword to return any type of value after processing of function which can store in variable.
def my_function5(x, y):
  return x + y

result = my_function5(5, 3)
print(result)

# Example
def calculator(a,b,operator):
  if operator=="+":
    return a+b
  elif operator=="-":
    return a-b
  elif operator=="*":
    return a*b
  elif operator=="/":
    return a/b
  elif operator=="^":
    return a**b
  elif operator=="%":
    return a%b
  else:
    return "Invalid operator"

a= float(input("Enter a number: "))
b= float(input("Enter another number: "))
operator = input("Enter a calculation operator: ")
operator = operator.strip()

result = calculator(a,b,operator)
print("your first number entered is",a , "your second number entered is", b,
  "your amount after calculation is",result)

# Decorator: It provides tags and behavior to another functions. It starts with "@".
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

# Scope of variable
# 1) Local Scope
def my_func():
    x = 10
    print(x)
my_func()
# print(x)  Error (x not accessible outside)

# 2) Global Scope: Global scope variables can be access and modify by global keyword
x = 20
def my_func():
    print(x)
my_func()
print(x)

# 3) Enclosing Scope: It is used in nested functions.
def outer():
    x = 10

    def inner():
        print(x)

    inner()
outer()

# 4) Nonlocal Keyword
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)
outer()

# Recursion = Function calls itself in return keyword. Less complex, easy to identify logical error
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))

# Example
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