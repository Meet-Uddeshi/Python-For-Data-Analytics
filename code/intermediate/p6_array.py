# Topic: Array. Array's index starts with 0. Number of elements in array (length of array) is equal to index + 1. Arrays are mutable.

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

# Array element insertion. Array functions append and insert used.
m = [2,3,4,5,6,7,8,9]
print(m)
m.append(10)    # Append function/method is used to add new element in array runtime at last index.
print(m)
m.insert(3,"aditi")   # Insert function/method is used to add new element in array at specific index and if index is not define then this function takes last index by default to add new element in array.

