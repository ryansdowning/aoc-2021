import time

from aocd import submit

from . import utils

INV_MAP = {"{": "}", "(": ")", "<": ">", "[": "]"}


def parse(data):
    return data.splitlines()


def part_a(data):
    val_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total = 0
    for line in data:
        stack = []
        for c in line:
            if c in INV_MAP:
                stack.append(c)
            elif c != INV_MAP[stack[-1]]:# or len(stack) == 0:
                total += val_map[c]
                break
            else:
                stack.pop(-1)
    return total
        

def part_b(data):
    val_map = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for line in data:
        stack = []
        score = 0
        for c in line:
            if c in INV_MAP:
                stack.append(c)
            elif c != INV_MAP[stack[-1]]:# or len(stack) == 0:
                break
            else:
                stack.pop(-1)
        else:
            for v in reversed(stack):
                score *= 5
                score += val_map[INV_MAP[v]]
            scores.append(score)
    return sorted(scores)[len(scores)//2]


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day10.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 10 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=10, year=2021)

    print("Running day 10 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=10, year=2021)
