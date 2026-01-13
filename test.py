#!/usr/bin/python3

def decode(message, shift):
    decoded = ""
    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            decoded += chr((ord(char) - base - shift) % 26 + base)
        else:
            decoded += char
    return decoded

secret_message = "M'di kdwh gh uhdolvhu wrxwh ohv fkrvhv grqw rq sdboh dx txrwlglhq."
shift = 3

print(decode(secret_message, shift))