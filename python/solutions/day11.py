import time

from aocd import submit
from functools import reduce
from itertools import product, count

from . import utils


def parse(data):
    return list(map(lambda line: list(map(int, line)), data.splitlines()))


def part_a(data):
    n, m = len(data), len(data[0])
    total = 0
    for _ in range(100):
        flashed = []
        for i, row in enumerate(data):
            for j, _ in enumerate(row):
                data[i][j] += 1
                if data[i][j] > 9:
                    data[i][j] = float('-inf')
                    flashed.append((i, j))

        while flashed:
            x, y = flashed.pop(0)
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if 0 <= x + dx < n and 0 <= y + dy < m:
                    data[x+dx][y+dy] += 1
                    if data[x+dx][y+dy] > 9:
                        data[x+dx][y+dy] = float('-inf')
                        flashed.append((x+dx, y+dy))

        for i, row in enumerate(data):
            for j, val in enumerate(row):
                if val < 0:
                    total += 1
                    data[i][j] = 0
    return total


def part_b(data):
    n, m = len(data), len(data[0])
    t = n * m
    step = 0
    while True:
        flashed = []
        flashes = 0
        for i, row in enumerate(data):
            for j, _ in enumerate(row):
                data[i][j] += 1
                if data[i][j] > 9:
                    data[i][j] = float('-inf')
                    flashed.append((i, j))

        while flashed:
            x, y = flashed.pop(0)
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if 0 <= x + dx < n and 0 <= y + dy < m:
                    data[x+dx][y+dy] += 1
                    if data[x+dx][y+dy] > 9:
                        data[x+dx][y+dy] = float('-inf')
                        flashed.append((x+dx, y+dy))

        for i, row in enumerate(data):
            for j, val in enumerate(row):
                if val < 0:
                    flashes += 1
                    data[i][j] = 0
        if flashes == t:
            return step
        step += 1


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day11.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 11 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=11, year=2021)

    print("Running day 11 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=11, year=2021)
