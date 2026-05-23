# Topic: Numpy library
# NumPy is a Python library used for mathematical and numerical operations.NumPy arrays consume less memory compared to Python lists. It is used for scientific computing, data analysis, machine learning, and more. It provides a multidimensional array object and various functions for array manipulation and mathematical operations.

# Features:-
# 1. Mathematical functions - performs mathematical operations on arrays.
# 2. Multidimensional arrays - supports arrays of any dimension.
# 3. Broadcasting - performs operations on arrays of different shapes.
# 4. Random number generation - generates random numbers for simulations and models.
# 5. Linear algebra - provides functions for linear algebra operations.

# Measure of tendency:

# Mean   -> Average value
# Median -> Middle value
# Mode   -> Most repeated value
# Standard Deviation -> Square root of variance
# Variance -> Average of squared differences from the mean
# Quartile -> Divides data into 4 equal parts (25% intervals)
# Decile -> Divides data into 10 equal parts (10% intervals)
# Percentile -> Divides data into 100 equal parts (1% intervals)

# Real-life applications:
# - Quartiles  -> Box plots and data spread analysis
# - Deciles    -> Finance and income distribution
# - Percentiles-> Exam rankings and performance comparison


# Example:
import numpy as np
import statistics as stat

age = np.array([10, 15, 20, 24, 30, 30])
abc = [13, 21, 21, 40, 42, 48, 55, 72]

mean_value = np.mean(age)
print("Mean:", mean_value)

median_value = np.median(age)
print("Median:", median_value)

mode_value = stat.mode(age)
print("Mode:", mode_value)

std_value = np.std(age)
print("Standard Deviation:", std_value)

var_value = np.var(age)
print("Variance:", var_value)

x = np.array(abc)

# 25th Percentile (Q1)
print("\n25th Percentile:", np.percentile(x, 25))

# 10th Percentile
print("10th Percentile:", np.percentile(x, 10))

#  Example

# Matrix Operations:
# Common matrix operations:
# Addition              -> np.add(A, B)
# Subtraction           -> np.subtract(A, B)
# Matrix Multiplication -> np.dot(A, B) or @ operator
# Element-wise Multiply -> np.multiply(A, B)
# Transpose             -> np.transpose(A) or A.T
# Inverse               -> np.linalg.inv(A)

a = [[1, 2, 4],
     [5, 6, 7],
     [8, 9, 10]]

b = [[2, 4, 6],
     [3, 6, 9],
     [5, 10, 15]]

A = np.array(a)
B = np.array(b)

multiplication = np.dot(A, B)
addition = np.add(A, B)
subtraction = np.subtract(A, B)

transpose_A = np.transpose(A)
transpose_B = np.transpose(B)

inverse_A = np.linalg.inv(A)

print("\nMatrix Multiplication:\n", multiplication)
print("\nMatrix Addition:\n", addition)
print("\nMatrix Subtraction:\n", subtraction)
print("\nTranspose of A:\n", transpose_A)
print("\nTranspose of B:\n", transpose_B)
print("\nInverse of A:\n", inverse_A)
