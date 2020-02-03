# Basic syntax:

# This is a comment
example = 0  # A comment can also come at the end of a line of code. 2 spaces before the # is recommended

'''
This is a multi-line string, which as stand alone is also a interpreted as comment.
This is the second line
'''

"""
Same goes with the double quotes
"""

# variable names tend to be written in snake_case, but it is not a requirement.
my_variable = 0


# class names tend to be written in CamelCase, but it is not a requirement either
class MyClass:
    pass


# function names are also typically in snake_case
def my_function(var1, var2):
    """
    :param var1: this is variable 1 in the function
    :param var2: this is variable 2 in the function
    :return:
    """
    # the lines above are called DocStrings, and they are used to document the code.
    # they can be parsed by framework like Sphynx to generate a HTML documentation for the code
    # triple double quotes are used for DocStrings
    pass

