# From https://www.youtube.com/watch?v=GxCXiSkm6no 
# cd <to here>
# conda create --name importing_custom python=3.9.12
# conda activate importing_custom
# pip install -r requirements.txt

# First way to import is to import a function from a file in
# the same directory as where the call is being made

from functionality import add

print(add(10, 20))

# Alternatively, import all functions in that file

from smaller import *

print(sub1(10))

print(sub2(10))

# If importing from a module, specify module then file name
# to import all objects in that module's file

from other_module import second

second.myfunction()

# Can also append file name after module and use *

from third_module.third import *

third_function()


# The import * syntax only works if referring to a file, it seems
# but not to a folder with multiple files.

from fourth import *

# This will not work:
# fourth_function()
# fourth_file.fourth_function()
# fourth.fourth_file.fourth_function()


# Using __init__.py helps out here
# within that file, list the files you want to make importable
# they still have to be specified when calling their functions, however


from fifth import *

fifth_file.fifth_function()


# Working with subfolders
# No __init__ needed if call everything explicitly

from sixth.subfolder import sixth_file

sixth_file.sixth_fxn()

# No list needed in __init__.py if make imports explicit in that file

from seventh import *

seventh_file.seventh_fux()