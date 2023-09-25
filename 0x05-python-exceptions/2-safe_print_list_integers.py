#!usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    for y in range(x):
        try:
            print("{:d}".format(y), end="")
            idx += 1

        except (TypeError, ValueError):
            continue
    print()
    return idx
