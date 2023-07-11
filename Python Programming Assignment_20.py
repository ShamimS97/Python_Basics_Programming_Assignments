#!/usr/bin/env python
# coding: utf-8
Question1
Create a function that takes a list of strings and integers, and filters out the list so that it
returns a list of integers only.
Examples
filter_list([1, 2, 3, 'a', 'b', 4]) ➞ [1, 2, 3, 4]
filter_list(['A', 0, 'Edabit', 1729, 'Python', '1729']) ➞ [0, 1729]
filter_list(['Nothing', 'here']) ➞ []
# In[1]:


def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]

# Example usage:
print(filter_list([1, 2, 3, 'a', 'b', 4]))  # Output: [1, 2, 3, 4]
print(filter_list(['A', 0, 'Edabit', 1729, 'Python', '1729']))  # Output: [0, 1729]
print(filter_list(['Nothing', 'here']))  # Output: []

Question2
Given a list of numbers, create a function which returns the list but with each element's
index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the
number at index 1, etc...
Examples
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
# In[2]:


def add_indexes(lst):
    return [i + num for i, num in enumerate(lst)]

# Example usage:
print(add_indexes([0, 0, 0, 0, 0]))  # Output: [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5]))  # Output: [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1]))  # Output: [5, 5, 5, 5, 5]

Question3
Create a function that takes the height and radius of a cone as arguments and returns the
volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.

Examples
cone_volume(3, 2) ➞ 12.57
cone_volume(15, 6) ➞ 565.49
cone_volume(18, 0) ➞ 0
# In[3]:


import math

def cone_volume(height, radius):
    volume = (1/3) * math.pi * radius**2 * height
    return round(volume, 2)

# Example usage:
print(cone_volume(3, 2))  # Output: 12.57
print(cone_volume(15, 6))  # Output: 565.49
print(cone_volume(18, 0))  # Output: 0

Question4
This Triangular Number Sequence is generated from a pattern of dots that form a triangle.
The first 5 numbers of the sequence, or dots, are:
1, 3, 6, 10, 15
This means that the first triangle has just one dot, the second one has three dots, the third one
has 6 dots and so on.
Write a function that gives the number of dots with its corresponding triangle number of the
sequence.
Examples
triangle(1) ➞ 1
triangle(6) ➞ 21
triangle(215) ➞ 23220
# In[4]:


def triangle(n):
    return (n * (n + 1)) // 2

# Example usage:
print(triangle(1))  # Output: 1
print(triangle(6))  # Output: 21
print(triangle(215))  # Output: 23220

Question5
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
returns the missing number.
Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
# In[5]:


def missing_num(nums):
    full_set = set(range(1, 11))
    given_set = set(nums)
    missing = full_set - given_set
    return missing.pop()

# Example usage:
print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))  # Output: 5
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))  # Output: 10
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))  # Output: 7

