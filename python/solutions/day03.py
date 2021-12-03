import time
from collections import Counter

from aocd import submit

from . import utils


def parse(data):
    return list(map(lambda line: list(map(int, line)), data.splitlines()))


def part_a(data):
    n, m = len(data[0]), len(data) // 2
    count = [0] * n
    for line in data:
        for i, num in enumerate(line):
            count[i] += num

    count = [c > m for c in count]
    return int(''.join(str(int(c)) for c in count), base=2) * int(''.join(str(int(not c)) for c in count), base=2)


def _part_b(data):
    data_t = list(zip(*data))
    counts = list(map(Counter,  data_t))

    counts_most = counts.copy()
    counts_least = counts.copy()
    data_most = data.copy()
    data_least = data.copy()
    m = l = len(data)
    n = len(data[0])
    i = 0
    while m > 1 or l > 1:
        if m > 1:
            m_val = int(counts_most[i][1] >= counts_most[i][0])
            new_most = []
            for data_m in data_most:
                if data_m[i] == m_val:
                    new_most.append(data_m)
                else:
                    counts_most[i+1][data_m[i+1]] -= 1
            data_most = new_most
        if l > 1:
            l_val = int(counts_least[i][1] < counts_least[i][0])
            new_least = []
            for data_l in data_least:
                if data_l[i] == l_val:
                    new_least.append(data_l)
                else:
                    counts_least[i+1][data_l[i+1]] -= 1
            data_least = new_least
        i += 1
        m = len(data_most)
        l = len(data_least)

    oxygen = int(''.join(str(a) for a in data_most[0]), base=2)
    co = int(''.join(str(a) for a in data_least[0]), base=2)
    return oxygen * co


def part_b(data):
    d = data.copy()
    f = data.copy()
    i = 0
    while len(d) > 1 or len(f) > 1:
        if len(d) != 1:
            t = len(d) / 2
            o = int(sum(l[i] for l in d) >= t)
            d = [l for l in d if l[i] == o]
        if len(f) != 1:
            t = len(f) / 2
            c = int(sum(l[i] for l in f) < t)
            f = [l for l in f if l[i] == c]
        i += 1
    oxygen = int(''.join(str(a) for a in d[0]), base=2)
    co = int(''.join(str(a) for a in f[0]), base=2)
    return oxygen * co


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day03.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 3 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=3, year=2021)

    print("Running day 3 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=3, year=2021)
