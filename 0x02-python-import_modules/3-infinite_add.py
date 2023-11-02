#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    result = 0
    if length > 0:
        if length == 1:

            print("{}".format(int(sys.argv[1])))
        else:
            for i in range(1, length+1):
                result += int(sys.argv[i])
            print("{}".format(result))
    else:
        print("{}".format(result))
