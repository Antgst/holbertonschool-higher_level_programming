#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0
    div = 0

    for i in range(0, list_length, 1):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            print("division by 0")
            div = 0
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
        except (IndexError):
            print("out of range")
            div = 0
        finally:
            result.append(div)
    return result
