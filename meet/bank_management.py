print("Welcome to bank Meet")

while True:
    print("Enter your basic details:")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Welcome to meet bank {name}. Your age is {age}.")
    print("How can I help you ?")
    print("1. Create account \n2. Transactions \n4 Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        phone_number = int(input("Enter your phone number: "))

        if age < 16:
            print("Please enter a valid age")

        else:
            print("Your account is created successfully")
            ac_number = 123456789
            balance = 0.00
            print(f"Your account number is {ac_number} and balance is {balance}.")

    elif choice == 2:
        balance = float(input("Enter your bank balance: "))
        print("Select a transaction type: ")
        print("1. Credit \n2. Debit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("How much money you need to credit ?")
            credit_amount = float(input("Enter your credit amount: "))
            balance = balance + credit_amount
            print("Amount credited successfully. your bank balance is ",balance)

        elif choice == 2:
            print("How much money you need to debit ?")
            debit_amount = float(input("Enter your debit amount: "))

            if debit_amount > balance:
                print("Insufficient balance")

            else:
                balance = balance - debit_amount
                print("Amount debited successfully. Your bank balance is ",balance)

    else:
        print("Thanks for visiting bank.")
        break