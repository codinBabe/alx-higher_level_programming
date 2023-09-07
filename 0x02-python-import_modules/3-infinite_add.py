#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    if len(argv) == 1:
        print("0")
    else:
        res = 0
        for i in argv[1:]:
            res += int(i)
            print(res)
