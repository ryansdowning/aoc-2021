from collections import defaultdict
import time

from aocd import submit

from . import utils


def get_coords(splitline):
    start = splitline[0].split(',')
    start = (int(start[0]), int(start[1]))
    end = splitline[1].split(',')
    end = (int(end[0]), int(end[1]))

    if start[0] == end[0]:
        start_y = min(start[1], end[1])
        end_y = max(start[1], end[1]) + 1
        return [(start[0], i) for i in range(start_y, end_y)]
    elif start[1] == end[1]:
        start_x = min(start[0], end[0])
        end_x = max(start[0], end[0]) + 1
        return [(i, start[1]) for i in range(start_x, end_x)]
    elif abs(start[0] - end[0]) == abs(start[1] - end[1]):
        x_step = (start[0] < end[0]) * 2 - 1
        y_step = (start[1] < end[1]) * 2 - 1
        return [(start[0]+(i*x_step), start[1]+(i*y_step)) for i in range(abs(start[0] - end[0]) + 1)]
    raise Exception("Line is not straight or 45 degrees")


def parse(data):
    data = list(map(lambda line: get_coords(line.split(' -> ')), data.splitlines()))
    return data


def part_a(data):
    count = defaultdict(int)
    for line in data:
        if line[0][0] != line[-1][0] and line[0][1] != line[-1][1]:
            continue
        for point in line:
            count[point] += 1
    return sum(c > 1 for c in count.values())


def part_b(data):
    count = defaultdict(int)
    for line in data:
        for point in line:
            count[point] += 1
    return sum(c > 1 for c in count.values())


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day05.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 5 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=5, year=2021)

    print("Running day 5 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=5, year=2021)
