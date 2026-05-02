# Topic: Sets, tuple, list and dictionary data structure in python.
# Note: List and array are same

# 1) Set
# Set: It is unordered list type data structure. It does not count duplication. It is defined with {...}.
a = {5,2,7,6,5}
b = {1,2,3,4,5,6,7}
print(a)
# print(a[1]) This is not correct because it is unordered list

# Set functions
# add = to add new element
# remove = to remove element
# union = to union both sets
# intersection = to intersect both set
# difference = to get element from set1 but not in set2
# symmetric_difference = to get element which are distinct from both the set
# pop = to get only element from set
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

