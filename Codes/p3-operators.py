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
name= "meet"
aadhar_no= 135678
phone_no= 9173359036
licence_no= 456789


if(aadhar_no== 1235678):
    if(name== "meet"):
        if(phone_no== 9173359036):
            print("you are verified")
        else:
            print("your number is not linked")
    else:
       print("your name is inappropriate")

else:                                      #nested_if - if(condition):
    if(licence_no== 45789):                              #if(condition):
      print("check your aadhar")                            #else:
    else:                                                       #print()
        print("your licence number is inappropriate")
