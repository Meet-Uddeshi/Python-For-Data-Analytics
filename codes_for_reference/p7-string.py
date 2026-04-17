#string is immutable.
# group of characters.
# cannot be changed in run time as array.

# string slicing - part to be printed
# in key word - checks the characters in given string. Output = True /false
# upper, lower, capatalise,replace, trim, etc
# day ="monday"
# print("om" in day)

# String concatenation
a = "hardik"
b = " Shah"
# print(a+b)

# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.count("h")) - counts specific charcater in arguement
# print(a.title()) - Converts the first character of each word to upper case
# print(a.strip())
 # - only trims first and last characters

weekdays = ["monday","tuesday","wednesday","thursday","friday"]
weekends = ["saturday"]
holiday = ["sunday"]
days = input("Enter a day:")
space_not_day = days.strip()
lower_day = space_not_day.lower()
if lower_day == "monday" or lower_day== "tuesday" or lower_day== "wednesday" or lower_day== "thursday" or lower_day== "friday":
    print("Weekday")
elif lower_day == "saturday":
    print("Weekend")
elif lower_day == "sunday":
    print("Holiday")
else:
    print("Enter valid day")

