import numpy as np

TEST_MAP = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

TEST_TARGET = 7


def parse_map(raw_map):
    rows = []
    for line in raw_map:
        row = list(line.strip())
        rows.append(row)
    forest = np.array(rows)
    forest = np.zeros_like(forest, dtype=int) + np.ones_like(forest, dtype=int) * (
        forest == "#"
    )
    return forest


def count_trees(forest, right=3, down=1):
    max_y, max_x = forest.shape
    y_vals = np.arange(0, max_y, down)
    idx = np.arange(0, len(y_vals))
    x_vals = idx * right
    x_vals = x_vals % (max_x)
    return forest[y_vals, x_vals].sum()


assert count_trees(parse_map(TEST_MAP.splitlines())) == TEST_TARGET
assert count_trees(parse_map(TEST_MAP.splitlines()), 1, 1) == 2
assert count_trees(parse_map(TEST_MAP.splitlines()), 3, 1) == 7
assert count_trees(parse_map(TEST_MAP.splitlines()), 5, 1) == 3
assert count_trees(parse_map(TEST_MAP.splitlines()), 7, 1) == 4
assert count_trees(parse_map(TEST_MAP.splitlines()), 1, 2) == 2

with open("inputs/day3.txt", "r") as infile:
    forest = parse_map(infile)
    print(count_trees(forest))

    print(
        count_trees(forest, 1, 1)
        * count_trees(forest, 3, 1)
        * count_trees(forest, 5, 1)
        * count_trees(forest, 7, 1)
        * count_trees(forest, 1, 2)
    )
