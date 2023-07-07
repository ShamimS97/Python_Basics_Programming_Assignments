#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python Program to Find LCM?

def calculate_lcm(num1, num2):
    # Find the maximum of the two numbers
    max_num = max(num1, num2)

    # Initialize the LCM
    lcm = max_num

    while True:
        # Check if lcm is divisible by both numbers
        if lcm % num1 == 0 and lcm % num2 == 0:
            break
        lcm += max_num  # Increment lcm by the maximum number

    return lcm

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and print the LCM
lcm = calculate_lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is", lcm)


# In[2]:


# 2. Write a Python Program to Find HCF?

def calculate_hcf(num1, num2):
    # Find the minimum of the two numbers
    min_num = min(num1, num2)

    # Initialize the HCF
    hcf = 1

    for i in range(1, min_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i

    return hcf

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and print the HCF
hcf = calculate_hcf(num1, num2)
print("The HCF of", num1, "and", num2, "is", hcf)


# In[4]:


# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print("Binary: ", binary)
print("Octal: ", octal)
print("Hexadecimal: ", hexadecimal)


# In[6]:


# 4. Write a Python Program To Find ASCII value of a character?

character = input("Enter a character: ")

ascii_value = ord(character)

print("The ASCII value of", character, "is", ascii_value)


# In[7]:


# 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = 0

if choice == 1:
    result = add(num1, num2)
    operation = "+"
elif choice == 2:
    result = subtract(num1, num2)
    operation = "-"
elif choice == 3:
    result = multiply(num1, num2)
    operation = "*"
elif choice == 4:
    result = divide(num1, num2)
    operation = "/"

if isinstance(result, float):
    print(num1, operation, num2, "=", round(result, 2))
else:
    print(result)

