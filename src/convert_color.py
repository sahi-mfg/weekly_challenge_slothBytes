"""
Create a function that inverts rgb colors of a given list

Examples:

>>> invert_colors([255, 255, 255])
[0, 0, 0]
>>> invert_colors([255, 244, 100])
[0, 11, 155]
>>> invert_colors([0, 0, 0])
[255, 255, 255]
>>> invert_colors([165, 170, 221])
[90, 85, 34]
"""

import logging


def invert_colors(rgb: list) -> list:
    return [255 - i for i in rgb]


if __name__ == "__main__":
    import doctest

    logging.info(f"Tests: {doctest.testmod()}")
    print(invert_colors([255, 255, 255]))
    print(invert_colors([255, 244, 100]))
