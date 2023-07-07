#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage
num = float(input("Enter a number: "))

result = check_number(num)
print("The number is", result)


# In[2]:


# 2. Write a Python Program to Check if a Number is Odd or Even?

def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
num = int(input("Enter a number: "))

result = check_odd_even(num)
print("The number is", result)


# In[3]:


# 3. Write a Python Program to Check Leap Year?

def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap Year"
            else:
                return "Not a Leap Year"
        else:
            return "Leap Year"
    else:
        return "Not a Leap Year"

# Example usage
year = int(input("Enter a year: "))

result = check_leap_year(year)
print("The year is", result)


# In[4]:


# 4. Write a Python Program to Check Prime Number?

def check_prime_number(num):
    if num <= 1:
        return "Not a Prime Number"
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not a Prime Number"
    
    return "Prime Number"

# Example usage
num = int(input("Enter a number: "))

result = check_prime_number(num)
print("The number is", result)


# In[5]:


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

def check_prime_number(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

# Example usage
lower_limit = 1
upper_limit = 10000

print("Prime numbers in the interval of", lower_limit, "to", upper_limit, "are:")

for num in range(lower_limit, upper_limit + 1):
    if check_prime_number(num):
        print(num)


# In[ ]:




