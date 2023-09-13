# Advanced Problem Set: Delving Deeper with Numbers in Python
#################### PROBLEM 1: Basic Arithmetic & Order of Operations ####################
# Task 1: Using the order of operations (PEMDAS/BODMAS), evaluate the following expression:
# 3 + 6 * (5 + 4) / 3 - 7. Print the result.
PEMDAS = 3 + 6 *(5+4)/ 3 - 7
print(PEMDAS)
# Task 2: Calculate the remainder when 145 is divided by 12 using modulo and print the result.
num1 = 145
num2 = 12
result = num1 / num2
print(result)
# Task 3: Raise 7 to the power of 3 and print the result.
a = 7
b = 3
result1 = a ** b
print(result1)
#################### PROBLEM 2: Working with Functions ####################
# Task 4: Given a list of numbers:
numbers = [23, 89, 12, 54, 92, 65, 71, 13, 45]
# Use the max() and min() functions to find the highest and lowest number respectively.
print(max(numbers))
print(min(numbers))
# Task 5: Round the number 12.5678 to 2 decimal places.
decimal = 12.5678
print(round(decimal,2))
# Task 6: Find the absolute value of -45.
value = -45
print(abs(value))
#################### PROBLEM 3: Advanced Math Functions ####################
# Task 7: Using the math library, find the floor value of 15.7.
import math
print(math.floor(15.7))
# Task 8: Find the ceiling value of 15.2.
print(math.ceil(15.2))
# Task 9: Calculate the square root of 625.
root = 625
print(math.sqrt(root))
#################### PROBLEM 4: Problem Solving ####################
# Task 10: You are given two lists:
prices = [34.56, 45.78, 23.89, 12.34, 78.90]
quantities = [3, 5, 2, 4, 6]
# Calculate the total cost for each item (price multiplied by quantity).
print(sum(prices))
print(sum(quantities))
print(sum(prices) * sum(quantities))
sumofitems = sum(prices)
print(sumofitems)
average = sumofitems/len(prices)
print(round(average, 2))
# Then, find the average cost of all items after rounding it to 2 decimal places.

#################### END OF ADVANCED PROBLEM SET ####################
