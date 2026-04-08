# #array
#index always starts with 0
#it is mutable
#length always = number of elements
#length = index+1
#array allows duplication- length, position, index is countable

a= ["xyz", "aditi", 1, "madari", 32.68, 1]
print(a)
i = 0
while i<len(a):
    if a[i] == "aditi":
        a[i]= "meet"
    i+=1
print(a)
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
#     i=i+1

