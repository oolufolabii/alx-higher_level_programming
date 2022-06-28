#!/usr/bin/python3
for num in range(122, 96, -2):
    print("{:c}{:s}".format(num, chr(num - 33)), end="")
