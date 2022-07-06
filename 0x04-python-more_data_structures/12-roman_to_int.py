#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_alphabet = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_numeral = 0
    for item in range(len(roman_string)):
        if item > 0 and roman_alphabet[roman_string[item]] > roman_alphabet[roman_string[j - 1]]:
            roman_numeral += roman_alphabet[roman_string[item]] - 2 * \
                roman_alphabet[roman_string[item - 1]]
        else:
            roman_numeral += roman_alphabet[roman_string[item]]
    return roman_numeral
