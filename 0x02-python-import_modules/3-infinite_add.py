#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_of_arg = len(argv) - 1

    total_sum = 0
    for num in range(1, num_of_arg + 1):
        total_sum += int(argv[num])

    print("{:d}".format(total_sum))
