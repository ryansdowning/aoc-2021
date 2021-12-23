import time
from copy import deepcopy

from aocd import submit

from . import utils


def parse(data):
    _, data = data.split('target area: ')
    x, y = data.split(', ')
    x = list(map(int, x[2:].split('..')))
    y = list(map(int, y[2:].split('..')))
    return x, y


def part_a(data):
    _, (y1, y2) = data
    return int(abs(y1) * (abs(y1) - 1) / 2)


def part_b(data):
    (x1, x2), (y1, y2) = data

    def simulate(vx, vy, x, y):
        if x > x2 or y < y1:
            return 0
        if x >= x1 and y <= y2:
            return 1
        return simulate(vx - (vx > 0), vy - 1, x + vx, y + vy)
    return sum(simulate(vx, vy, 0, 0) for vx in range(1, x2 + 1) for vy in range(y1, -y1))


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day17.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    data_a = deepcopy(data)
    print("Running day 17 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=17, year=2021)

    print("Running day 17 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=17, year=2021)
