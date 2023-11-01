#!/usr/bin/python3
def uppercase(c):
    for i in c:
        lettre_to_number = ord(i)
        if (97 <= lettre_to_number and lettre_to_number <= 122):
            change = 32
        else:
            change = 0
        print("{:c}".format(lettre_to_number - change), end="")
