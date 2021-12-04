import time

from aocd import submit

from . import utils


class Board:
    def __init__(self, board: list[list[int]]):
        self.n, self.m = len(board), len(board[0])
        self.board = {(row, col): val for row, lst in enumerate(board) for col, val in enumerate(lst)}
        self.iboard = {val: pos for pos, val in self.board.items()}
        self.called = {pos: False for pos in self.board}
        self.win_counts = {'rows': [0 for _ in range(self.n)], 'cols': [0 for _ in range(self.m)], 'diags': [0, 0]}
        self.winning = False

    def call_val(self, val: int):
        # Original solution:
        # if val in self.board:
        #     self.called[pos] = True
        if val in self.iboard:
            pos = self.iboard[val]
            if not self.called[pos]:
                self.win_counts['rows'][pos[0]] += 1
                self.win_counts['cols'][pos[1]] += 1
                if pos[0] == pos[1]:
                    self.win_counts['diags'][0] += 1
                if pos[0] + pos[1] == self.n - 1:
                    self.win_counts['diags'][1] += 1
                self.called[pos] = True
                self.winning = self.winning or any(
                    count == self.n
                    for count in [
                        self.win_counts['rows'][pos[0]], self.win_counts['cols'][pos[1]]
                    ] + self.win_counts['diags']
                )

    def remaining_sum(self):
        return sum(self.board[pos] for pos, is_called in self.called.items() if not is_called)

    def check_win(self):
        return self.winning
        # Original solution below, does not involve the additional logic in check_val; naively checks each direction.
        # The current solution tracks the number of bingo spots called for each possible win condition, if the count
        # equals the size of the board, that win condition has been met.
        # if self.winning:
        #     return True
        #
        # def check_direction(start, direction):
        #     if not self.called[start]:
        #         return False
        #     x, y = start
        #     h, v = direction
        #
        #     while -1 < x < self.n and -1 < y < self.m:
        #         if not self.called[(x, y)]:
        #             return False
        #         x += h
        #         y += v
        #     return True
        #
        # DIRS = {
        #     (0, 1): [(i, 0) for i in range(self.n)],
        #     (1, 1): [(0, 0)],
        #     (1, 0): [(0, i) for i in range(self.m)],
        #     (1, -1): [(0, self.m-1)]
        # }
        #
        # for dir_, starts in DIRS.items():
        #     for start in starts:
        #         if check_direction(start, dir_):
        #             self.winning = True
        #             return True
        # return False


def parse(data):
    chunks = data.split('\n\n')
    calls = list(map(int, chunks[0].split(',')))
    boards = list(
        map(lambda chunk: Board(list(
            map(lambda line: list(
                map(int, line.strip().replace('  ', ' ').split(' '))
            ), chunk.strip().splitlines())
        )), chunks[1:])
    )
    return calls, boards


def part_a(data):
    calls, boards = data
    for call in calls:
        for board in boards:
            board.call_val(call)
            if board.check_win():
                return board.remaining_sum() * call
    raise Exception("No winning board")


def part_b(data):
    calls, boards = data
    total = len(boards)
    winning = [False for _ in range(total)]
    count = 0
    for call in calls:
        for i, board in enumerate(boards):
            if winning[i]:
                continue
            board.call_val(call)
            if board.check_win():
                count += 1
                if count == total:
                    return board.remaining_sum() * call
                winning[i] = True
    raise Exception("Not every board won")


if __name__ == "__main__":
    with open("/home/ryan/Desktop/repos/aoc/aoc-2021/python/solutions/../../inputs/day04.txt", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day 4 part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {utils.format_time(elapsed_a)} with solution: {solution_a}, submitting...")
    submit(solution_a, part="a", day=4, year=2021)

    print("Running day 4 part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {utils.format_time(elapsed_b)} with solution: {solution_b}, submitting...")
    submit(solution_b, part="b", day=4, year=2021)
