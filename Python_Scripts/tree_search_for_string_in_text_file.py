#!/usr/bin/env python3
# tree_search_for_string_in_text_file.py
"""
Take a pattern list as input and find files that contain these patterns in their text.
The script doesn't consider the binary files. It skips files with restricted access.
"""

import os
import re
import click


# @click.command() makes read_pattern behave as a command line interface.
@click.command()
@click.option('--patterns', '-p', multiple=True, help='Patterns to search for')
@click.option('--all', '-a', is_flag=True, help='All patterns must be found for the filepath to be printed')
def read_pattern(patterns, all):
    """This script finds files that contain patterns in their text. Files without read permissions or binary files
    are skipped. The scipped files are stored in the file: 'skipped_files.txt'.
    :param patterns: patterns to search
    :param all: if set, all patterns must be found for the filepath to be printed
    :return: None
    """
    # uses Click to get input from the command line when the script is run
    if not patterns or len(patterns) == 0:
        click.echo("Please provide a pattern")
        return

    # Pass the all flag to find_files
    find_files(".", patterns, all)


def is_text(filename):
    """
    :param filename:
    :return: Boolean
    Takes filename as an argument and tries to open and read the file in text mode ('r').
    If the file is no text file or the attempt to read the file raises a PermissionError,
    the filename is stored in 'skipped_files.txt' """
    if not os.path.isfile(filename):
        return False
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


def find_files(root_dir, pattern_list, all_present):
    """
    :param root_dir:
    :param pattern_list:
    :return:
    This function takes a directory path and a list of patterns as arguments. It compiles regular expressions from the
    pattern_list and walks through the directory structure from the root directory. For each file in each nested directory,
    it checks if the file is text, using is_text. If it is, the function attempts to open the file and read its
    contents. If a PermissionError is raised, it notes the filepath in 'skipped_files.txt'.
    For each compiled pattern, it searches the file's contents. If any of the patterns match, it prints the filepath
    and exits the loop for this file. Files are only inspected once: finding one match is considered enough.
    """
    """ pattern_list is a list that contains regular expression patterns as strings.
    re.compile(p) compiles the regular expression pattern p into a regular expression object.
    [re.compile(p) for p in pattern_list] is a list comprehension that applies re.compile(p) to each element p 
    in pattern_list.
    The result is a list of regular expression objects. The resulting list pattern_compiled allows these
    compiled regular expression objects to be used later for matching patterns in strings more efficiently.
    Once a regular expression pattern has been compiled, it can be used repeatedly
    to match the pattern in different texts.
    """

    pattern_compiled = [re.compile(p) for p in pattern_list]

    for directory_path, dirs, files in os.walk(root_dir):
        for filename in files:
            filepath = os.path.join(directory_path, filename)
            if not is_text(filepath):
                continue
            try:
                with open(filepath, "r") as file:
                    contents = file.read()

                # Define a list to store the results
                results = [pattern.search(contents) is not None for pattern in pattern_compiled]
                # If all patterns must be found: Flag -a is True
                if all_present:
                    # Only output filepath if all patterns found
                    if all(results):
                        print(filepath)
                # Else, Flag -a is false
                else:
                    # If any pattern is found, output the filepath
                    if any(results):
                        print(filepath)

            except PermissionError:
                with open('skipped_files.txt', 'a') as skipped:
                    skipped.write(filepath + '\n')


if __name__ == '__main__':
    read_pattern()
