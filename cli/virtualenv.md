# Virtual Environments in Python

## Why use a virtual environment?

A virtual environment is an isolation mechanism insuring that a project runs in a well defined 
environment.

The version of packages used in the project can be controlled, as they are not shared
with other projects.

This allows multiple projects to use the same package with different versions without conflicts.

In short, it keeps things tidy when working on many projects on a single machine.

## How?

`virtualenv` is the tool used to create virtual environments.

```bash
pip install virtualenv
```

`virtualenv` defaults to creating an environment with the default Python version on the machine.


### Options at a glance


```bash
$ virtualenv
Usage: virtualenv [OPTIONS] DEST_DIR

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose         Increase verbosity.
  -q, --quiet           Decrease verbosity.
  -p PYTHON_EXE, --python=PYTHON_EXE
                        The Python interpreter to use, e.g.,
                        --python=python3.5 will use the python3.5 interpreter
                        to create the new environment.  The default is the
                        interpreter that virtualenv was installed with
                        (/usr/local/opt/python@2/bin/python2.7)
  --clear               Clear out the non-root install and start from scratch.
  --no-site-packages    DEPRECATED. Retained only for backward compatibility.
                        Not having access to global site-packages is now the
                        default behavior.
  --system-site-packages
                        Give the virtual environment access to the global
                        site-packages.
  --always-copy         Always copy files rather than symlinking.
  --relocatable         Make an EXISTING virtualenv environment relocatable.
                        This fixes up scripts and makes all .pth files
                        relative.
  --no-setuptools       Do not install setuptools in the new virtualenv.
  --no-pip              Do not install pip in the new virtualenv.
  --no-wheel            Do not install wheel in the new virtualenv.
  --extra-search-dir=DIR
                        Directory to look for setuptools/pip distributions in.
                        This option can be used multiple times.
  --download            Download preinstalled packages from PyPI.
  --no-download, --never-download
                        Do not download preinstalled packages from PyPI.
  --prompt=PROMPT       Provides an alternative prompt prefix for this
                        environment.
  --setuptools          DEPRECATED. Retained only for backward compatibility.
                        This option has no effect.
  --distribute          DEPRECATED. Retained only for backward compatibility.
                        This option has no effect.
  --unzip-setuptools    DEPRECATED.  Retained only for backward compatibility.
                        This option has no effect.

```

```bash
virtualenv .myvenv
```
creates a virtual environment in a local folder called .myenv, with the default python interpreter

Note: 
- I used a . in front of the folder name, so it ends up being hidden. This is a matter of preference
- setuptools, pip and wheel are installed by default

### Default Python interpreter

To figure what is the default python, use:

```angular2html
$ which python                                                              2 ↵  
/usr/local/bin/python
$ python --version                                                               
Python 2.7.15
$                                                                                
```

Nowadays you might want to always use Python3, since Python 2.7 will be deprecated next year.


### Specify Python version

```bash
virtualenv -p $(which python3) .venv
```

## Now what?



Here we go, we have an environment defined. 

To actually get into the environment, we need to activate it

```bash
source .venv/bin/activate
# or more simply, using the '.' shortcut for source:
. .venv/bin/activate
```

Now we can install packaged for this specific project
