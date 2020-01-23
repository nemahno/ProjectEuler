
"""
Find the sum of all the multiples of 3 and 5 below limit
"""


def multiple_of_5_3_sum(limit):
    _sum = 0

    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            _sum += i
    return _sum


if __name__ == '__main__':
    value = multiple_of_5_3_sum(1000)
    print(value)
