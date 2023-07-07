#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to print "Hello Python" ?

print("Hello Python")


# In[4]:


# 2. Write a Python program to do arithmetical operations addition and division.?

a = int(input("Select First Number = "))
b = int(input("Select Second Number = "))

print("Additon of given no. is", a+b)
print("Division of given no. is", a/b)


# In[5]:


# 3. Write a Python program to find the area of a triangle?

def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

# Example usage
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

triangle_area = calculate_triangle_area(base, height)
print("The area of the triangle is:", triangle_area)


# In[6]:


# 4. Write a Python program to swap two variables?

def swap_variables(a, b):
    # Temporary variable to hold the value of 'a'
    temp = a
    # Swapping the values
    a = b
    b = temp
    return a, b

# Example usage
var1 = input("Enter the first variable: ")
var2 = input("Enter the second variable: ")

print("Before swapping: var1 =", var1, "and var2 =", var2)

var1, var2 = swap_variables(var1, var2)

print("After swapping: var1 =", var1, "and var2 =", var2)


# In[7]:


# 5. Write a Python program to generate a random number?

import random

def generate_random_number(start, end):
    random_number = random.randint(start, end)
    return random_number

# Example usage
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

random_number = generate_random_number(start_range, end_range)
print("Random number between", start_range, "and", end_range, "is:", random_number)

