#!/usr/bin/env python
# coding: utf-8
# Question 1:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated
sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
# In[1]:


import math

def calculate_values(input_sequence):
    C = 50
    H = 30
    values = []

    # Split the input sequence by commas
    numbers = input_sequence.split(',')

    for number in numbers:
        D = int(number)
        Q = int(math.sqrt((2 * C * D) / H))
        values.append(Q)

    return values

# Example usage
input_sequence = "100,150,180"

result = calculate_values(input_sequence)
print(f"The output of the program: {','.join(str(value) for value in result)}")

# Question 2:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# In[2]:


def generate_2d_array(x, y):
    array = []

    for i in range(x):
        row = []
        for j in range(y):
            row.append(i * j)
        array.append(row)

    return array

# Example usage
x = 3
y = 5

result = generate_2d_array(x, y)
print(f"The output of the program: {result}")

# Question 3:
Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
# In[3]:


def sort_words(sequence):
    words = sequence.split(',')
    sorted_words = sorted(words)
    sorted_sequence = ','.join(sorted_words)
    return sorted_sequence

# Example usage
input_sequence = "without,hello,bag,world"

sorted_sequence = sort_words(input_sequence)
print(f"The output of the program: {sorted_sequence}")

# Question 4:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
# In[4]:


def remove_duplicates_and_sort(sequence):
    words = sequence.split()
    unique_words = sorted(set(words))
    sorted_sequence = ' '.join(unique_words)
    return sorted_sequence

# Example usage
input_sequence = "hello world and practice makes perfect and hello world again"

result = remove_duplicates_and_sort(input_sequence)
print(f"The output of the program: {result}")

# Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
# In[5]:


def count_letters_digits(sentence):
    letter_count = 0
    digit_count = 0

    for char in sentence:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1

    return letter_count, digit_count

# Example usage
input_sentence = "hello world! 123"

letters, digits = count_letters_digits(input_sentence)
print("LETTERS", letters)
print("DIGITS", digits)

# Question 6:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
# In[6]:


import re

def check_password_validity(passwords):
    valid_passwords = []

    for password in passwords:
        if (
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password) and
            re.search(r'[A-Z]', password) and
            re.search(r'[$#@]', password) and
            len(password) >= 6 and
            len(password) <= 12
        ):
            valid_passwords.append(password)

    return valid_passwords

# Example usage
passwords = "ABd1234@1,aF1#,2w3E*,2We3345"

password_list = passwords.split(',')
valid_passwords = check_password_validity(password_list)
valid_passwords_str = ', '.join(valid_passwords)
print(f"The output of the program: {valid_passwords_str}")

