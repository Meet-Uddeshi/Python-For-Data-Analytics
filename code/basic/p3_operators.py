# Topic: Operators. There are certain types of operators like arithmatic, logical and conditional.

# Arithmatic: +,*,*,/,%,** For arithmatic operators python follows BODMAS rule
print("Enter non zero numbers.")
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

add = num_1 + num_2
sub = num_1 - num_2
mul = num_1 * num_2
div = num_1 / num_2
raise_to = num_1 ** num_2
modulus = num_1 % num_2
floor_div = num_1 // num_2
avg = (num_1 + num_2) / 2

print(num_1, num_2, sum, sub, mul, div, raise_to, modulus, floor_div) # Print statement for printing variable values

# Condition: if, if...else, if...elif, if...elif...else
n1 = int(input("Enter a number number: "))

# If syntax
if n1 % 2 == 0:
    print(n1, "is even")

# If...else syntax
if n1 % 2 == 0:
    print(n1, "is even")
else:
    print(n1, "is odd")

# If...elif syntax
if n1 < 0:
    print(n1, "is negative")
else:
    print(n1, "is positive")

# If...elif...else
if n1 == 0:
    print(n1, "is zero")
elif n1<0:
    print(n1, "is negative")
else:
    print(n1, "is positive")

# Logical: and, or, not
print("Enter a non zero numbers.")
s1 = int(input("Enter first number: "))
s2 = int(input("Enter second number: "))

if (s1 < 0) and (s2 < 0):
    print("Multiplication of both number is positive")
elif ((s1 < 0) and (s2 > 0)) or ((s1 > 0) and (s2 < 0)):
    print("Multiplication of both number is negative")
else:
    print("Multiplication of both number is positive")

# These are some other operators to check the condition.
# < Less than
# > Greater than
# <= Less than or equal to
# >= Greater than or equal to
# == To check and compare
# != Not equal comparison
# = To assign value to variable

