#!/usr/bin/env python
# coding: utf-8
Question1
Create a function that takes three integer arguments (a, b, c) and returns the amount of
integers which are of equal value.
Examples
equal(3, 4, 3) ➞ 2
equal(1, 1, 1) ➞ 3
equal(3, 4, 1) ➞ 0
Notes
Your function must return 0, 2 or 3.
# In[1]:


def equal(a, b, c):
    if a == b == c:  # All three integers are equal
        return 3
    elif a == b or b == c or a == c:  # Two integers are equal
        return 2
    else:  # No integers are equal
        return 0

# Example usage:
print(equal(3, 4, 3))  # Output: 2
print(equal(1, 1, 1))  # Output: 3
print(equal(3, 4, 1))  # Output: 0

Question2
Write a function that converts a dictionary into a list of keys-values tuples.
# In[2]:


def dict_to_list(dictionary):
    return sorted(dictionary.items())

# Example usage:
print(dict_to_list({"D": 1, "B": 2, "C": 3}))  # Output: [("B", 2), ("C", 3), ("D", 1)]
print(dict_to_list({"likes": 2, "dislikes": 3, "followers": 10}))  # Output: [("dislikes", 3), ("followers", 10), ("likes", 2)]

Question3
Write a function that creates a dictionary with each (key, value) pair being the (lower case,
upper case) versions of a letter, respectively.
# In[3]:


def mapping(letters):
    dictionary = {}
    for letter in letters:
        dictionary[letter] = letter.upper()
    return dictionary

# Example usage:
print(mapping(["p", "s"]))  # Output: {"p": "P", "s": "S"}
print(mapping(["a", "b", "c"]))  # Output: {"a": "A", "b": "B", "c": "C"}
print(mapping(["a", "v", "y", "z"]))  # Output: {"a": "A", "v": "V", "y": "Y", "z": "Z"}

Question4
Write a function, that replaces all vowels in a string with a specified vowel.
# In[4]:


def vow_replace(string, vowel):
    vowels = "aeiou"
    replaced_string = ""
    for char in string:
        if char.lower() in vowels:
            replaced_string += vowel
        else:
            replaced_string += char
    return replaced_string

# Example usage:
print(vow_replace("apples and bananas", "u"))  # Output: "upplus und bununus"
print(vow_replace("cheese casserole", "o"))  # Output: "chooso cossorolo"
print(vow_replace("stuffed jalapeno poppers", "e"))  # Output: "steffed jelepene peppers"

Question5
Create a function that takes a string as input and capitalizes a letter if its ASCII code is even
and returns its lower case version if its ASCII code is odd.
# In[5]:


def ascii_capitalize(string):
    result = ""
    for char in string:
        if ord(char) % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

# Example usage:
print(ascii_capitalize("to be or not to be!"))  # Output: "To Be oR NoT To Be!"
print(ascii_capitalize("THE LITTLE MERMAID"))  # Output: "THe LiTTLe meRmaiD"
print(ascii_capitalize("Oh what a beautiful morning."))  # Output: "oH wHaT a BeauTiFuL moRNiNg."

