#!/usr/bin/python3

if __name__ == "__main__":
    hidden = __import__("hidden_4")

    names = dir(hidden)

    for name in names:
        if not name.startswith("__"):
            print(name)
