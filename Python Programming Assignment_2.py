#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to convert kilometers to miles?

def convert_kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

# Example usage
kilometers = float(input("Enter the distance in kilometers: "))

miles = convert_kilometers_to_miles(kilometers)
print("The distance in miles is:", miles)


# In[2]:


# 2. Write a Python program to convert Celsius to Fahrenheit?

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = convert_celsius_to_fahrenheit(celsius)
print("The temperature in Fahrenheit is:", fahrenheit)


# In[3]:


# 3. Write a Python program to display calendar?

import calendar

# Example usage
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar
print(calendar.month(year, month))


# In[4]:


# 4. Write a Python program to solve quadratic equation?

import cmath

def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant
    discriminant = (b**2) - (4*a*c)

    # Calculate the solutions
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    return root1, root2

# Example usage
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

roots = solve_quadratic_equation(a, b, c)
print("The solutions are:", roots)


# In[5]:


# 5. Write a Python program to swap two variables without temp variable?

def swap_variables(a, b):
    a, b = b, a
    return a, b

# Example usage
var1 = input("Enter the first variable: ")
var2 = input("Enter the second variable: ")

print("Before swapping: var1 =", var1, "and var2 =", var2)

var1, var2 = swap_variables(var1, var2)

print("After swapping: var1 =", var1, "and var2 =", var2)

