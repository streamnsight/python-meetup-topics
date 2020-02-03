# For loop

# simple loop over array of values
for x in [1, 2, 3, 4]:
    print(x)
# prints:
# 1
# 2
# 3
# 4

for x in range(4):
    print(x)
# prints:
# 0
# 1
# 2
# 3


# get the index of an element in the array within the loop
for i, x in enumerate(['a', 'b', 'c', 'd']):
    print(f'{x} is at index {i}')


# loop through key/value pairs of a dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}
for k, v in dict1.items():
    print(f'key {k} has value: {v}')

for k in dict1:
    print(k)

# List comprehension
a = ['a', 'b', 'c', 'd']
b = [letter.upper() for letter in a]
print(b)

b = []
for letter in a:
    b.append(letter.upper())

# conditional in list comprehension
a = ['a', 'b', 'c', 'd']
b = [letter.upper() for letter in a if letter != 'b']
print(b)


# dictionary comprehension
dict1 = {'a': 1, 'b': 2, 'c': 3}

dict2 = {k: v * 2 for k, v in dict1.items()}
print(dict2)


# While loops
count = 3

while count:  # count is True if not 0
    print(count)
    count -= 1


# break and continue
for x in range(10):
    if x < 5:
        continue  # skip the rest of the code and continue with the loop
    if x > 7:
        break  # stop the loop
    print(x)


# there is no 'do ... until' in python
count = 3
while True:
    count -= 1
    if count == 0:
        break


