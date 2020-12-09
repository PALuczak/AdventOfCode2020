from typing import List

TEST_DATA = [1721, 979, 366, 299, 675, 1456]
TEST_TARGET = 514579


def find_product(values: List[int], target=2020):
    needs = {target - val for val in values}

    for val in values:
        if val in needs:
            return val * (target - val)


assert find_product(TEST_DATA) == TEST_TARGET


from itertools import combinations

TEST_TARGET = 241861950


def find_triple_product(values: List[int], target=2020):
    needs = {target - a - b: (a, b) for a, b in combinations(values, 2)}

    for val in values:
        if val in needs:
            a, b = needs[val]
            return val * a * b


assert find_triple_product(TEST_DATA) == TEST_TARGET


with open("inputs/day1.txt", "r") as infile:
    real_data = [int(line) for line in infile]
    print(find_product(real_data))
    print(find_triple_product(real_data))
