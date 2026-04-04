# Loops are used for repetitive task. There are two types of loops entry control and exit control.
# There are 3 steps in loops to process,
# 1) Instantaneous variable (loop variable) initialization
# 2) Instantaneous variable condition check
# 3) Increment or decrement operators
from math import factorial

# entry control loops - checks conditions first and then executes
# exit control loops -  executes first and then checks conditions
#
# i = 100
# while i<=100:
#     print(i)
#     i-=1 #i= i+1
#     if i <= 0:
#         break

# while = True.it will run infinite times as it wont check the conditions
#
# i = 100
# while i>=1:
#     if i % 17 == 0:
#         print(i)
#     if i==34:
#             break
#     i = i - 1
#
# i = 1
# while i<=100:
#     print(i)
#     i-=3

# i = 1
# fact = 1
# while i <= 50:
#     if i==0 or i==1:
#         fact = 1
#     else:
#         fact = fact*i
#     i=i+1
# print(fact)

# day = input("Enter the day: ")
# if (day == "Monday") or (day=="Tuesday") or (day=="Wednesday") or (day=="Thursday") or (day=="Friday"):
#     print("Working Day")
# elif day=="Saturday":
#     print("Weekend Day")
# else :
#     print("Holiday Day")

#While True:
while True:
    check_students_details = input("Enter if students details available: ")
    if check_students_details == "Yes":
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        phone_number = int(input("Enter phone number: "))
        email = input("Enter email: ")
        print("here are the students details: ")
        print("Name is: ", name)
        print("Marks = ", marks)
        print("phone_number is = ", phone_number)
        print("email = ", email)
    else:
        break