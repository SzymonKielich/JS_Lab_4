import os
import sys
import pathlib


def print_path_folders(*args):
    environment_vars = os.environ
    path_vals = environment_vars['PATH'].split(";")
    while '' in path_vals:
        path_vals.remove('')
    for val in path_vals:
        print(val, end='\n')


def print_path_folders_with_exec(*args):
    environment_vars = os.environ
    path_vals = environment_vars['PATH'].split(";")
    while '' in path_vals:
        path_vals.remove('')
    for val in path_vals:
        print(val, end=": \n")

        for filename in os.listdir(path=val):
            full_path = pathlib.Path(val).joinpath(filename)

            if not full_path.is_dir() and os.access(full_path, os.X_OK):
                print('\t', filename)




if __name__ == '__main__':
    if len(sys.argv) != 1:
        choice = sys.argv[1]
        if choice.lower() == 'a':
            print_path_folders(sys.argv[0])
        else:
            print_path_folders_with_exec(sys.argv[0])
