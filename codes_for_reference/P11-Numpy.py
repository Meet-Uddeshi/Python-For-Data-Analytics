# 1. Numpy is nothing but a library widely used for mathemetical operations like algebra, matrix, statistics , probablity etc.
# 2. Less memory occupied
# 3. only similar data type to be used.
# 4. Inbuilt functions as append, array,etc.
# 5. it support multi dimensioned array operations.

# import numpy as np - This is to import or inherit the numpy library file which has inbuilt functions which can be used further in coding
# if you want version then write the version besides the numpy name in file
# numpy is used to do the function or operations in a easy way and with less memory usage. bcz if we run using loops and other operators it will take alot time and memory to calulate manually
# if tehre is no repetitive value in array then it will take the minimum vaue from array
# noise/outlier - datapoint  which makes your data uneven.
# mean /median/mode - it is used to fill in the missing data in the database.if we have any in the database.
#


import numpy as np
import statistics as stat
# age =np.array([10,15,20,24,30,30])
# n = np.mean(age)
# print (n)
#
# o = np.median(age)
# print (o)
#
# p = stat.mode(age)
# print (p)
#
# q= np.std(age)
# print(q)
#
# r= np.var(age)
# print(r)

# always use() for functions.
# below is the example of the matrix multipication in which 1 row is defined in one [] followed by , so on.
#  using numpy.dot we can calclulate or use operator to perfom. which is same as we did it in mannual matrix calculations
# using the for and while loop
# OperationNumPy ExpressionDescriptionAdditionA + B or np.add(A, B) Element-wise addition of two matrices.
# SubtractionA - B or np.subtract(A, B)Element-wise subtraction.
# Multiplication (Matrix)A @ B or np.matmul(A, B)Standard dot product matrix multiplication.Multiplication (Element-wise)A * B or np.multiply(A, B)Multiplies corresponding elements (Hadamard product).
# TransposeA.T or A.transpose()Flips the matrix over its diagonal.
# Inversenp.linalg.inv(A)Computes the multiplicative inverse of a square matrix.
# # differencebetween array and list is that it varies as the memory used will be different.
# a = [[1,2,4],
#       [5,6,7],
#       [8,9,10]]
# b = [[2,4,6],
#      [3,6,9],
#      [5,10,15]]
# z = np.array(a)
# q= np.array(b)
# mult = np.dot(z,q)
# addition = np.add(z,q)
# sub = np.subtract(z,q)
# t = np.transpose(z)
# u = np.transpose(q)
# inv = np.linalg.inv(z)
# print(mult)
# print(addition)
# print(sub)
# print(t,"\n",u)
# print(z)
# print(inv)

# Quartile - is the data whoch is divided in 25% intervals.
# Decile - is the data whoch is divided in 10% intervals.
# Percentile - is the data whoch is divided in 1% intervals.
# Percentile Formula: p100 = 100/100(n+1)
# Decile Fromula: p10 = 10/100(n+1)
# Quartile Formula: p25 = 25/100(n+1)

# uses in real life:
# Quartiles: Used in box-and-whisker plots to show the spread, median, and skewness of data.
# Deciles: Used in finance and economic studies to analyze income distribution or performance brackets.
# Percentiles: Used in standardized testing (e.g., scoring at the 90th percentile) to compare scores relative to the whole group.

abc = [13, 21, 21, 40, 42, 48, 55, 72]
x = np.array(abc)
print(np.percentile(x, 25))
print(np.decile(x, 10))
print(np.quantile(x, 0.25))


