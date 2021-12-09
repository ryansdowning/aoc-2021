import time
from functools import reduce

from aocd import submit

from . import utils


def parse(data):
    return list(map(lambda line: list(map(int, line)), data.splitlines()))


def part_a(data):
    n, m = len(data), len(data[0])
    total = 0
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if (i < 1 or data[i-1][j] > val) and (i > n - 2 or data[i+1][j] > val) and (j < 1 or data[i][j-1] > val) and (j > m - 2 or data[i][j+1] > val):
                total += val + 1
    return total


def part_b(data):
    data = [[0 if num != 9 else 9 for num in line] for line in data]
    n, m = len(data), len(data[0])
    basins = []

    def basin_size(x, y):
        size = 0
        value = data[x][y]
        if value == 0:
            data[x][y] = 1
            size = 1
            if x > 0:
                size += basin_size(x-1, y)
            if x < n - 1:
                size += basin_size(x+1, y)
            if y > 0:
                size += basin_size(x, y-1)
            if y < m - 1:
                size += basin_size(x, y+1)
        return size

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            basins.append(basin_size(i, j))

    # print(basins)
    return reduce(lambda acc, num: acc * num, sorted(basins)[-3:], 1)


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day09.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 9 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=9, year=2021)

    print("Running day 9 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=9, year=2021)
