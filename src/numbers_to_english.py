"""
Write a function that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that integer written in English.

example:

>>> numbers_to_english(0)
'zero'

>>> numbers_to_english(18)
'eighteen'

>>> numbers_to_english(909)
'nine hundred nine'

>>> numbers_to_english(126)
'one hundred twenty six'

"""

import logging

logging.basicConfig(level=logging.DEBUG)

def numbers_to_english(n: int) -> str:
    num_dict = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
        40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
        80: 'eighty', 90: 'ninety'
    }

    if n in num_dict:
        return num_dict[n]
    else:
        if n < 100:
            return num_dict[n // 10 * 10] + ' ' + num_dict[n % 10]
        else:
            return num_dict[n // 100] + ' hundred ' + numbers_to_english(n % 100)

if __name__ == '__main__':
    import doctest
    logging.info(f"Tests: {doctest.testmod()}")
