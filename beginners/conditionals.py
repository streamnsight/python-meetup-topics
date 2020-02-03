# Conditionals

# The variable names for true and false are True and False. an undeclared variable has the value None
a = True
b = False
c = None

# is notation to test boolean equivalence
if a is True:
    # do something
    print('a is true')
else:
    # do something else
    print('a is false')

# 'not' notation for boolean non-equivalence
if a is not True:
    print('a is not true')

# else if is shorten to 'elif'
if a is True:
    print('a is true')
elif a is None:
    print('a is no defined')


# conditional with numeric values
x = 1
y = 2
z = 3

if x == 1:
    print('x is equal to 1')
elif x != 1:
    print('x is not equal to 1')

# or condition
if x > 1 or x < 1:
    print('x is not equal to 1')

# For more complex expressions, use parens
if (x == 1 and y >= 1) or z < 2:
    print('condition met')

# assignment with conditional

w = 5 if x == 1 else 3
# w = 5 since x is equal to 1
print(w)

# There is no 'switch / case' in Python
