# full_name = input("Enter your full name: ")
# roll_number = int(input("Enter your roll number: "))
# course_enrolled = input("Enter your course enrolled: ")
# course_duration = float(input("Enter your course duration (months): "))
# professor = input("Enter your professor name: ")
#
# print(f"full_name of student:{full_name}\n")
# print(f"roll_number is:{roll_number}\n")
# print(f"course enrolled is:{course_enrolled}\n")
# print(f"duration of course is:{course_duration}\n")
# print(f"professor is:{professor}\n")
#
# age = int(input("Enter your age: "))
# weight = int(input("Enter your weight: "))
# if age == 30 and weight <= 40:
#     print("healthy")
# elif age > 30 or weight >= 80:
#     print("unhealthy")
# else:
#     print("obbese")
from distutils.command.build_scripts import first_line_re
from os import access

# number_1 = int(input("Enter first number: "))
# number_2 = int(input("Enter second number: "))
# addition = number_1 + number_2
# subtraction = number_1 - number_2
# multiplication = number_1 * number_2
# division = number_1 / number_2
# modulus = number_1 % number_2
# exponent = number_1 ** number_2
#
# print("the addition of two numbers", addition)
# print("the subtraction of two numbers", subtraction)
# print("the multiplication of two numbers",multiplication)
# print("the division of two numbers",division)
# print("the modulo of two numbers",modulus)
# print("the exponentiation of two numbers",exponent)

# number_1 = 15
# print(f"15*1 = {number_1*1}")
# print(f"15*2 = {number_1*2}")
# print(f"15*3 = {number_1*3}")
# print(f"15*4 = {number_1*4}")
# print(f"15*5 = {number_1*5}")
# print(f"15*6 = {number_1*6}")
# print(f"15*7 = {number_1*7}")
# print(f"15*8 = {number_1*8}")
#
# year = int(input("Enter the year: "))
# if ((year %4 ==0 and year %100 !=0) and (year %400 ==0)):
#     print("Yes")
# else:
#     print("No")
# nested if:
# year = 2800
# if (year %4 == 0):
#     if (year %100 != 0):
#         if (year %400 !=0):
#             print("Yes its a Leap Year")
#         else:
#             print("Not a Leap Year")
#
#     else:
#         print("Not a Leap Year")
# else:
#     print("Not a Leap Year")
# #
# indian = input("Are you Indian: ")
# pancard_holder = input("Are you Pancard Holder: ")
# income = float(input("How much is your income: "))
# print("The details of elgibility for taxation is as follows: \n"
#       f"Are you Indian:{indian}\n"
#       f"Are you Pancard Holder:{pancard_holder}\n"
#       f"How much is your income:{income}")
# if (indian == "yes"):
#     if (pancard_holder == "yes"):
#         if (income > 500000):
#             print("You are eligible to pay the tax")
#         else:
#             print("You are not eligible to pay the tax")
#     else:
#         print("You are not eligible to pay the tax")
# else:
#     print("You are not eligible to pay the tax")

# weight = int(input("Enter your weight (kgs): "))
# height = int(input("Enter your height(meters): "))
# BMI = weight / (height ** 2)
# any_disease = input("Do you have any disease?: ")
# if (any_disease=="yes"):
#     if (BMI> 18.5):
#         print("You are underweight")
#     else:
#         print("You are normal")
# else:
#     if (BMI> 25):
#         print("You are underweight")
#     else:
#         print("You are normal")
#
# ticket_holder = input("Enter if you are a ticket holder(y/n): ")
# id_holder = input("Enter if you hold a valid ID(y/n): ")
# baggage_limit = int(input("Enter baggage weight(kgs): "))
# if ticket_holder == "y":
#     print("buy ticket first to travel")
#     if id_holder == "y":
#         if baggage_limit   <= 50:
#             print("you are eligible to travel")
#         else:
#             print("Please pay extra amount for luggage")
#     else:
#         print("You donot hold a valid ID so not eligible to travel")
# else:
#     print("Please buy a ticket to travel")


#if first input doesnt fulfill the condition it should directly prompt else (end)
#boolean
#
# registeration = bool(input("Enter if you are a registered(True/False): "))
# if registeration == True:
#     insurance = bool(input("Enter if you have insurance(True/False): "))
#     if insurance == True:
#         doctor_available = bool(input("Doctor availibility(True/False)): "))
#         if doctor_available == True:
#             print("you can be admitted")
#         else:
#             print("Please come once doctor is available")
#     else:
#         print("Please buy an insurance before admission")
# else:
#     print("Please get registered first")

# active_plan = input("Do you have any active plan(y/n)?: ")
# payment_status = input("Plan amount (paid/un-paid)?: ")
# if active_plan == "y":
#     if payment_status == "paid":
#         print("you are platinum member")
#     else:
#         print("you are free member")
# else:
#     print("buy a membership plan")

# n= 11//3
# print(n)

# year = int(input("Enter a year: "))

# Nested if syntax. Nested condition can apply in all condition operators (if, if...else, if...elif, if...elif...else)
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# registration = bool(input("Enter if you are a registered(True/False): "))
# if not registration:
#     print("Please get registered first")
# else:
#     insurance = bool(input("Enter if you have insurance(True/False): "))
#     if not insurance:
#         print("Please buy an insurance before admission")
#     else:
#         doctor_available = bool(input("Doctor availibility(True/False)): "))
#         if not doctor_available:
#             print("Please come once doctor is available")
#         else:
#             print("You can be admitted.")

# principal =float(input("enter the principal:"))
# rate_of_int = float(input("enter the rate of interest:"))
# no_of_yrs = float(input("enter the number of years:"))
# simple_interest = (principal*rate_of_int*no_of_yrs/100)
# print("the simple interest is",simple_interest)

# #swapping numbers
# a,b = 25, 30
# print(a,b)
# a,b = b, a
# print(a,b)
# # print(a,b)# two values at a time
# # c = a
# # a=b
# # b=c
# # print(a,b)

# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))
# mul =1
# i= 1
#
# while i<=second_number:
#     mul = first_number * i
#     print(f"{first_number}*{i} = {mul}")
#     i = i + 1

