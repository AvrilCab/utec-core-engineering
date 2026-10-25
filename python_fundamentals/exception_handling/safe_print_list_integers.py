#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    i = 0
    while True:
        if i >= x:
            break
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_print += 1
        except TypeError:
            pass
        i += 1
    print()
    return nb_print
