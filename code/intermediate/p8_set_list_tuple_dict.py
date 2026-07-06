# Topic: Sets, tuple, list and dictionary data structure in python.
# Note: List and array are same

# 1) Set
# Set: It is unordered list type data structure. It does not count duplication. It is defined with {...}.
a = {5,2,7,6,5}
b = {1,2,3,4,5,6,7}
print(a)
# print(a[1]) This is not correct because it is unordered list

# Set functions
# add(ele) = to add new element
# remove(ele) = to remove element
# union(set2) = to union both sets
# intersection(set2) = to intersect both set
# difference(set2) = to get element from set1 but not in set2
# symmetric_difference(set2) = to get element which are distinct from both the set
# pop() = to get only element from set
a.add(7)
a.remove(2)
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
while a:
    value = a.pop()
    print(value)
print(a)

# Set iteration using loops
# 1) for loop
for num in a:
    if num > 2:
        print(num)

# 2) while loop
total = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))

# 2) Tuple
# Tuple: it is ordered list type data structure. It is immutable. It allows duplication.
t = (5,8,9,56,4,71,2)
print(t)
print(t[0])
print(t[-1])

# Tuple functions
# len(t) = to find length of tuple
# max(t) = to find maximum element from tuple
# min(t) = to find minimum element from tuple
# index(ele) = to get specific element index from tuple
# cont(ele) = to get count of specific element in tuple
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(t.index(30))
print(t.count(20))

# Tuple iterations using loops
# 1) while loop
t = (5, 10, 15, 20)
i = 0
while i < len(t):
    print(t[i])
    i += 1

# 2) for loop
t = (10, 20, 30)
for item in t:
    print(item)

# 3) Dict
# Dict = It has key value or json type structure. It stands for dictionary.
a={"name":["aditi","hardik"],
   "age":[22,29],
   "marks":["pass","fail"]
}
print(a["name"],a["age"])

student = {
    "name": "Meet",
    "age": 22,
    "marks": 85,
    "city":"rajkot"
}
print(student)
student["city"] = "Ahmedabad"
student["marks"] = 90
print(student)

# Dict functions
# get(key) = to get values of specific key
# pop(key) = to remove specific key from dict
# clear() = to remove all keys and values
# keys() = to get all keys
# values() = to get all values of respected keys
# items() = to get both the things keys and values
print(student.get("age"))
student.pop("age")
student.popitem()
student.clear()
print(student)
print(student.keys())
print(student.values())
print(student.items())

# Dict iterations using loops
# 1) while loop
keys = list(student.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(key, ":", student[key])
    i += 1

# 2) for loop
for key, value in student.items():
    print(key, ":", value)