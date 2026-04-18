#array = always starts with 0
from os import remove

# indexing = len(n)-1

# a= ["apple","banana","orange","kiwi"]
# i= 0
# while i<len(a):
#     print(a[i])
#     i=i+1
# print(a)

# b=["Hardik","Meet","Aditi","Rohit"]
# i = len(b)-1
# while i>=0:
#     print(b[i])
#     i=i-1

# c=["India","Dubai","Pakistan","Australia"]
# i=0
# while i<len(c):
#     print(c[i])
#     i=i+1
#
# a= ["apple","banana","orange","kiwi"]
# b= ["Hardik","Meet","Aditi","Rohit"]
# c= ["India","Dubai","Pakistan","Australia"]
# i= 0
# j= 0
# k= 0
# while i < len(a):
#     print(a[i])
#     i=i+1
# while j < len(b):
#     print(b[j])
#     j=j+1
# while k < len(c):
#     print(c[k])
#     k=k+1


# days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# i=0
# while i<len(days):
#     print(days[i])
#     if days[i]=="Monday" or days[i]=="Tuesday" or days[i]=="Wednesday" or days[i]=="Thursday" or days[i]=="Friday":
#         print("Weekday")
#     elif days[i]==("Saturday"):
#         print("Weekend")
#     else:
#         print("Holiday")
#     i=i+1



# Topic: Array. Array's index starts with 0. Number of elements in array (length of array) is equal to index + 1. Arrays are mutable.
#
# #
# a = [7,9,12,2.5,"abc"]
# print(a)
# print(a[2])
# b = len(a)
# print(b)
#
# # Array iterations. For this process must need to use loops. Any operations in array must be applied n array index.
# i = 0
# a = [1,2,3,4,5,7,6,"meet"]
# while i<len(a):
#     print(a[i])
#     i += 1
#
# j = 0
# while j<len(a):
#     if a[j] == "meet":
#         print(j)
#     j = j + 1

# Array element insertion. Array functions append and insert used.
# k=-1
# m = [2,3,4,5,6,7,8,9]
# print(m[2:6:2])
# while k <= 0:
#     print(m[k])
#     k = k-1
#     if k == -9:
#         break


# m.append(10)    # Append function/method is used to add new element in array runtime at last index.
# print(m)
# m.insert(3,"aditi")   # Insert function/method is used to add new element in array at specific index and if index is not define then this function takes last index by default to add new element in array.
# print(m)

#: is used to print any of the middle elements.

# # print(fruits[2:15:3])
# fruits[0]="mango"
# print(fruits)

# for loop: In  - only used in array iteration used range used for with and without array. its an entry level loop
#
# for fruit in fruits:
#     print(fruits[1:6])
#     break
# if you print the loop variable then it will only print the value stored in first iteration.
# the above example is run in loop wherein the fruit is the loop variable and it will print all the element is the array.

# s = "meet"
# s[0] = "j"
# print(s)

# for x in range(10,21,2):
#     print(x)
# in range for the above example 10 is the starting value 21 till that value and 2 is difference value.the whoile bracket is called as arguement or parameters
#
# for fruit in range(len(fruits)):
#     print(fruits[::-1])
#     break

#  append(x): Adds an element to the end.
#  insert(i, x): Inserts element x at index i.
#  remove(x): Removes the first occurrence of x.
# ️ pop([i]): Removes and returns the item at index i (last item by default).
#  reverse(): Reverses the list in place.
#  sort(): Sorts the list (ascending by default).
# copy(obj): Creates a shallow copy. It duplicates the container but keeps references to the original nested items.



fruits = ["apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon","mango","mango",
    "mango", "nectarine", "orange", "papaya", "quince"]

fruits.insert(10, "orange")
# print(fruits)

fruits. remove("orange")
# print(fruits)
#
# fruits.pop(10)
# print(fruits)

# fruits.reverse()
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)

# veg=fruits.copy()
# print(veg)



