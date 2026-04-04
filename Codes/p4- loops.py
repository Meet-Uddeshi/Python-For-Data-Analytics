# Topic: Loops. Loops are used for repetitive task. There are two types of loops entry control and exit control.
# There are 3 steps in loops to process,
# 1) Instantaneous variable (loop variable) initialization
# 2) Instantaneous variable condition check
# 3) Increment or decrement operators

# Entry control loop: There are two types of entry control loops for adn while loops. In this type of loop instantaneous variable checks condition and then execute the loop if condition is true. It execute minimum zero time.
# ------- Code for entry control loop ---------

# Exit control loop: Do..while loop is included in this type of loop. Exit control loop must execute st least one time because it execute first and then check condition for instantaneous variable.
# ---------- Code for exit control loop ----------

#while loop
# j=0
# while j<101:
#     print(j)
#     j+=1
#     if j==101:
#         break

# i=1
# while i<=100:
#     print(i)
#     i+=17

# i=1
# fact=1
# n= int(input("Enter a number: "))
# while i<=n:
#       if n==0 or n==1:
#           fact=1
#       else:
#           fact = fact*i
#       i+=1
# print(fact)

# i=252
# while i>=1:
#     if i%3 == 0:
#         print(i)
#     i-=1

# days= input("Enter the day: ")
#
# if days == ("monday") or days == ("tuesday") or days == ("wednesday") or days == ("thursday") or days == ("friday"):
#     print ("it's weekday")
# elif days == ("saturday"):
#     print ("it's weekend")
# else:
#     print ("it's holiday")

while True:
    ask = input("do we have any student?: ")
    if ask == "yes":
     name= input("Enter your name: ")
     marks= float(input("Enter your marks: "))
     phone= int(input("Enter your phone number: "))
     email= input("Enter your email address: ")
     print ("here are your details: ")
     print ("name: ",name)
     print ("marks: ",marks)
     print ("email: ",phone)
     print ("address: ",email)
    else:
       break