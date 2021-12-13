import time
from collections import defaultdict
from copy import deepcopy

from aocd import submit

from . import utils


def parse(data):
    adj_list = defaultdict(set)
    for a, b in list(map(lambda line: line.split('-'), data.splitlines())):
        adj_list[a].add(b)
        adj_list[b].add(a)
    return adj_list


def part_a(data):
    def dfs(node, visited, paths=0):
        if node == 'end':
            return 1
        for neighbor in data[node]:
            if neighbor[0].islower():
                if neighbor not in visited:
                    paths += dfs(neighbor, {neighbor, *visited})
            else:
                paths += dfs(neighbor, visited)
        return paths
    return dfs('start', {'start'})


def part_b(data):
    def dfs(node, visited, flag=True, paths=0):
        if node == 'end':
            return 1
        for neighbor in data[node]:
            if neighbor[0].islower():
                if neighbor not in visited:
                    paths += dfs(neighbor, {neighbor, *visited}, flag)
                elif flag and neighbor not in {'start', 'end'}:
                    paths += dfs(neighbor, visited, False)
            else:
                paths += dfs(neighbor, visited, flag)
        return paths
    return dfs('start', {'start'})


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day12.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    data_a = deepcopy(data)
    print("Running day 12 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=12, year=2021)

    print("Running day 12 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=12, year=2021)
