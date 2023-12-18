#!/usr/bin/env python3
"""
Python script which parses each of the $PATH directories and checks if they exist.
Existing $PATH directory names are printed to the console.
If the directory doesn't exist it is printed, marked as missing.
"""

import os

# Get the PATH environment variable
path = os.getenv('PATH')

# Split the PATH string by ':' to get individual directories
directories = path.split(':')

# Iterate over the list of directories
for directory in directories:
    # Check if the directory exists
    if not os.path.exists(directory):
        # If the directory doesn't exist, print it
        print(f"missing-------------------------------------{directory}---------missing")
    else:
        print(directory)
