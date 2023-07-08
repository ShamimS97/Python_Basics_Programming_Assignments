#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to check if the given number is a Disarium Number?

def is_disarium_number(number):
    # Convert the number to string to iterate over its digits
    number_str = str(number)
    n = len(number_str)

    # Calculate the sum of the digits raised to their respective positions
    digit_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(number_str))

    # Check if the sum is equal to the original number
    return digit_sum == number

# Test the program
number = int(input("Enter a number: "))

if is_disarium_number(number):
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")


# In[2]:


# 2. Write a Python program to print all disarium numbers between 1 to 100?

def is_disarium_number(number):
    # Convert the number to string to iterate over its digits
    number_str = str(number)
    n = len(number_str)

    # Calculate the sum of the digits raised to their respective positions
    digit_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(number_str))

    # Check if the sum is equal to the original number
    return digit_sum == number

# Find and print Disarium numbers between 1 and 100
print("Disarium numbers between 1 and 100:")
for i in range(1, 101):
    if is_disarium_number(i):
        print(i)


# In[3]:


# 3. Write a Python program to check if the given number is Happy Number?

def is_happy_number(number):
    seen = set()

    while number != 1:
        number = sum(int(digit) ** 2 for digit in str(number))
        if number in seen:
            return False
        seen.add(number)

    return True

# Test the program
number = int(input("Enter a number: "))

if is_happy_number(number):
    print(f"{number} is a Happy number.")
else:
    print(f"{number} is not a Happy number.")


# In[4]:


# 4. Write a Python program to print all happy numbers between 1 and 100?

def is_happy_number(number):
    seen = set()

    while number != 1:
        number = sum(int(digit) ** 2 for digit in str(number))
        if number in seen:
            return False
        seen.add(number)

    return True

# Find and print Happy numbers between 1 and 100
print("Happy numbers between 1 and 100:")
for i in range(1, 101):
    if is_happy_number(i):
        print(i)


# In[5]:


# 5. Write a Python program to determine whether the given number is a Harshad Number?

def is_harshad_number(number):
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in str(number))

    # Check if the number is divisible by the sum of its digits
    return number % digit_sum == 0

# Test the program
number = int(input("Enter a number: "))

if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")


# In[6]:


# 6. Write a Python program to print all pronic numbers between 1 and 100?

def is_pronic_number(number):
    # Find the square root of the number
    root = int(number ** 0.5)

    # Check if the product of consecutive numbers is equal to the given number
    return root * (root + 1) == number

# Find and print pronic numbers between 1 and 100
print("Pronic numbers between 1 and 100:")
for i in range(1, 101):
    if is_pronic_number(i):
        print(i)

