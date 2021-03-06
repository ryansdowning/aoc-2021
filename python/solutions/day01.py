import time

from aocd import submit
import pandas as pd
import numpy as np

from . import utils


def parse(data) -> list[int]:
    return pd.Series(list(map(int, data.split("\n"))))


def solve_numpy(data, window=1):
    # cast list to np.ndarray in the parse function if using
    return (data[window:] > data[:-window]).sum()


def solve(data, window=1):
    # cast list to pd.Series in parse function if using
    return (data.values[window:] > data.values[:-window]).sum()


# O(n) time, no extra space
# def solve(data, window=1):
#     return sum(curr > prev for prev, curr in zip(data, data[window:]))


# O(n) time, no extra space
def part_a(data):
    return solve(data, 1)


# O(n) time, no extra space
def part_b(data):
    return solve(data, 3)


# O(n) time, O(1) space, O(n * window) swaps
def _part_a(data):
    n = len(data)
    if n < 2:
        return 0

    count = 0
    prev = data[0]
    for curr in data[1:]:
        if curr > prev:
            count += 1
        prev = curr
    return count


# O(n) time, O(1) space, O(n * window) swaps
def _part_b(data):
    n = len(data)
    if n < 4:
        return 0

    count = 0
    a, b, c = data[:3]
    total = a + b + c
    for num in data[3:]:
        new_total = total - a + num
        a, b, c = b, c, num
        if new_total > total:
            count += 1
        total = new_total
    return count


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day01.txt", "r") as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 1 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=1, year=2021)

    print("Running day 1 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=1, year=2021)
