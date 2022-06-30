#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    num_of_arg = len(argv) - 1

    if num_of_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] == '+':
        addition = add(int(argv[1]), int(argv[3]))
        print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], addition))
    elif argv[2] == '-':
        subtraction = sub(int(argv[1]), int(argv[3]))
        print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], subtraction))
    elif argv[2] == '*':
        multiplication = mul(int(argv[1]), int(argv[3]))
        print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3],
                                       multiplication))
    elif argv[2] == '/':
        quotient = div(int(argv[1]), int(argv[3]))
        print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], quotient))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
