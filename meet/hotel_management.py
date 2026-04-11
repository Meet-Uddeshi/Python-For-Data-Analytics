print("Welcome to hotel meet")

while True:
    print("How can I help you ?")
    print("1. Book a new room  \n2. About hotel \n3. Exit")
    print("Please select a number")
    opt = int(input("Enter a number for choice: "))

    if opt == 1:
        print("Enter  your basic details: ")
        name = input("Enter your name: ")
        a_no = int(input("Enter you aadhar number: "))
        age = int(input("Enter your age: "))
        print(f"Welcone {name} in hotel meet. Verify your details. Your aadhar number is {a_no}. Your age is {age}.")
        print("Here are many types of room in this hotel.")
        print("1. Non A/C \n2. Delux \n3. A/C")
        choice = int(input("Please select a number: "))

        if choice == 1:
            nac_room = 1000
            print("This room is for at max 3 persons.")
            persons = int(input("Enter number of persons: "))
            days = int(input("Enter number of days: "))
            bill = nac_room * days
            print("You can check in. Your total is ", bill)

        elif choice == 2:
            d_room = 1700
            print("This room is for at max 4 persons.")
            persons = int(input("Enter number of persons: "))
            days = int(input("Enter number of days: "))
            bill = d_room * days
            print("You can check in. Your total is ", bill)

        elif choice == 3:
            ac_room = 2000
            print("This room is for at max 3 persons.")
            persons = int(input("Enter number of persons: "))
            days = int(input("Enter number of days: "))
            bill = ac_room * days
            print("You can check in. Your total is ", bill)

        else:
            print("Invalid choice")

    elif opt == 2:
        print("About US:")
        print("\t Hotel Meet located in junagadh, gujarat. Rate us on google and give feedback.")
        feedback = input("Enter feedback: ")
        print("Thanks for feedback. Your feedback is ",feedback)

    else:
        break