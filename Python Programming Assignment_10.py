#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to find sum of elements in list?

def sum_of_elements(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum

# Test the program
lst = [int(x) for x in input("Enter the list elements (space-separated): ").split()]
result = sum_of_elements(lst)
print("The sum of the elements in the list is:", result)


# In[2]:


# 2. Write a Python program to Multiply all numbers in the list?

def multiply_numbers(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Test the program
lst = [int(x) for x in input("Enter the list elements (space-separated): ").split()]
result = multiply_numbers(lst)
print("The product of the numbers in the list is:", result)


# In[3]:


# 3. Write a Python program to find smallest number in a list?

def find_smallest_number(lst):
    if len(lst) == 0:
        return None

    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

# Test the program
lst = [int(x) for x in input("Enter the list elements (space-separated): ").split()]
result = find_smallest_number(lst)

if result is None:
    print("The list is empty.")
else:
    print("The smallest number in the list is:", result)


# In[4]:


# 4. Write a Python program to find largest number in a list?

def find_largest_number(lst):
    if len(lst) == 0:
        return None

    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Test the program
lst = [int(x) for x in input("Enter the list elements (space-separated): ").split()]
result = find_largest_number(lst)

if result is None:
    print("The list is empty.")
else:
    print("The largest number in the list is:", result)


# In[5]:


# 5. Write a Python program to find second largest number in a list?

def find_second_largest_number(lst):
    if len(lst) < 2:
        return None

    largest = max(lst[0], lst[1])
    second_largest = min(lst[0], lst[1])

    for num in lst[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

    return second_largest

# Test the program
lst = [int(x) for x in input("Enter the list elements (space-separated): ").split()]
result = find_second_largest_number(lst)

if result is None:
    print("The list does not have a second largest number.")
else:
    print("The second largest number in the list is:", result)


# In[7]:


# 6. Write a Python program to find N largest elements from a list?

def find_n_largest_elements(lst, n):
    if len(lst) < n:
        return None

    largest_elements = sorted(lst, reverse=True)[:n]
    return largest_elements

# Test the program
lst = [int(x) for x in input("Enter the list elements (space-separated): ").split()]
n = int(input("Enter the value of N: "))

result = find_n_largest_elements(lst, n)

if result is None:
    print("The list does not have enough elements.")
else:
    print(f"The {n} largest elements in the list are:", result)


# In[8]:


# 7. Write a Python program to print even numbers in a list?

def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    for num in even_numbers:
        print(num)

# Test the program
lst = [int(x) for x in input("Enter the list elements (space-separated): ").split()]

print("Even numbers in the list:")
print_even_numbers(lst)


# In[9]:


# 8. Write a Python program to print odd numbers in a List?

def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    for num in odd_numbers:
        print(num)

# Test the program
lst = [int(x) for x in input("Enter the list elements (space-separated): ").split()]

print("Odd numbers in the list:")
print_odd_numbers(lst)


# In[13]:


# 9. Write a Python program to Remove empty List from List?

def remove_empty_lists(lst):
    result = [sublist for sublist in lst if sublist]
    return result

# Test the program
lst = eval(input("Enter a list containing sublists: "))

print("Original list:", lst)
result = remove_empty_lists(lst)
print("List after removing empty sublists:", result)


# In[14]:


# 10. Write a Python program to Cloning or Copying a list?

def clone_list(lst):
    # Method 1: Using the list() constructor
    cloned_list = list(lst)

    # Method 2: Using the list slice [:]
    # cloned_list = lst[:]

    return cloned_list

# Test the program
lst = [int(x) for x in input("Enter the list elements (space-separated): ").split()]

# Clone the list
cloned_list = clone_list(lst)

print("Original list:", lst)
print("Cloned list:", cloned_list)


# In[16]:


# 11. Write a Python program to Count occurrences of an element in a list?

def count_occurrences(lst, element):
    count = lst.count(element)
    return count

# Test the program
lst = [int(x) for x in input("Enter the list elements (space-separated): ").split()]
element = int(input("Enter the element to count: "))

occurrences = count_occurrences(lst, element)

print(f"The element {element} occurs {occurrences} time(s) in the list.")

