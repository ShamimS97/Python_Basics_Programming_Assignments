#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python Program to Add Two Matrices?

def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: Matrices have different dimensions.")
        return None

    # Create an empty result matrix with the same dimensions as the input matrices
    rows = len(matrix1)
    columns = len(matrix1[0])
    result = [[0] * columns for _ in range(rows)]

    # Perform element-wise addition
    for i in range(rows):
        for j in range(columns):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

# Test the program
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result = add_matrices(matrix1, matrix2)

if result is not None:
    print("The sum of the matrices is:")
    for row in result:
        print(row)


# In[2]:


# 2. Write a Python Program to Multiply Two Matrices?

def multiply_matrices(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        print("Error: Matrices cannot be multiplied.")
        return None

    # Create an empty result matrix with appropriate dimensions
    rows = len(matrix1)
    columns = len(matrix2[0])
    result = [[0] * columns for _ in range(rows)]

    # Perform matrix multiplication
    for i in range(rows):
        for j in range(columns):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Test the program
matrix1 = [[1, 2],
           [3, 4]]

matrix2 = [[5, 6],
           [7, 8]]

result = multiply_matrices(matrix1, matrix2)

if result is not None:
    print("The product of the matrices is:")
    for row in result:
        print(row)


# In[3]:


# 3. Write a Python Program to Transpose a Matrix?

def transpose_matrix(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    columns = len(matrix[0])

    # Create an empty result matrix with swapped dimensions
    result = [[0] * rows for _ in range(columns)]

    # Perform matrix transposition
    for i in range(rows):
        for j in range(columns):
            result[j][i] = matrix[i][j]

    return result

# Test the program
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = transpose_matrix(matrix)

print("The transposed matrix is:")
for row in result:
    print(row)


# In[4]:


# 4. Write a Python Program to Sort Words in Alphabetic Order?

def sort_words(words):
    sorted_words = sorted(words)
    return sorted_words

# Test the program
input_string = input("Enter a sentence: ")

# Split the input string into individual words
words = input_string.split()

# Call the sort_words() function to sort the words
sorted_words = sort_words(words)

print("The words in alphabetical order are:")
for word in sorted_words:
    print(word)


# In[6]:


# 5. Write a Python Program to Remove Punctuation From a String?

import string

def remove_punctuation(input_string):
    # Create a translation table using string.punctuation
    translator = str.maketrans("", "", string.punctuation)
    
    # Remove punctuation using the translation table
    processed_string = input_string.translate(translator)
    
    return processed_string

# Test the program
input_string = input("Enter a string: ")

processed_string = remove_punctuation(input_string)

print("String without punctuation:", processed_string)

