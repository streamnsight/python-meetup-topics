# Base types
# Python is not strongly typed (contrary to other languages like
# C, C++, C#, Java, Go...)
# A variable can be any type
int_var = 1  # a number. !!! By default this will be an integer
print(type(int_var))
# 'int'

float_var = 1.  # a number. This will be a float
print(type(float_var))
# 'float'

string_var = 'string'  # a "regular" string (which defaults to
# UniCode in Python 3.x)
print(type(string_var))
# 'str'

binary_string_var = b'binarystring'  # i.e. a string that is not encoded, equivalent to a list of bytes
print(type(binary_string_var))
# 'bytes'

# Important note on numbers: Python 2.7 vs. Python 3
a = 3
b = 2
c = a // b
print(c)  # In python 2.7, this would return 1 (integer division, returning an integer)
# In python 3 it returns the more intuitive result 1.5
# (Use Python 3!)

# Dictionaries
# dict are data structures that hold key/value pairs (also called hash or maps in other languages)
dictionary = {'key': 'value'}
dictionary2 = {'key1': {'nested_key': 1}}

# and empty dict
empty_dict = {}

# Getting the keys of a dictionary:
dictionary.keys()

# adding key/values to a dictionary:
dict1 = {}
dict1['key1'] = 'value1'
dict1['key2'] = 'value2'
print(dict1)

# dictionary key from a variable:
key_name='mykey'
dict2 = {key_name: 'value'}
print(dict2)


# Lists (also called arrays)
# A Python List can contain a mix of element types, hence it is not an 'array' as typically understood
# in other typed languages. It is implemented as a dynamic array
# each element is in fact a pointer to its content anyway, since it can be any type.
array_var = [1, 2, 3, 'one', 'two', 'three']

# Append to an array
array_var.append('four')
array_var += [3]

# get element from an array by index
print(array_var[0])  # first element: arrays are 0 indexed


# get a sub-set (range) of the array
print(array_var[1:3])  # get second and third elements (exclusive of fourth at index 3 (i.e index 1 and 2)
print(array_var[3:5])  # get 4th and 5th elements (exclusive of 6th at index 5 (i.e index 1 and 2)


# Sets (list of unique values)
empty_set = set()  # note that a set can also be initialized with {}, but it can be confused with dict
unique_values = {1, 2, 3, 2, 1, 5}
print(unique_values)
# will contain {1, 2, 3, 5}

# this is also valid:
unique_values = set([1, 2, 3, 2, 1, 5])

# Add to a set:
unique_values.add(6)

# Remove from a set
unique_values.remove(3)
# remove would raise an error if the value doesn't exist in the set

# Discard from a set
unique_values.discard(7)
# discard does not raise an error
