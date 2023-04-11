import os
import sys

def print_all_vars():
    environment_vars = sorted(os.environ.items())
    for key_val_tup in environment_vars:
        print(f'{key_val_tup[0]}: {key_val_tup[1]}', end='\n')


def print_filtered(*args):
    environment_vars = sorted(os.environ.items())
    cmd_args = sys.argv[1:]
    for key_val_tup in environment_vars:
        for arg in cmd_args:
            if arg.lower() in key_val_tup[0].lower():
                print(f'{key_val_tup[0]}: {key_val_tup[1]}', end='\n')




if __name__ == '__main__':
    if len(sys.argv) != 1:
        print_filtered(sys.argv[0])
    else:
        print_all_vars()