#!/usr/bin/env python3
"""
python_batch_template.py
To run the Python script from the terminal, store the script in $:~/.scripts
Enable execution with chmod +x <scriptname> use the python or python3 command, followed by the script name.
Reload with `$:source ~/.bashrc` or close and reopen the terminal:
To run the script type <scriptname> and include parameters after the script name.
"""
import sys
import os
import click

# @click.command() makes read_pattern behave as a command line interface.
"""
examples for optional parameters
@click.option('--patterns', '-p', multiple=True, help='Patterns to search for')
@click.option('--all', '-a', is_flag=True, help='All patterns must be found for the filepath to be printed')
@click.option('--swap_axes', '-s', default=False, help='swap x- and y-axes', is_flag=True)
"""


@click.command()
@click.argument('new_script_name', type=str)  # default parameter
def main(new_script_name):
    """
    :param new_script_name: script to be created with this template as content
    """
    template = '''#!/usr/bin/env python3
"""
This is a sample template created by python_batch_template.py
Further customize it as per your needs.

<script_name>
To run the Python script from the terminal, store the script in $:~/.scripts 
Enable execution with chmod +x <scriptname> use the python or python3 command, followed by the script name.
Reload with `$:source ~/.bashrc` or close and reopen the terminal:
To run the script type <scriptname> and include parameters after the script name.
"""
import sys
import os
import click

# @click.command() makes read_pattern behave as a command line interface.
"""
examples for optional parameters
@click.option('--patterns', '-p', multiple=True, help='Patterns to search for')
@click.option('--all', '-a', is_flag=True, help='All patterns must be found for the filepath to be printed')
@click.option('--swap_axes', '-s', default=False, help='swap x- and y-axes', is_flag=True)
"""
@click.command()
@click.argument('test_input', type=str)  # default parameter
def main(test_input):
    """
    :param : test_input: default parameter template as example
    """
    pass

if __name__ == '__main__':
    main()
    '''

    while True:
        if os.path.exists(new_script_name):
            should_overwrite = input(f"File {new_script_name} exists. Overwrite? (y/n):\n")
            if should_overwrite.lower() == 'y':
                break
            else:
                new_script_name = input("Enter a new file name:\n")
        else:
            break

    # Create/overwrite the python file with the given name
    with open(new_script_name, 'w') as file:
        file.write(template)


if __name__ == '__main__':
    main()
