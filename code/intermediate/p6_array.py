# Topic: Array. Array's index starts with 0. Number of elements in array (length of array) is equal to index + 1. Arrays are mutable. Arrays are ordered list. It can access by index.
a = [7,9,12,2.5,"abc"]
print(a)
print(a[2])
b = len(a)
print(b)

# Array iterations. For this process must need to use loops. Any operations in array must be applied n array index.
i = 0
a = [1,2,3,4,5,7,6,"meet"]
while i<len(a):
    print(a[i])
    i += 1

j = 0
while j<len(a):
    if a[j] == "meet":
        print(j)
    j = j + 1

for index in a: # in keyword is used for checking element in array
    print(a[index])

# Array element insertion. Array functions append and insert used.
m = [2,3,4,5,6,7,8,9]
print(m)
m.append(10)    # Append function/method is used to add new element in array runtime at last index.
print(m)
m.insert(3,"aditi")   # Insert function/method is used to add new element in array at specific index and if index is not define then this function takes last index by default to add new element in array.

# Array slicing.
print(m[1:4:2]) # array[starting_index:ending_index:gap/difference]. It takes 0 index, last index and 1 gap or difference by default.

# Negative indexing. To print from last
print(m[-1])

# Array functions
# append = to add new element in last index
# insert = to add new element in specific index
# pop = to delete element in array
# remove = to remove specific index element
# sort = to sort array. It takes by default ascending, For descending it takes argument
m.append(5)
m.insert(3,"meet")
m.pop(2)
m.remove(3)
m.sort()
print(m)

# In array for loop has in key word which is used to compare array values directly not index.
for i in m:
    print(i)

# Nested loop: Loop inside loop. It is generally used for more than 1d array or 1d matrix.

# Array element multiplication.

# 1) for lop
a = [[4,6],
     [8,3]]
b = [[9,7],
     [5,2]]
c = [[0, 0],
     [0, 0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k] * a[k][j]

for row in c:
    print(row)

# 2) while loop
a = [[4,6],
     [8,3]]
b = [[9,7],
     [5,2]]
c = [[0, 0],
     [0, 0]]

i = 0
while i < len(a):
    j = 0
    while j < len(b[0]):
        k = 0
        while k < len(b):
            c[i][j] += a[i][k] * b[k][j]
            k += 1
        j += 1
    i += 1

for row in c:
    print(row)

# Array element addition

# 1) for loop
a = [[4,6],
     [8,3]]
b = [[9,7],
     [5,2]]
c = [[0, 0],
     [0, 0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        c[i][j] = a[i][j] + b[i][j]

for row in c:
    print(row)

# 2) while loop
a = [[4,6],
     [8,3]]
b = [[9,7],
     [5,2]]
c = [[0, 0],
     [0, 0]]

i = 0
while i < len(a):
    j = 0
    while j < len(a[0]):
        c[i][j] = a[i][j] + b[i][j]
        j += 1
    i += 1

for row in c:
    print(row)