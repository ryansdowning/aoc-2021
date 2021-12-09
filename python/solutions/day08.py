import time
from collections import defaultdict
from functools import reduce

from aocd import submit

from . import utils


MAP = [
    set("abcefg"), set("cf"), set("acdeg"), set("acdfg"), set("bcdf"), set("abcdfg"),
    set("abdefg"), set("acf"), set("abcdefg"), set("abcdfg")
]
# NUM_MAP = {s: n for n, s in enumerate(MAP)}
LENS = [len(i) for i in MAP]
LENS_MAP = {len_: str(i) for i, len_ in enumerate(LENS)}


def parse(data):
    return list(
        map(
            lambda line: list(map(lambda splitline: list(map(set, splitline.split(' '))), line.split(' | '))),
            data.splitlines()
        )
    )


def part_a(data):
    N = {2, 4, 3, 7}
    total = 0
    for _, outputs in data:
        total += sum(len(o) in N for o in outputs)
    return total


def resolve(output, segments):
    n = len(output)
    if n == 6:
        if len(set(output).union(segments[4])) == 6:
            return "9"
        elif len(set(output).intersection(segments[1])) == 2:
            return "0"
        return "6"
    if n == 5:
        if len(set(digit).union(segments[1])) == n:
            return "3"
        elif len(set(digit).union(segments[4])) == 7:
            return "2"
        return "5"
    return LENS_MAP[n]


def part_b(data):
    total = 0
    for segments, outputs in data:
        wires = defaultdict(list)
        for segment in segments:
            wires[len(segment)].append(segment)

        (one,) = wires[2]
        (seven,) = wires[3]
        (four,) = wires[4]
        (*three_five, two) = sorted(wires[5], key=(one | four).__rsub__)
        (three, five) = sorted(three_five, key=two.__rsub__)
        (*zero_nine, six) = sorted(wires[6], key=one.__sub__)
        (nine, zero) = sorted(zero_nine, key=three.__rsub__)
        (eight,) = wires[7]

        wire_map = (zero, one, two, three, four, five, six, seven, eight, nine)
        resolved = [wire_map.index(output) for output in outputs]
        total += reduce(lambda acc, num: 10 * acc + num, resolved)
    return total


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day08.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 8 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=8, year=2021)

    print("Running day 8 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=8, year=2021)
