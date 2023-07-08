#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def display_fibonacci_sequence(limit):
    if limit <= 0:
        print("Invalid input. Limit must be a positive integer.")
        return

    print("Fibonacci sequence:")
    for i in range(limit):
        print(fibonacci(i))

# Test the program
limit = int(input("Enter the limit: "))
display_fibonacci_sequence(limit)


# In[2]:


# 2. Write a Python Program to Find Factorial of Number Using Recursion?

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the program
number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1.")
else:
    result = factorial(number)
    print(f"Factorial of {number} is {result}.")


# In[3]:


# 3. Write a Python Program to calculate your Body Mass Index?

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Test the program
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print("Your Body Mass Index (BMI) is:", round(bmi, 2))


# In[4]:


# 4. Write a Python Program to calculate the natural logarithm of any number?

import math

number = float(input("Enter a number: "))

if number <= 0:
    print("Error: Natural logarithm is only defined for positive numbers.")
else:
    result = math.log(number)
    print(f"The natural logarithm of {number} is {result}.")


# In[5]:


# 5. Write a Python Program for cube sum of first n natural numbers?

def cube_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** 3
    return sum

# Test the program
n = int(input("Enter the value of n: "))
result = cube_sum(n)
print(f"The cube sum of the first {n} natural numbers is {result}.")

