#!/usr/bin/env python
# coding: utf-8
Question1
Create a function that takes three parameters where:
 x is the start of the range (inclusive).
 y is the end of the range (inclusive).
 n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n.
Return an empty list if there are no numbers that are divisible by n.
Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]
list_operation(7, 9, 2) ➞ [8]
list_operation(15, 20, 7) ➞ []
# In[1]:


def list_operation(x, y, n):
    return [num for num in range(x, y+1) if num % n == 0]

# Example usage:
print(list_operation(1, 10, 3))  # Output: [3, 6, 9]
print(list_operation(7, 9, 2))  # Output: [8]
print(list_operation(15, 20, 7))  # Output: []

Question2
Create a function that takes in two lists and returns True if the second list follows the first list
by one element, and False otherwise. In other words, determine if the second list is the first
list shifted to the right by 1.
Examples
simon_says([1, 2], [5, 1]) ➞ True
simon_says([1, 2], [5, 5]) ➞ False
simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
Notes
 Both input lists will be of the same length, and will have a minimum length of 2.
 The values of the 0-indexed element in the second list and the n-1th indexed element
in the first list do not matter.
# In[2]:


def simon_says(lst1, lst2):
    return lst1[:-1] == lst2[1:]

# Example usage:
print(simon_says([1, 2], [5, 1]))  # Output: True
print(simon_says([1, 2], [5, 5]))  # Output: False
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))  # Output: True
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))  # Output: False

Question3
A group of friends have decided to start a secret society. The name will be the first letter of
each of their names, sorted in alphabetical order.
Create a function that takes in a list of names and returns the name of the secret society.
# In[3]:


def society_name(names):
    initials = [name[0] for name in names]
    return ''.join(sorted(initials))

# Example usage:
print(society_name(["Adam", "Sarah", "Malcolm"]))  # Output: "AMS"
print(society_name(["Harry", "Newt", "Luna", "Cho"]))  # Output: "CHLN"
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))  # Output: "CJMPRR"

Question4
An isogram is a word that has no duplicate letters. Create a function that takes a string and
returns either True or False depending on whether or not it's an 'isogram'.
# In[4]:


def is_isogram(string):
    lowercase_string = string.lower()
    return len(lowercase_string) == len(set(lowercase_string))

# Example usage:
print(is_isogram("Algorism"))  # Output: True
print(is_isogram("PasSword"))  # Output: False
print(is_isogram("Consecutive"))  # Output: False

Question5
Create a function that takes a string and returns True or False, depending on whether the
characters are in order or not.
# In[5]:


def is_in_order(string):
    return string == ''.join(sorted(string))

# Example usage:
print(is_in_order("abc"))  # Output: True
print(is_in_order("edabit"))  # Output: False
print(is_in_order("123"))  # Output: True
print(is_in_order("xyzz"))  # Output: True

