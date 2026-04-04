print ("welcome to bank of aditi" )
branch= input("enter your branch: ")
print (branch)

while True:
    ask= input("do you have account here?: ")
    if ask == "yes":
        name=input("enter your name: ")
        number= int(input("enter your number: "))
        address=input("enter your address: ")
        email= input("enter your email: ")
    else:
        print("please create your account.")
        print ("fill this details to create an account")
        cx_name= input("enter your name: ")
        cx_number= int(input("enter your number: "))
        cx_address= input("enter your address: ")
        cx_email= input("enter your email: ")
        cx_password= input("set your password: ")
        print("your account has been created")
        print("your account number is 12345")
        cx1= 12345
        curr_bal= 00
