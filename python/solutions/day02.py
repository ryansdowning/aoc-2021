import time

from aocd import submit

from . import utils


DIRECTIONS = {"f": (0, 1), "d": (1, 0), "u": (-1, 0)}


def parse(data):
    out = []
    for line in data.strip().split("\n"):
        direction, val = line[0], int(line[-1])
        vert, horiz = DIRECTIONS[direction]
        out.append((vert*val, horiz*val))
    return out


def part_a(data):
    vert, horiz = 0, 0
    for v, h in data:
        vert += v
        horiz += h
    return vert * horiz


def part_b(data):
    vert, horiz, aim = 0, 0, 0
    for v, h in data:
        aim += v
        horiz += h
        vert += h * aim
    return vert * horiz


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day02.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 2 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=2, year=2021)

    print("Running day 2 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=2, year=2021)
