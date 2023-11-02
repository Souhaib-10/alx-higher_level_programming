#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0 or length == 1:
        print("{} arguments".format(length))
    else:
        print("{} arguments".format(length))
        for i in range(1, length+1):
            print("Argument {}: {}".format(i, sys.argv[i]))
