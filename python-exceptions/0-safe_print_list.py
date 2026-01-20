#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    count = 0

    if my_list is None:
        print()
        return 0

    if not my_list:
        print()
        return 0

    while i < x:
        try:
            print(my_list[i], end="")
            i += 1
            count += 1
        except IndexError:
            break

    print()
    return count
