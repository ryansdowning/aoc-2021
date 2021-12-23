import time
from functools import reduce
from copy import deepcopy

from aocd import submit

from . import utils

BIT_MAP = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

OPS = [
    sum,
    lambda x: reduce(lambda acc, curr: acc * curr, x),
    min,
    max,
    None,
    lambda x: x[0] > x[1],
    lambda x: x[0] < x[1],
    lambda x: x[0] == x[1]
]


def parse(data):
    return ''.join(BIT_MAP[bit] for bit in data)


class PacketDecoder:
    def __init__(self, data):
        self.data = data
        self.i = 0
        self.vers = []

    def read_bytes(self, n):
        val = int(self.data[self.i:self.i+n], base=2)
        self.i += n
        return val

    def get_packet(self):
        self.vers.append(self.read_bytes(3))
        t = self.read_bytes(3)

        if t == 4:
            val = 0
            while self.read_bytes(1) == 1:
                val = (val << 4) + self.read_bytes(4)
            return (val << 4) + self.read_bytes(4)

        if self.read_bytes(1) == 0:
            vals = []
            packets = self.read_bytes(15)
            end = self.i + packets
            while self.i < end:
                vals.append(self.get_packet())
        else:
            vals = [self.get_packet() for _ in range(self.read_bytes(11))]
        return OPS[t](vals)


def part_a(data):
    decoder = PacketDecoder(data)
    decoder.get_packet()
    return sum(decoder.vers)


def part_b(data):
    decoder = PacketDecoder(data)
    return decoder.get_packet()


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day16.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    data_a = deepcopy(data)
    print("Running day 16 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=16, year=2021)

    print("Running day 16 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=16, year=2021)
