from collections import Counter
import time

from aocd import submit

from . import utils


def parse(data):
    return list(map(int, data.strip().split(',')))


def solve(data, days):
    count = Counter(data)
    count = [0] + [count[v] for v in range(1, 7)] + [0, 0]
    n = [0] * len(count)
    for _ in range(days):
        new_count = n.copy()
        for i in range(8, 0, -1):
            new_count[i-1] = count[i]
        zeros = count[0]
        new_count[8] = zeros
        new_count[6] = new_count[6] + zeros
        count = new_count
    return sum(count)


def part_a(data):
    return solve(data, 80)


def part_b(data):
    return solve(data, 256)


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day06.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 6 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=6, year=2021)

    print("Running day 6 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=6, year=2021)
