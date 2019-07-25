#!./.venv/bin/python

"""
When importing a package, python will run the code in the file.
The __name__ variable will be the name of the package imported
When running a Python script, Python will run whatever is defined as a 

The following line will print "myscript" when imported, but will print "__main__" when ran as the main script
"""
print(__name__)


# This test insures that this code only runs when the script is called from the command line, and NOT when
# the package is imported by another package.

if __name__ == '__main__':
    pass