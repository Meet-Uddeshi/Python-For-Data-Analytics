# Topic: Nested if or nested condition.
# Nested if means condition inside condition

year = int(input("Enter a year: "))

# Nested if syntax. Nested condition can apply in all condition operators (if, if...else, if...elif, if...elif...else)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Example
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