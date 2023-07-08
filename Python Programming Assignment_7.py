#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. Write a Python Program to find sum of array?

def sum_of_array(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

# Test the program
array = [int(x) for x in input("Enter the array elements (space-separated): ").split()]
result = sum_of_array(array)
print("The sum of the array is:", result)


# In[3]:


# 2. Write a Python Program to find largest element in an array?

def find_largest_element(arr):
    if len(arr) == 0:
        return None

    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Test the program
array = [int(x) for x in input("Enter the array elements (space-separated): ").split()]
result = find_largest_element(array)

if result is None:
    print("The array is empty.")
else:
    print("The largest element in the array is:", result)


# In[6]:


# 3. Write a Python Program for array rotation?

def rotate_array(arr, k):
    n = len(arr)
    # Normalize the rotation factor to handle large values of k
    k = k % n

    rotated_arr = arr[k:] + arr[:k]
    return rotated_arr

# Test the program
array = [int(x) for x in input("Enter the array elements (space-separated): ").split()]
rotation_factor = int(input("Enter the rotation factor: "))

rotated_array = rotate_array(array, rotation_factor)
print("The rotated array is:", rotated_array)


# In[7]:


# 4. Write a Python Program to Split the array and add the first part to the end?

def split_and_add(arr, k):
    n = len(arr)

    # Validate the split position
    if k < 0 or k >= n:
        return arr

    # Split the array into two parts
    first_part = arr[:k]
    second_part = arr[k:]

    # Add the first part to the end
    rotated_arr = second_part + first_part
    return rotated_arr

# Test the program
array = [int(x) for x in input("Enter the array elements (space-separated): ").split()]
split_position = int(input("Enter the split position: "))

rotated_array = split_and_add(array, split_position)
print("The modified array is:", rotated_array)


# In[10]:


# 5. Write a Python Program to check if given array is Monotonic?

def is_monotonic(arr):
    n = len(arr)

    if n <= 2:
        return True

    # Determine the direction of the array (increasing or decreasing)
    direction = 0
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            if direction == 0:
                direction = 1
            elif direction == -1:
                return False
        elif arr[i] < arr[i - 1]:
            if direction == 0:
                direction = -1
            elif direction == 1:
                return False

    return True

# Test the program
array = [int(x) for x in input("Enter the array elements (space-separated): ").split()]

if is_monotonic(array):
    print("The array is monotonic.")
else:
    print("The array is not monotonic.")

