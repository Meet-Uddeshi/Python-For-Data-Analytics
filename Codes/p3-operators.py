#arithmatics, logical, condition
#arithmatics- +,-,division, %

#rule- /,*,+,-

# number1 = int(input("enter a number: "))
# number2 = int(input("enter another number: "))
# number3 = int(input("enter another number: "))
# number4 = int(input("enter another number: "))
#
# avg= (number1+number2+number3+number4)/4


# sum = number1 + number2
# minus = number1 - number2
# multiplication = number1 * number2
# division = number1 / number2
# modulo = number1 % number2

# print ("sum of number1 and number2",sum,"which is too large")
#print ("minus of number1 and number2",minus)
# print ("multiplication of number1 and number2",multiplication)
# print ("division of number1 and number2",division)
# print ("modulo of number1 and number2",modulo)
#
# print (f" sum of number1 and number2 {sum}")

#print ("average of number1, number2, number3, number4: ", avg)

#conditions
# syntax: if varible_name <,>, ==, !=, =>, <= :

#  age= int(input("what is your age"))
#
# if age >= 18 and age <= 65:
#    print("you are eligible for licence")
#  else :
#    print("you are not eligible for licence")
#
# name = input("Enter your name: ")
# marks = int(input("Enter your marks: "))
#
# if marks >= 90:
#     grade = "A"
#
# if marks >= 80 and marks < 90:
#     grade = "B"
#
# if marks >= 70 and marks < 80:
#     grade = "C"
#
# if marks >= 60 and marks < 70:
#     grade = "D"
#
# if marks < 60:
#     grade = "F"

#another-example

# city = input("Enter your city: ")
# temperature =int(input("Enter temperature: "))
#
# if temperature >= 40:
#     print(f"{city} is very hot today")
#
# elif temperature >= 25 and temperature < 40:
#     print(f"{city} is warm today")
#
# else:
#     print(f"{city} is cold today")

#if - else
# name= "meet"
# aadhar_no= 135678
# phone_no= 9173359036
# licence_no= 456789
#
#
# if(aadhar_no== 1235678):
#     if(name== "meet"):
#         if(phone_no== 9173359036):
#             print("you are verified")
#         else:
#             print("your number is not linked")
#     else:
#        print("your name is inappropriate")
#
# else:                                      #nested_if - if(condition):
#     if(licence_no== 45789):                              #if(condition):
#       print("check your aadhar")                            #else:
#     else:                                                       #print()
#         print("your licence number is inappropriate")

#online shopping
# item= bool(input("is item available?: (true/false) "))
# payment= input("is payment done?: ")
# address= input("Enter an address: ")
#
# if item:
#     if payment == "yes":
#         if address == "ahmedabad":
#          print("item is available")
#         else:
#             print("we dont deliver here.")
#     else:
#         print("please make a payment.")
#
# else:
#    print("we will get back to you once the item is available.")

# #job hiring
# degree = input("do you have degree?: ")
# experience = input("do you have experience?: ")
# interview_score = int(input("whats your interview score?: "))
#
# if degree == "yes":
#     if experience == "yes":
#         if interview_score >= 70:
#             print("Hired")
#         else:
#             print("Interview failed")
#     else:
#         print("Not enough experience")
# else:
#     print("Degree required")


#same exp. with diff sytax
# has_degree = input("Do you have a degree (yes/no): ")
#
# if has_degree == "yes":
#     experience = int(input("Enter your experience: "))
#
#     if experience >= 2:
#         interview_score = int(input("Enter interview score: "))
#
#         if interview_score >= 70:
#             print("Hired")
#         else:
#             print("Interview failed")
#     else:
#         print("Not enough experience")
# else:
#     print("Degree required")

# College Admission
# passed_12th = bool(input("have you passed 12th? (True/False) "))
# marks = int(input("Marks: "))
# cutoff = 80
# documents_submitted = True
#
# if passed_12th == True:
#     if marks >= cutoff:
#         if documents_submitted:
#             print("Admission granted")
#         else:
#             print("Submit documents")
#     else:
#         print("Marks below cutoff")
# else:
#     print("Not eligible for admission")


#example 
registration = bool(input("Enter if you are a registered(True/False): "))
if not registration:
    print("Please get registered first")
else:
    insurance = bool(input("Enter if you have insurance(True/False): "))
    if not insurance:
        print("Please buy an insurance before admission")
    else:
        doctor_available = bool(input("Doctor availibility(True/False)): "))
        if not doctor_available:
            print("Please come once doctor is available")
        else:
            print("You can be admitted.")