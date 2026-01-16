#!/usr/bin/python3

if __name__ == "__main__":
    hidden = __import__("hidden_4")

    for name in sorted(dir(hidden)):
        if not name.startswith("__"):
            print(name)
