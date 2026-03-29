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
# syntax: if varible_name <,>,= :

 age= int(input("what is your age"))

if age >= 18 and age <= 65:
   print("you are eligible for licence")
 else :
   print("you are not eligible for licence")

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"

if marks >= 80 and marks < 90:
    grade = "B"

if marks >= 70 and marks < 80:
    grade = "C"

if marks >= 60 and marks < 70:
    grade = "D"

if marks < 60:
    grade = "F"

print(f"Student Name : {name}")
print(f"Marks        : {marks}")
print(f"Grade        : {grade}")

if marks < 60:
    print("You failed, please study harder!")

if marks >= 60:
    print("Congratulations, you passed!")