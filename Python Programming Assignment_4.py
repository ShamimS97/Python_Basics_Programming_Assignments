#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python Program to Find the Factorial of a Number?

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))

result = factorial(num)
print("The factorial of", num, "is:", result)


# In[2]:


# 2. Write a Python Program to Display the multiplication Table?

def display_multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

# Example usage
num = int(input("Enter a number: "))

print("Multiplication table for", num)
display_multiplication_table(num)


# In[3]:


# 3. Write a Python Program to Print the Fibonacci sequence?

def fibonacci_sequence(n):
    sequence = []
    if n <= 0:
        return sequence
    elif n == 1:
        sequence.append(0)
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
    return sequence

# Example usage
num = int(input("Enter the number of terms in the Fibonacci sequence: "))

fib_sequence = fibonacci_sequence(num)
print("The Fibonacci sequence:")
for num in fib_sequence:
    print(num, end=" ")


# In[4]:


# 4. Write a Python Program to Check Armstrong Number?

def check_armstrong_number(num):
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        return True
    else:
        return False

# Example usage
num = int(input("Enter a number: "))

if check_armstrong_number(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# In[5]:


# 5. Write a Python Program to Find Armstrong Number in an Interval?

def find_armstrong_numbers(start, end):
    armstrong_numbers = []

    for num in range(start, end + 1):
        order = len(str(num))
        sum = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            armstrong_numbers.append(num)

    return armstrong_numbers

# Example usage
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

result = find_armstrong_numbers(start, end)
print("Armstrong numbers in the interval", start, "to", end, "are:")
for num in result:
    print(num)


# In[6]:


# 6. Write a Python Program to Find the Sum of Natural Numbers?

def find_sum_of_natural_numbers(n):
    if n < 1:
        return "Invalid input. Please enter a positive integer."
    
    sum = 0
    for num in range(1, n+1):
        sum += num

    return sum

# Example usage
num = int(input("Enter a positive integer: "))

result = find_sum_of_natural_numbers(num)
print("The sum of natural numbers up to", num, "is:", result)

