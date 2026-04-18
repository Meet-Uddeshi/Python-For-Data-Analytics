# nested loop - n number of loops used in 2d and multi-dimensional array
# 2d - rows n col
# 1 dimnsional = one row values.

# fruits = [["banana","mango"],["cherry","orange"]]
# print(fruits)

#   list and array are same - all arrays as list - dupe allowed, ordered(index), mutable
# tupple - row (), ordered (index), dupe allowed, multiple data types can be added, multiple functions as arrays.Immutable.
# set - {} displayed, unordered, no dupe allowed in output or count
# dict - {} json format or key value pair. ex: in table : coloumn will always in "". it can store any type of values (strings, arrays, etc.)

# names = {
#     "Name": ["Meet", "Hardik", "Aditi"] ,
#     "Age": [22, 29, 22],
#     "Percentage": [33, 99, 99]
# }
#
# print(names)

# Dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Delhi"
}

# ✅ 1. Get value

# print(student.get("name"))

# ✅ 2. Keys
# print(student.keys())

# ✅ 3. Values
# print(student.values())

# ✅ 4. Items (key + value)
# print(student.items())

# ✅ 5. Update dictionary
# student.update({"city": "New York"})
# student.update({"age": 21})
# print(student)

# ✅ 6. Remove item
#
# student.pop("age")
# print(student)

#➤ Loop through keys
# for key in student:
#     print(key)

# Loop through values

# for values in student.values():
#     print(values)

# Loop through key + value (most useful)

# for key, value in student.items():
    # print(key, value)

# marks = {"science":60,"maths":80,"geog":75}
# for subject,score in marks.items():
#     if score >=75:
#         print(subject,"good score")
#     else:
#         print(subject,"bad score")

# Count items

# count = 0
# for key, value in student.items():
#     count=+1
#     print(count)

## Tuple
# marks = (50,60,80)

# ✅ 1. Length
# print(len(marks))

# ✅ 2. Count

# marks = (60, 80, 75, 80, 90)
# print(marks.count(80))

# ✅ 3. Index
# print(marks.index(80))

# ➤ Simple Loop
#
# for score in marks:
#     if score >= 90:
#         print(score,"score is good")
#     else:
#         print(score,"score is bad")

# ➤ With Index (using range)

# marks = (60, 80, 75)

# for i in range(len(marks)):
#     print("Index", i,"Values",marks [i])


# for score in enumerate(marks):
#     print(score)

# sets
# No dupe print
#
fruits = {"apple", "banana", "cherry", "apple"}
# print(fruits)
#
# # Length
#
# print(len(fruits))

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}

# print(type(set1))

# for x in fruits:
#   print(x)

# Add Items
# fruits.add("orange")
# print(fruits)

# Add elements from tropical into fruits
# union() and update()
# tropical = {"kiwi", "dragon"}
#
# fruits.update(tropical)
# print(fruits)

# remove

# fruits.remove("orange")
# print(fruits)
#
# # discard(), pop(), clear(), del()
# fruits.discard("banana")
# print(fruits)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2)
# print(set3)

# set1 ={"hardik","aditi","meet"}
# set2 = {"India", "Australia","US","hardik"}

# set3 = set1.union(set2)
# print(set3)

# intersection()

# set3 = set1.intersection(set2)
# print(set3)


# difference()
# set3 = set1.difference(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1 - set2
# print(set3)

# difference_update()

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set1.symmetric_difference_update(set2)
# print(set1)

# fruits = {"apple", "cherry","banana"}
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))



