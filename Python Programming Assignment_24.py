#!/usr/bin/env python
# coding: utf-8
Question1
Create a function that takes an integer and returns a list from 1 to the given number, where:
1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
2. If the number cannot be divided evenly by 4, simply return the number.
# In[1]:


def amplify(num):
    return [n * 10 if n % 4 == 0 else n for n in range(1, num + 1)]

# Example usage:
print(amplify(4))  # Output: [1, 2, 3, 40]
print(amplify(3))  # Output: [1, 2, 3]
print(amplify(25))  # Output: [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]

Question2
Create a function that takes a list of numbers and return the number that's unique.
Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7
unique([0, 0, 0.77, 0, 0]) ➞ 0.77
unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0
Notes
Test cases will always have exactly one unique number while all others are the same.
# In[2]:


def unique(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num

# Example usage:
print(unique([3, 3, 3, 7, 3, 3]))  # Output: 7
print(unique([0, 0, 0.77, 0, 0]))  # Output: 0.77
print(unique([0, 1, 1, 1, 1, 1, 1, 1]))  # Output: 0

Question3
Your task is to create a Circle constructor that creates a circle with a radius provided by an
argument. The circles constructed must have two getters getArea() (PIr^2) and
getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).

For help with this class, I have provided you with a Rectangle constructor which you can use
as a base example.
# In[3]:


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        area = math.pi * (self.radius ** 2)
        return round(area)
    
    def getPerimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter)

# Example usage:
circy = Circle(11)
print(circy.getArea())  # Output: 380
circy = Circle(4.44)
print(circy.getPerimeter())  # Output: 28

Question4
Create a function that takes a list of strings and return a list, sorted from shortest to longest.
# In[4]:


def sort_by_length(strings):
    return sorted(strings, key=len)

# Example usage:
print(sort_by_length(["Google", "Apple", "Microsoft"]))  # Output: ["Apple", "Google", "Microsoft"]
print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))  # Output: ["Raphael", "Leonardo", "Donatello", "Michelangelo"]
print(sort_by_length(["Turing", "Einstein", "Jung"]))  # Output: ["Jung", "Turing", "Einstein"]

Question5
Create a function that validates whether three given integers form a Pythagorean triplet. The
sum of the squares of the two smallest integers must equal the square of the largest number to
be validated.

Examples
is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25
is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169
is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9
Notes
Numbers may not be given in a sorted order.
# In[5]:


def is_triplet(a, b, c):
    numbers = [a, b, c]
    numbers.sort()  # Sort the numbers in ascending order

    # Check if the condition for a Pythagorean triplet is satisfied
    return numbers[0] ** 2 + numbers[1] ** 2 == numbers[2] ** 2

# Example usage:
print(is_triplet(3, 4, 5))  # Output: True
print(is_triplet(13, 5, 12))  # Output: True
print(is_triplet(1, 2, 3))  # Output: False

