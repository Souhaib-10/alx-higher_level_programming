#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("{:d} arguments.".format(length))
    elif length == 1:

        print("{:d} argument:".format(length))
        print("{:d}: {}".format(length, sys.argv[length]))
    else:
        print("{:d} arguments:".format(length))
        for i in range(1, length+1):
            print("{:d}: {}".format(i, sys.argv[i]))
