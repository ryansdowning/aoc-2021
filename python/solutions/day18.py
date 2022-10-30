import time
import json
import math
from itertools import permutations
from functools import reduce
from copy import deepcopy

from aocd import submit

from . import utils


def parse(data):
    return list(map(json.loads, data.splitlines()))


def add_idx(snailfish, n, idx):
    if n is None:
        return snailfish
    if isinstance(snailfish, int):
        return snailfish + n
    return [
        add_idx(num, n, idx) if i == idx else num
        for i, num in enumerate(snailfish)
    ]


def explode(snailfish, n=4):
    if isinstance(snailfish, int):
        return False, None, snailfish, None
    if n == 0:
        return True, snailfish[0], 0, snailfish[1]

    x, y = snailfish
    exp, left, x, right = explode(x, n - 1)
    if exp:
        return True, left, [x, add_idx(y, right, 0)], None

    exp, left, y, right = explode(y, n - 1)
    if exp:
        return True, None, [add_idx(x, left, 1), y], right
    return False, None, snailfish, None


def split(snailfish):
    if isinstance(snailfish, int):
        if snailfish >= 10:
            return True, [snailfish // 2, math.ceil(snailfish / 2)]
        return False, snailfish
    x, y = snailfish
    change, x = split(x)
    if change:
        return True, [x, y]
    change, y = split(y)
    return change, [x, y]


def magnitude(x):
    return x if isinstance(x, int) else 3 * magnitude(x[0]) + 2 * magnitude(x[1])


def solve(x, y):
    pair = [x, y]
    while True:
        change, _, pair, _ = explode(pair)
        if change:
            continue
        change, pair = split(pair)
        if not change:
            break
    return pair


def part_a(data):
    return magnitude(reduce(solve, data))


def part_b(data):
    return max(magnitude(solve(x, y)) for x, y in permutations(data, 2))


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day18.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    data_a = deepcopy(data)
    print("Running day 18 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=18, year=2021)

    print("Running day 18 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=18, year=2021)
