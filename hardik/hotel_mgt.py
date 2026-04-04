# print("Welcome to the Hotel_Mgt")
# rate_per_night = 1000
# while True:
#     rooms_available = input("are rooms avaialable?:")
#     if rooms_available == "Yes":
#         full_name = input("Enter customer full name: ")
#         id_num = input("Enter customer's ID number(AADHAR/PAN): ")
#         room_num = int(input("Enter room number: "))
#         payment_status = input("Enter payment status: ")
#         payment_mode = input("Enter payment mode: ")
#         booking_date = input("Enter booking date(dd/mm/yyyy): ")
#         no_of_days_of_booking = int(input("Enter number of days of booking: "))
#         payment_amount = no_of_days_of_booking * rate_per_night
#         print("payment amount is: ", payment_amount)
#     else:
#         print("Rooms not available")
#         break


salary= int(input("Enter your salary: "))
while salary<500000:
    print(salary)
    salary= salary + (salary * 0.10)



