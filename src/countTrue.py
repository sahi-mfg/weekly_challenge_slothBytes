"""
week 1: Count True Values in a List

Create a function which returns the number of True values there are in an array.

Examples
count_true([True, False, False, True, False]) ➞ 2
count_true([False, False, False, False]) ➞ 0
count_true([]) ➞ 0

"""


def count_true(lst: list) -> int:
    return lst.count(True)


def count_true_from_scratch(lst: list) -> int:
    count = 0
    for item in lst:
        if item:
            count += 1
    return count


if __name__ == "__main__":
    print("##### Python built-in count method #####")
    print(count_true([True, False, False, True, False]))
    print(count_true([False, False, False, False]))
    print(count_true([]))
    print(count_true([True, True, True, True, True]))

    print("\n#### From scratch ####")
    print(count_true_from_scratch([True, False, False, True, False]))
    print(count_true_from_scratch([False, False, False, False]))
    print(count_true_from_scratch([]))
    print(count_true_from_scratch([True, True, True, True, True]))
