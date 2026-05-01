# one liner function
# faster execution
# less complex
# lambda keyword
# expression use
# Implicit Return: The result of the expression is returned automatically; you do not use the return keyword.
# No Statements: They cannot contain statements like if, for, or print (as a statement), or multiple lines
#
# add =  lambda a,b: a + b
# mul = lambda a,b: a * b
#
# print(add(10,20))
# print(mul(10,20))

# recurssion basically is the function which is self called. less complexity. reusable and repititive task as loop.
# the difference in recurrsion is that it can be reused if the function is called.
# function recurrsion if return value is undefined if function is called
# will get error of out of bound or RecursionError: maximum recursion depth exceeded

# def factor(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factor(n-1)
# num = int(input("Enter the number of which factor is required:"))
# fact = factor(num)
# print(fact)

def fibonnaci(n):
    try:
        if n<0:
            return("Enter a positive number")
        else:
            return(fibonnaci(n)+fibonnaci(n-1))
    except Exception as e:
            return(e)
num = int(input("Enter the number of which fibbonaci series is required:"))
result = fibonnaci(num)
print(result)
