#!/usr/bin/python3
import sys


def main():
    length = len(sys.agrv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc))
        for i in range(1, length + 1):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == '__main__':
    main()
