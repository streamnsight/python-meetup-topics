
# Command Line Python

## The mystery `__main__`

When importing a package, python will run the code in the file.

The `__name__` variable will be the name of the package imported

When running from the command line, the name is `__main__`

A Python script meant to run on the command line typically include the following code:

```python
if __name__ == '__main__':
    # do something
    # ...
    
```

This is to prevent the code to run if the package was to be imported by another package

## The hashbang, and the executable

At the top of the file, you might also find the typical

```python
#!./.venv/bin/python
```
to use our local environment


or more globally:
```python
#!/usr/local/bin/python
```

This indicates what interpreter needs to be used to read the code (i.e. python)

Without this line, the shell tries to interpret the python code (a text file) as a shell script 
and fails

In order for this to work, the file also needs to be made executable

```bash
# the file is not executable
./myscript.py                                                                                                                                                
-> command not found: myscript.py

# make the file executable
chmod +x myscript.py

./myscript.py
--> __main__
```

## Command line arguments

To parse command line arguments, the `argparse` package is your friend


## Logging

Logging without buffering:

use environment variable

`PYTHONUNBUFFERED=1`

also 

`python -m <script>`

