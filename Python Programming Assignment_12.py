#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to Extract Unique values dictionary values?

def extract_unique_values(dictionary):
    unique_values = set()

    for values in dictionary.values():
        if isinstance(values, list):
            unique_values.update(values)
        else:
            unique_values.add(values)

    return unique_values

# Example usage
my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value1',
    'key4': ['value3', 'value4'],
    'key5': 'value2'
}

unique_values = extract_unique_values(my_dict)
print(f"Unique values: {unique_values}")


# In[2]:


# 2. Write a Python program to find the sum of all items in a dictionary?

def sum_of_dictionary_items(dictionary):
    total_sum = sum(dictionary.values())
    return total_sum

# Example usage
my_dict = {'item1': 10, 'item2': 20, 'item3': 30, 'item4': 40}

total_sum = sum_of_dictionary_items(my_dict)
print(f"Sum of dictionary items: {total_sum}")


# In[3]:


# 3. Write a Python program to Merging two Dictionaries?

def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged = merge_dictionaries(dict1, dict2)
print(f"Merged dictionary: {merged}")


# In[4]:


# 4. Write a Python program to convert key-values list to flat dictionary?

def convert_to_flat_dictionary(key_value_list):
    flat_dict = {}

    for pair in key_value_list:
        key, value = pair
        flat_dict[key] = value

    return flat_dict

# Example usage
key_value_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

flat_dictionary = convert_to_flat_dictionary(key_value_list)
print(f"Flat dictionary: {flat_dictionary}")


# In[5]:


# 5. Write a Python program to insertion at the beginning in OrderedDict?

from collections import OrderedDict

def insert_at_beginning(ordered_dict, key, value):
    ordered_dict[key] = value
    ordered_dict.move_to_end(key, last=False)

# Example usage
my_ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print("Before insertion:")
for key, value in my_ordered_dict.items():
    print(key, value)

insert_at_beginning(my_ordered_dict, 'x', 99)

print("\nAfter insertion:")
for key, value in my_ordered_dict.items():
    print(key, value)


# In[6]:


# 6. Write a Python program to check order of character in string using OrderedDict()?

from collections import OrderedDict

def check_order_of_characters(string, pattern):
    char_order = OrderedDict()

    for char in string:
        char_order[char] = char

    pattern_index = 0

    for char in char_order:
        if pattern_index >= len(pattern):
            break
        if char == pattern[pattern_index]:
            pattern_index += 1

    return pattern_index == len(pattern)

# Example usage
string = "Hello, World!"
pattern1 = "Hlo"
pattern2 = "lHo"

print(f"Order of characters in '{string}' for pattern '{pattern1}': {check_order_of_characters(string, pattern1)}")
print(f"Order of characters in '{string}' for pattern '{pattern2}': {check_order_of_characters(string, pattern2)}")


# In[7]:


# 7. Write a Python program to sort Python Dictionaries by Key or Value?

def sort_dictionary_by_key(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[0]))
    return sorted_dict

def sort_dictionary_by_value(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
    return sorted_dict

# Example usage
my_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}

sorted_by_key = sort_dictionary_by_key(my_dict)
print(f"Sorted by Key: {sorted_by_key}")

sorted_by_value = sort_dictionary_by_value(my_dict)
print(f"Sorted by Value: {sorted_by_value}")

