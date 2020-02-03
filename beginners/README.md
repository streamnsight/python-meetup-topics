# Getting started with Python

## Introduction

### Why Python?

Python has been used for scientific programming for quite a while, as well as for backend server development.

It has grown in popularity with the advance of Machine Learning as it is free, easy to learn, offers countless packages and it a generalist language.

### Python 2.7 vs. Python 3.x

As of January 2020, the choice is much easier:
Python 2.7 has reached End of Life. Just use Python 3.x!

### IDEs (Development editors)

- The hard way: vim, nano or other basic text editor
- The Official Python way: IDLE
- The generalist option: EMACs etc...
- The more popular choices: VS Code + Python extension, PyCharm (CE or Pro edition)

Personal preference for PyCharm Pro for the additional set of tools (DB explorer etc...)

## Installing Python

Python comes pre-installed on Mac OSX, but it tends to be Python 2.7!

There are various installers on the Python.org website.

For Mac OS, I'd recommend using `pyenv` to manage Python versions, and then use pip as the package manager.
```bash
brew install pyenv
# then
pyenv install <version>
#
pyenv global 3.8.1 # for latest Python release
# and set this line in your ~/.bash_profile (or whatever bash you use)

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

```

For Windows systems, the popular choice is to use Anaconda.


## Environment

### Virtual Environments

In order to separate project, it is highly recommended to use a virtual environment

```bash
pip install virtualenv

virtualenv -p $(which python3) .venv

source .venv/bin/activate
# or
. .venv/bin/activate
```

On Windows:

```
\env\Scripts\activate.bat
```

### Project requirements

In order to keep track of what packages are installed during development and needed on installation, it is
recommended to use requirements files, that can install all requirements at once.

