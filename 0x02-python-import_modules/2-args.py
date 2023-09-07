#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("{} {}:".format(0, "arguments"))
    elif num_args == 1:
        print("{} {}:".format(1, "argument"))
    else:
        print("{} {}:".format(num_args, "arguments"))
        for i in range(1, len(sys.argv)):
            args = sys.argv[i]
            print("{}: {}".format(i, args))
