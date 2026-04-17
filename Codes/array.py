# #array
#index always starts with 0
#it is mutable
#length always = number of elements
#length = index+1
#array allows duplication- length, position, index is countable
#length- numnber of elements
from os import remove

from Tools.demo.sortvisu import insertionsort

# Array iterations. For this process must need to use loops. Any operations in array must be applied on array index.
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
#
# # Array element insertion. Array functions append and insert used.
# m = [2,3,4,5,6,7,8,9]
# print(m)
# m.append(10)    # Append function/method is used to add new element in array runtime at last index.
# print(m)
# m.insert(3,"aditi")   # Insert function/method is used to add new element in array at specific index and if index is not define then this function takes last index by default to add new element in array.

# a= ["xyz", "aditi", 1, "madari", 32.68, 1]
# print(a)
# i = 0
# while i<len(a):
#     if a[i] == "aditi":
#         a[i]= "meet"
#     i+=1
# print(a)
#mutable- if value is known then use if
# Or if value is not known then use indexing - i== 1

# # print(a[0], a[1])
# len (a)
# print(len(a))
#
# a= ["aditi", "madari", 22, 9173359036, "b+", "yellow"]
# # age = int(input("Enter your age to find that in array: "))
# i=0
# while i < len(a):     #we can't use = here becuase- length = index+1
#     if a[i]==22:
#         print("Index is ",i)
#         print("Position is ", i+1)
#         print("Element is ",a[i])
#         break
#     i=i+1ti
#
# a=["madari", "aditi", "literature", 12345, 56.90, "mandvi"]
## a.insert (5,"kutch")
# # print(a)
# print(a)
# while True:
#     k = input("do you want to add another value?: yes/no ")
#     if k=="no":
#         print("thank you!")
#         print(a)
#         break
#     else:
#         i = input("what value you want to add?: ")
#         j = int(input("where you want to add?: "))
#         a.insert(j, i)
# a=[]
# m=[]
# h=[]
# while True:
#    ques=input("in which part you want to add value? a/m/h: ")
#    i = input("what value you want to add?: ")
#    if ques == "a":
#      print(a.append(i))
#      print(a)
#
#    elif ques == "m":
#        print(m.append(i))
#        print(m)
#
#    elif ques == "h":
#        print(h.append(i))
#        print(h)
#    else:
#        print("thanks!")
#        break

# a=["madari", "aditi", "literature", 12345, 56.90, "mandvi"]
# #how to print in between elements in array
# i=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#  11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#  91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
# print(i[3::2])
#
#
# def aditi(n):
#     return n/2
# print(aditi(5))
#
#
#FOR loop
#IN- can use in array iteration
#RANGE-can use in array and without array
# a = ["madari", "aditi", "literature", 12345, 56.90, "mandvi"]
# for aditi in a :
#     print(a[1:5:])  #slicing
#     break
# print(aditi)  #if we take instentenious array out of loop then it will print the first value of the array
# # And if we run instenious array in loop then it will print all the value till the loop iterates
#
# for i in range(3,20,2): #range-function, (parameters)
#     print(i)

# sort- to set ascending and descending value
# reverse- to change the visevarse of the values
# appened- to insert value after last value
# insert- to insert value on specific position
# remove- to remove value
# pop - to remove specific value in particular array
# copy- to copy array ex: b=a.copy

aditi= ["Alpha", "Bravo", "Charlie", "Delta", "Echo",
 "Foxtrot", "Golf", "Hotel", "India", "Juliet",
 "Kilo", "Lima", "Mike", "November", "Oscar",
 "Papa", "Quebec", "Romeo", "Sierra", "Tango",
 "Uniform", "Victor", "Whiskey", "X-ray", "Zulu"]
#
# aditi.sort(reverse=True)
# print(aditi)
#
# aditi.reverse()
# print(aditi)
#
# aditi.append("Hello")
# print(aditi)
#
# aditi.insert(0,"madari")
# print(aditi)
#
# aditi.pop(3)
# print(aditi)
#
# cutie= aditi.copy()
#
# strings
# it is immutable
# can't change in run time like array
# group of character

# a="aditi"
# print(a[2:4]) #string slicing
#IN- checks the character in strings in form of true or false
# a="aditi"
# print("di" in a)

#count, index, in, upper, lower, title, capitalize, strip, replace and so on....
# a="aditi"
# m="madari"
# print(a+m) #string concatenation
#
# a="aditi"
# print(a.rstrip("ait")

days= input("enter the day: ")
space_not_day= days.strip()
lower_case= space_not_day.lower()
if lower_case == ("monday") or lower_case == ("tuesday") or lower_case == ("wednesday") or lower_case == ("thursday") or lower_case == ("friday"):
    print("it's weekday")
elif lower_case == ("saturday"):
    print("it's weekend")
else:
 print("it's holiday")