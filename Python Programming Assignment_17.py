#!/usr/bin/env python
# coding: utf-8
Question1. Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
# In[1]:


def evenly_divisible(a, b, c):
    total_sum = 0
    for num in range(a, b+1):
        if num % c == 0:
            total_sum += num
    return total_sum

# Example usage
print(evenly_divisible(1, 10, 20))  # Output: 0
print(evenly_divisible(1, 10, 2))   # Output: 30
print(evenly_divisible(1, 10, 3))   # Output: 18

Question2. Create a function that returns True if a given inequality expression is correct and
False otherwise.
Examples
correct_signs('3 < 7 < 11') ➞ True
correct_signs('13 > 44 > 33 > 1') ➞ False
correct_signs('1 < 2 < 6 < 9 > 3') ➞ True
# In[2]:


def correct_signs(expression):
    return eval(expression)

# Example usage
print(correct_signs('3 < 7 < 11'))              # Output: True
print(correct_signs('13 > 44 > 33 > 1'))         # Output: False
print(correct_signs('1 < 2 < 6 < 9 > 3'))        # Output: True

Question3. Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels('the aardvark', '#') ➞ 'th# ##rdv#rk'
replace_vowels('minnie mouse', '?') ➞ 'm?nn?? m??s?'
replace_vowels('shakespeare', '*') ➞ 'sh*k*sp**r*'
# In[3]:


def replace_vowels(string, char):
    vowels = 'aeiouAEIOU'
    replaced_string = ''
    for ch in string:
        if ch in vowels:
            replaced_string += char
        else:
            replaced_string += ch
    return replaced_string

# Example usage
print(replace_vowels('the aardvark', '#'))    # Output: 'th# ##rdv#rk'
print(replace_vowels('minnie mouse', '?'))    # Output: 'm?nn?? m??s?'
print(replace_vowels('shakespeare', '*'))     # Output: 'sh*k*sp**r*'

Question4. Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1
# In[4]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))   # Output: 120
print(factorial(3))   # Output: 6
print(factorial(1))   # Output: 1
print(factorial(0))   # Output: 1

Question 5
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: 'abcbba'
String2: 'abcbda'
Hamming Distance: 1 - 'b' vs. 'd' is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance('abcde', 'bcdef') ➞ 5
hamming_distance('abcde', 'abcde') ➞ 0
hamming_distance('strong', 'strung') ➞ 1
# In[5]:


def hamming_distance(str1, str2):
    distance = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            distance += 1
    return distance

# Example usage
print(hamming_distance('abcde', 'bcdef'))   # Output: 5
print(hamming_distance('abcde', 'abcde'))   # Output: 0
print(hamming_distance('strong', 'strung')) # Output: 1

