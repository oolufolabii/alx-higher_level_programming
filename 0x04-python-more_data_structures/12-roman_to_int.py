#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    last = 0
    numerals = (('I', 1), ('V', 5), ('X', 10),
                ('L', 50), ('C', 100), ('D', 500),
                ('M', 1000))

    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0

    for item in reversed(roman_string):
        for elem in numerals:
            if item == elem[0]:
                if elem[1] < last:
                    result -= elem[1]
                else:
                    result += elem[1]
                last = elem[1]
    return result
