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
