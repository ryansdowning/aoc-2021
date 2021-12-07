from functools import cache
import time

from aocd import submit

from . import utils


def parse(data):
    return list(map(int, data.split(',')))


@cache
def get_fuel_cost(steps):
    return (steps * (steps + 1)) // 2


def part_a(data):
    x = min(data)
    y = max(data)
    m = float('inf')
    for i in range(x, y + 1):
        total = 0
        for num in data:
            total += abs(num - i)
        if total < m:
            m = total
    return m


def part_b(data):
    x = min(data)
    y = max(data)
    m = float('inf')
    for i in range(x, y + 1):
        total = 0
        for num in data:
            total += get_fuel_cost(abs(num - i))
        if total < m:
            m = total
    return m


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day07.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 7 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=7, year=2021)

    print("Running day 7 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=7, year=2021)
