import time
from collections import defaultdict

from aocd import submit

from . import utils


MAP = [
    set("abcefg"), set("cf"), set("acdeg"), set("acdfg"), set("bcdf"), set("abcdfg"),
    set("abdefg"), set("acf"), set("abcdefg"), set("abcdfg")
]
# NUM_MAP = {s: n for n, s in enumerate(MAP)}
LENS = [len(i) for i in MAP]
LENS_MAP = {len_: i for i, len_ in enumerate(LENS)}


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


def part_b(data):
    total = 0
    for segments, outputs in data:
        wires = [set("abcdefg")] * 7
        for segment in segments:
            n = len(segment)
            if n == 2:
                wires[2] &= segment
                wires[5] &= segment
            elif n == 3:
                wires[0] &= segment
                wires[2] &= segment
                wires[5] &= segment
            elif n == 4:
                wires[1] &= segment
                wires[2] &= segment
                wires[3] &= segment
                wires[5] &= segment

        wire_map = {}
        for i, c in enumerate("abcdefg"):
            if len(wires[i]) == 1:
                wire_map[c] = wires[i].pop()
            else:
                print(c,  wires[i])
                raise Exception("Could not resolve wires")

        for output in outputs:
            mapped_output = set(wire_map[c] for c in output)
            total += MAP.index(mapped_output) + 1

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
