#!usr/bin/env python3
""""""


class VerboseList(list):
    """"""
    def append(item):
        """"""
        super().append(item)
        print("Added [item] to the list")

    def extend(item):
        """"""
        x = len(item)
        super().extend(x)
        print("Extended the list with [x] items")

    def remove(item):
        """"""
        super().remove()
        print("Removed [item] from the list")

    def pop(item):
        """"""
        super().pop()
        print("Popped [item] from the list")
