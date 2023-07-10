#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate_numbers(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Example usage
n = 50

generator = DivisibleBySeven(n).generate_numbers()
for num in generator:
    print(num)

# Question 2:
Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
# In[2]:


def compute_word_frequency(input_string):
    words = input_string.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[0])

    return sorted_word_count

# Example usage
input_string = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

frequency = compute_word_frequency(input_string)
for word, count in frequency:
    print(f"{word}:{count}")

# Question 3:

Define a class Person and its two child classes: Male and Female. All classes have a
method 'getGender' which can print 'Male' for Male class and 'Female' for Female
class.
# In[3]:


class Person:
    def getGender(self):
        print("Unknown")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

# Example usage
person = Person()
person.getGender()  # Output: Unknown

male = Male()
male.getGender()  # Output: Male

female = Female()
female.getGender()  # Output: Female

#Question 4:
Please write a program to generate all sentences where subject is in ['I', 'You'] and
verb is in ['Play', 'Love'] and the object is in ['Hockey','Football'].
# In[4]:


def generate_sentences():
    subjects = ['I', 'You']
    verbs = ['Play', 'Love']
    objects = ['Hockey', 'Football']

    sentences = []

    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentence = f"{subject} {verb} {obj}"
                sentences.append(sentence)

    return sentences

# Example usage
sentences = generate_sentences()
for sentence in sentences:
    print(sentence)

# Question 5:
Please write a program to compress and decompress the string 'hello world!hello
world!hello world!hello world!'.
# In[5]:


import gzip

def compress_string(string):
    compressed_data = gzip.compress(string.encode())
    return compressed_data

def decompress_string(compressed_data):
    decompressed_data = gzip.decompress(compressed_data).decode()
    return decompressed_data

# Example usage
original_string = 'hello world!hello world!hello world!hello world!'

compressed_data = compress_string(original_string)
print(f"Compressed data: {compressed_data}")

decompressed_string = decompress_string(compressed_data)
print(f"Decompressed string: {decompressed_string}")

# Question 6:
Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list.
# In[6]:


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not found

# Example usage
sorted_list = [2, 5, 7, 10, 15, 20, 25]
target = 10

index = binary_search(sorted_list, target)
print(f"The index of {target} in the list: {index}")

