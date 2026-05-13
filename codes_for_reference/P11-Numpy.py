# 1. Numpy is nothing but a library widely used for mathemetical operations like algebra, matrix, statistics , probablity etc.
# 2. Less memory occupied
# 3. only similar data type to be used.
# 4. Inbuilt functions as append, array,etc.
# 5. it support multi dimensioned array operations.

# import numpy as np - This is to import or inherit the numpy library file which has inbuilt functions which can be used further in coding
# if you want version then write the version besides the numpy name in file
# numpy is used to do the function or operations in a easy way and with less memory usage. bcz if we run using loops and other operators it will take alot time and memory to calulate manually
# if tehre is no repetitive value in array then it will take the minimum vaue from array
import numpy as np
import statistics as stat
age =np.array([10,15,20,24,30,30])
n = np.mean(age)
print (n)

o = np.median(age)
print (o)

p = stat.mode(age)
print (p)

q= np.std(age)
print(q)

r= np.var(age)
print(r)