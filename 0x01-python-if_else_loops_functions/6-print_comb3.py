#!/usr/bin/python3

for a in range(10):
    for b in range(a + 1, 10):
        if b < 9:
            print("{:02d}".format(a * 10 + b), end=", ")
        else:
            print("{:02d}".format(a * 10 + b))
