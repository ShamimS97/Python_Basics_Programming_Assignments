#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to find words which are greater than given length k?

def find_long_words(sentence, k):
    words = sentence.split()
    long_words = []
    
    for word in words:
        if len(word) > k:
            long_words.append(word)
    
    return long_words

# Example usage
sentence = "This is a sample sentence to demonstrate the program."
k = 5

long_words = find_long_words(sentence, k)
print(f"Words longer than {k} characters: {long_words}")


# In[2]:


# 2. Write a Python program for removing i-th character from a string?

def remove_character(string, i):
    if i < 0 or i >= len(string):
        return string
    
    return string[:i] + string[i+1:]

# Example usage
string = "Hello, World!"
i = 7

new_string = remove_character(string, i)
print(f"String with character at index {i} removed: {new_string}")


# In[3]:


# 3. Write a Python program to split and join a string?

def split_and_join(string, delimiter):
    # Split the string into a list of substrings
    words = string.split(delimiter)
    
    # Join the substrings using a specified delimiter
    new_string = delimiter.join(words)
    
    return new_string

# Example usage
string = "Hello, World!"
delimiter = ", "

# Split the string by delimiter
split_words = string.split(delimiter)
print(f"Split words: {split_words}")

# Join the split words using a different delimiter
new_string = delimiter.join(split_words)
print(f"Joined string: {new_string}")


# In[4]:


# 4. Write a Python to check if a given string is binary string or not?

def is_binary_string(string):
    for char in string:
        if char != '0' and char != '1':
            return False
    return True

# Example usage
string1 = "101010"
string2 = "12345"

print(f"{string1} is binary: {is_binary_string(string1)}")
print(f"{string2} is binary: {is_binary_string(string2)}")


# In[5]:


# 5. Write a Python program to find uncommon words from two Strings?

def find_uncommon_words(string1, string2):
    words1 = string1.split()
    words2 = string2.split()
    
    uncommon_words = []
    
    # Find uncommon words in string1
    for word in words1:
        if word not in words2:
            uncommon_words.append(word)
    
    # Find uncommon words in string2
    for word in words2:
        if word not in words1:
            uncommon_words.append(word)
    
    return uncommon_words

# Example usage
string1 = "Hello world! This is a sample string."
string2 = "This is another string."

uncommon = find_uncommon_words(string1, string2)
print(f"Uncommon words: {uncommon}")


# In[6]:


# 6. Write a Python to find all duplicate characters in string?

def find_duplicate_characters(string):
    duplicates = []
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)

    return duplicates

# Example usage
string = "Hello, World!"

duplicate_chars = find_duplicate_characters(string)
print(f"Duplicate characters: {duplicate_chars}")


# In[7]:


# 7. Write a Python Program to check if a string contains any special character?

import re

def contains_special_characters(string):
    # Regular expression pattern to match special characters
    pattern = r'[!@#$%^&*(),.?":{}|<>]'

    # Search for special characters in the string
    match = re.search(pattern, string)

    return match is not None

# Example usage
string1 = "Hello, World!"
string2 = "Hello@World"

print(f"{string1} contains special characters: {contains_special_characters(string1)}")
print(f"{string2} contains special characters: {contains_special_characters(string2)}")

