import time
from collections import Counter
from copy import deepcopy

from aocd import submit

from . import utils


def parse(data):
    template, rules = data.split("\n\n")
    rules = dict(map(lambda rule: rule.split(' -> '), rules.splitlines()))
    return template, rules


def solve(data, days=40):
    template, rules = data
    chars = Counter(template)
    pairs = Counter(template[i:i+2] for i, _ in enumerate(template[:-1]))

    for _ in range(days):
        new = pairs.copy()
        for pair, n in pairs.items():
            c = rules[pair]
            new[pair] -= n
            new[pair[0] + c] += n
            new[c + pair[1]] += n
            chars[c] += n
        pairs = new

    most, *_, least = chars.most_common()
    return most[1] - least[1]


def part_a(data):
    return solve(data, 10)


def part_b(data):
    return solve(data, 40)


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day14.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    data_a = deepcopy(data)
    print("Running day 14 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=14, year=2021)

    print("Running day 14 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=14, year=2021)
