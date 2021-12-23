import time
from heapq import heappop, heappush
from copy import deepcopy

from aocd import submit

from . import utils


def parse(data):
    return list(map(lambda line: list(map(int, line)), data.splitlines()))


def solution(data, scale=1):
    n, m = len(data), len(data[0])
    heap = [(0, (0, 0))]
    visited = {(0, 0)}
    while heap:
        val, (i, j) = heappop(heap)
        if i == (n * scale) - 1 and j == (m * scale) - 1:
            return val

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = i + dx, j + dy
            if x < 0 or y < 0 or x >= n * scale or y >= m * scale:
                continue

            a, am = divmod(x, n)
            b, bm = divmod(y, m)
            dist = (data[am][bm] + a + b - 1) % 9 + 1
            if (x, y) not in visited:
                visited.add((x, y))
                heappush(heap, (val + dist, (x, y)))


def part_a(data):
    return solution(data, 1)


def part_b(data):
    return solution(data, 5)


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day15.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    data_a = deepcopy(data)
    print("Running day 15 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=15, year=2021)

    print("Running day 15 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=15, year=2021)
