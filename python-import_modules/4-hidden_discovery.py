#!/usr/bin/python3

if __name__ == __import__("hidden_4"):
    words = __import__("hidden_4")

    names = dir(hidden)

    for name in names:
        if not name.startswith("__"):
            print(name)
