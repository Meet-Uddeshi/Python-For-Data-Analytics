# 1D- row
# 2D- row & column
#
# a=[["aditi",1], [22,"cool",2,5,"madari"]]
# print(a[0])

#list = array- allows duplication, mutable, indexed
# fruits = ["apple", "banana", "mango", "apple"]
# print(fruits)
# print(fruits[0])   # apple
# print(fruits[-1])  # last item
#
# # (tapple) - row, allows duplication, indexed, has many functions, immutable
# t = (10, 20, 30, 20)
# # print(t)
# #
# # print(t[0])     # first element
# # print(t[-1])    # last element
#
# #count
# print(t.count(20))   # how many times 20 appears
#
# #index
# print(t.index(30))   # position of 30
#
# #funstions
# print(len(t))    # length
# print(max(t))    # maximum value
# print(min(t))    # minimum value
# print(sum(t))    # sum of elements
#
# #while loop
# t = (5, 10, 15, 20)
# i = 0
# while i < len(t):
#     print(t[i])
#     i += 1
#
# #for loop
# t = (10, 20, 30)
# for item in t:
#     print(item)

# {set} - no duplication, unorderded
# Creating sets
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
#
# # Add element
# a.add(7)
#
# # Remove element
# a.remove(2)
#
# # Union (all elements)
# print("Union:", a.union(b))
#
# # Intersection (common elements)
# print("Intersection:", a.intersection(b))
#
# # Difference (a - b)
# print("Difference:", a.difference(b))
#
# # Symmetric Difference
# print("Symmetric Difference:", a.symmetric_difference(b)) #not common
#
# #IN keyword
# print(3 in a)   # True

#examples of loops
#for loop
# data = {1, 2, 2, 3, 4, 4, 5}
# unique = set(data)
# for num in unique:
#     if num > 2:
#         print(num)
#
# #while loop
# total = 0
# num = int(input("Enter number (0 to stop): "))
# while num != 0:
#     total += num
#     num = int(input("Enter number (0 to stop): "))
#
# print("Total:", total)
#
# #while true
# i = 1
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1
#
# #pop
# numbers = {10, 20, 30, 40}
# while numbers:
#     value = numbers.pop()
#     print(value)

# # {dict} - json (key value pair)
# a={"name":["aditi","hardik"],
#    "age":[22,29],
#    "marks":["pass","fail"]
# }
# print(a["name"],a["age"])

# student = {
#     "name": "Aditi",
#     "age": 22,
#     "marks": 85,
#     "city":"rajkot"
# }

# print(student["name"])      # Aditi
# print(student.get("age"))   # gives value

# student["city"] = "Ahmedabad"   # add
# student["marks"] = 90           # update
# print(student)

# student.pop("age")      # remove specific key
# student.popitem()       # remove last item
# student.clear()       # remove all
# print(student)
#
# print(student.keys())    # all keys
# print(student.values())  # all values
# print(student.items())   # key-value pairs
#
# #for loop
# for key in student:
#     print(key)
#
# #for loop key value pair
# for key, value in student.items():
#     print(key, ":", value)
#
# #while loop
# keys = list(student.keys())
# i = 0
# while i < len(keys):
#     key = keys[i]
#     print(key, ":", student[key])
#     i += 1
#
# #nested loop
# students = {
#     1: {"name": "Aditi", "age": 22},
#     2: {"name": "Hardik", "age": 29}
# }
# for id, data in students.items():
#     print("ID:", id)
#     for key, value in data.items():
#         print(key, value)
#
# #copy
# new_student = student.copy()
#
# #update multiple values
# student.update({"age": 23, "marks": 95})