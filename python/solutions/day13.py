import time
from copy import deepcopy

from aocd import submit

from . import utils


def parse(data):
    points, folds = data.split("\n\n")
    points = set(map(lambda line: tuple(map(int, line.strip().split(','))), points.strip().splitlines()))
    folds = list(map(lambda line: line.split('fold along ')[1].split('='), folds.strip().splitlines()))
    folds = [(_, int(v)) for _, v in folds]
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]
    grid = [[int((x, y) in points) for x in range(max_x+1)] for y in range(max_y+1)]
    return grid, folds


def fold_left(grid, val):
    ylen = len(grid)
    xlen = val * 2
    return [[grid[y][x] or grid[y][xlen-x] for x in range(val)] for y in range(ylen)]


def fold_up(grid, val):
    ylen = val * 2
    xlen = len(grid[0])
    return [[grid[y][x] or grid[ylen-y][x] for x in range(xlen)] for y in range(val)]


def part_a(data):
    grid, folds = data
    for fold_dir, val in folds[:1]:
        if fold_dir == 'y':
            grid = fold_up(grid, val)
        elif fold_dir == 'x':
            grid = fold_left(grid, val)
    return sum(map(sum, grid))


def part_b(data):
    grid, folds = data
    for fold_dir, val in folds:
        if fold_dir == 'y':
            grid = fold_up(grid, val)
        elif fold_dir == 'x':
            grid = fold_left(grid, val)
    return grid


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day13.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    data_a = deepcopy(data)
    print("Running day 13 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=13, year=2021)

    print("Running day 13 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=13, year=2021)
