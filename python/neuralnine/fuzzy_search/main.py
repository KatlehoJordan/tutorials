# From https://www.youtube.com/watch?v=WNFBLi6CaTM
# cd <to here>
# conda create --name fuzzy_search python=3.7
# conda activate fuzzy_search
# pip install -r requirements.txt
# Note that one of the packages threw an error:
# Microsoft Visual C++ 14.0 or greater is required.
# Get it with "Microsoft C++ Build Tools": 
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Thus I installed Visual Studio Build tools.
# However, that was going to take over 6 GB, which was too much, so I abandoned.
# It did not seem to matter though, it may just do pattern matching slower

import os
from fuzzywuzzy import fuzz
root_dir = input("Enter the root directory for your search: ")
file_types = input("Enter the file endings to look for (separated by spaces) (Empty = All): ")
fuzzy_search = input("Enter a fuzzy search query (Empty = None): ")

file_types = file_types.split(" ")

for root, dirs, files in os.walk(root_dir):
    for name in files:
        if name.endswith(tuple(ft for ft in file_types)) or file_types[0] == "":
            if fuzz.token_sort_ratio(fuzzy_search.lower(), name.lower()) > 50 or fuzzy_search == "":
                print(root + os.sep + name)