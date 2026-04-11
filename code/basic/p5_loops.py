# Topic: Loops. Loops are used for repetitive task. There are two types of loops entry control and exit control.
# There are 3 steps in loops to process,
# 1) Instantaneous variable (loop variable) initialization
# 2) Instantaneous variable condition check
# 3) Increment or decrement operators

# Entry control loop: There are two types of entry control loops for adn while loops. In this type of loop instantaneous variable checks condition and then execute the loop if condition is true. It execute minimum zero time.

# 1) while loop:
i = 0
while i <= 10:
    print(i)
    i = i + 1 # (i+= 1) or (i = i+1)

# Example: Factorial
i = 0
n = int(input("Enter a number: "))
fact = 1
while i <= n:
    if n==0 or n==1:
        fact = 1
    else:
        fact = fact * i
    i = i + 1

# Example: Print only factors of 5 till 50.
i = 1
while i<=50:
    if i % 5 == 0:
        print(i)
    i = i + 1

# Example: Print by decrement operators
i = 100
while i>=0:
    print(i)
    i = i - 1