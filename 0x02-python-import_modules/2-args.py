#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_of_arg = len(argv) - 1

    print(num_of_arg, end=" ")

    if num_of_arg == 1:
        print("argument", end="")
    else:
        print("arguments", end="")

    if num_of_arg == 0:
        print(".")
    else:
        print(":")

    for num in range(1, num_of_arg + 1):
        print("{:d}: {}".format(num, argv[num]))
