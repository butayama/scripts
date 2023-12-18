#!/usr/bin/env python3
"""
In this script,
In the find_files function, it skips over files that is_text determines to be binary
with if not is_text(filepath): continue.
Again, please replace "." with the directory you wish to search if it's not the current directory.
And this script still doesn't account for files that it doesn't have permission to read.
"""

import os
import re
import click


@click.command()
@click.argument('pattern')
def read_pattern(pattern):
    """This script converts files to the PDF format"""
    return pattern


def is_text(filename):
    try:
        with open(filename, 'r') as f:
            for block in f:
                if '\0' in block:
                    return False
    except UnicodeDecodeError:
        return False
    except PermissionError:
        with open('skipped_files.txt', 'a') as skipped:
            skipped.write(filename + '\n')
        return False

    return True


def find_files(root_dir, patterns):
    """ patterns is a list that contains regular expression patterns as strings.
    re.compile(p) compiles the regular expression pattern p into a regular expression object.
    [re.compile(p) for p in patterns] is a list comprehension that applies re.compile(p) to each element p in patterns.
    The result is a list of regular expression objects. The resulting list pattern_compiled allows these
    compiled regular expression objects to be used later for matching patterns in strings more efficiently.
    Once a regular expression pattern has been compiled, it can be used repeatedly
    to match the pattern in different texts.
    """
    pattern_compiled = [re.compile(p) for p in patterns]

    for directory_path, dirs, files in os.walk(root_dir):
        for filename in files:
            filepath = os.path.join(directory_path, filename)
            if not is_text(filepath):
                continue
            try:
                with open(filepath, "r") as file:
                    contents = file.read()
                for pattern in pattern_compiled:
                    if pattern.search(contents):
                        print(filepath)
                        break
            except PermissionError:
                with open('skipped_files.txt', 'a') as skipped:
                    skipped.write(filepath + '\n')


if __name__ == '__main__':
    patterns = read_pattern()
    find_files("..", patterns)
