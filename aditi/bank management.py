print ("welcome to bank of aditi" )
branch= input("enter your branch: ")
print ("welcome to branch of", branch)

cx_name= ("aditi")
cx1 = 12345
while True:
    ask= input("do you have account here?: ")
    if ask == "yes":
        if ask == "yes":
            name = input("enter your name: ")
            number = int(input("enter your account number: "))

            if name == cx_name and number == cx1:
                print("login successful")
            else:
                print("wrong details")


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




        curr_bal = 0

        while True:
                 print("\n1. deposit")
                 print("2. withdraw")
                 print("3. balance")
                 print("4. exit")

                 choice = input("enter choice: ")

                 if choice == "1":
                     amt = int(input("enter amount: "))
                     curr_bal += amt
                     print("deposited")

                 elif choice == "2":
                     amt = int(input("enter amount: "))
                     if amt <= curr_bal:
                         curr_bal -= amt
                         print("withdrawn")
                     else:
                         print("not enough balance")

                 elif choice == "3":
                     print("balance:", curr_bal)

                 elif choice == "4":
                     print("thank you! visit again.")
                     break

                 else:
                     print("invalid")
                     break