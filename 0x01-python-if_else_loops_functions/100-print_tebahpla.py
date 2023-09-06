#!/usr/bin/python3

for a in range(90, 64, -1):
    if a % 2 == 0:
        b = chr(a + 32)
    else:
        b = chr(a)
    print("{}".format(b), end="")
