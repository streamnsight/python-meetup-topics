# importing a package
# standard package can be imported without installation
import os

print(os.environ)

# external packages need to be installed first

import pandas

# set local name of imported package
import pandas as pd

print(pd.__version__)


# import only a specific function from a package
from os import environ

environ.get('PATH')

# import a module from a package
from datetime import date

print(date)
# import multiple modules from package
from datetime import date, timedelta

# import from submodule
from matplotlib.pyplot import matplotlib

# import all function of a module
from datetime import *

