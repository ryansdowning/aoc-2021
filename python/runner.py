import argparse
import glob
import statistics
from functools import partial
from importlib import import_module
from pathlib import Path

from solutions import utils

parser = argparse.ArgumentParser()
parser.add_argument("--days", "-d", type=int, nargs="*")
parser.add_argument("--verbose", "-v", action="count", default=1)

YEAR = 2021
PKG_NAME = "solutions"
INPUTS_PATH = Path("../inputs")
SOLUTION_PATTERN = "solutions/day*.py"

MODULES = {}
for file in glob.glob(SOLUTION_PATTERN):
    stem = Path(file).stem
    MODULES[stem] = import_module(f"{PKG_NAME}.{stem}", PKG_NAME)
MODULES = sorted(((stem, module) for stem, module in MODULES.items()), key=lambda x: x[0])

if __name__ == "__main__":
    args = parser.parse_args()
    days = args.days
    verbose = args.verbose
    print(f"Starting runner for {YEAR}")

    for stem, module in MODULES:
        day = int(stem[-2:])
        if days and day not in days:
            continue
        print(f"Running day {day}")

        with open(INPUTS_PATH / f"{stem}.txt", "r") as fp:
            time, runs, data = utils.timeit(fp.read)
        print(utils.format_results("Reading", time, runs, verbose=verbose))

        parse = partial(module.parse, data)
        time, runs, data = utils.timeit(parse)
        n = len(runs)
        print(utils.format_results("Parsing", time, runs, verbose=verbose))

        part_a = partial(module.part_a, data)
        time, runs, solution_a = utils.timeit(part_a)
        print(utils.format_results("Part A", time, runs, solution_a, verbose=verbose))

        part_b = partial(module.part_b, data)
        time, runs, solution_b = utils.timeit(part_b)
        print(utils.format_results("Part B", time, runs, solution_b, verbose=verbose))

        print()
