#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import os
    from calculator_1 import add, sub, mul, div
    operation = ["+", "-", "/", "*"]
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
    elif (sys.argv[2] not in operation):
        print("Unknown operator. Available operators: +, -, * and /")
        print(1)
    else:
        operate = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if operate == "+":
            print("{} {} {} = {}".format(a, operate, b, add(a, b)))
        elif operate == "-":
            print("{} {} {} = {}".format(a, operate, b, sub(a, b)))
        elif operate == "*":
            print("{} {} {} = {}".format(a, operate, b, mul(a, b)))
        else:
            print("{} {} {} = {}".format(a, operate, b, div(a, b)))
