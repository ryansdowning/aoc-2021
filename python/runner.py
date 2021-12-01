import glob
from pathlib import Path
from functools import partial
from importlib import import_module
import statistics

from solutions import utils

YEAR = 2021
PKG_NAME = "solutions"
INPUTS_PATH = Path("../inputs")
SOLUTION_PATTERN = "solutions/day*.py"

MODULES = {}
for file in glob.glob(SOLUTION_PATTERN):
    stem = Path(file).stem
    MODULES[stem] = import_module(f"{PKG_NAME}.{stem}", PKG_NAME)

if __name__ == "__main__":
    print(f"Starting runner for {YEAR}")

    for stem, module in MODULES.items():
        day = int(stem[-2:])
        print(f"Running day {day}")

        with open(INPUTS_PATH / f"{stem}.txt", 'r') as fp:
            time, runs, data = utils.timeit(fp.read)
        n = len(runs)
        print(
            f"Reading: {utils.format_time(time / n):<7s} ± {utils.format_time(statistics.stdev(runs))}"
            f" per loop (mean ± std. dev. of {n} loops)"
        )

        parse = partial(module.parse, data)
        time, runs, data = utils.timeit(parse)
        n = len(runs)
        print(
            f"Parsing: {utils.format_time(time / n):<7s} ± {utils.format_time(statistics.stdev(runs))}"
            f" per loop (mean ± std. dev. of {n} loops)"
        )

        part_a = partial(module.part_a, data)
        time, runs, solution_a = utils.timeit(part_a)
        n = len(runs)
        print(
            f"Part A:  {utils.format_time(time / n):<7s} ± {utils.format_time(statistics.stdev(runs))}"
            f" per loop (mean ± std. dev. of {n} loops)"
        )

        part_b = partial(module.part_b, data)
        time, runs, solution_b = utils.timeit(part_b)
        n = len(runs)
        print(
            f"Part B:  {utils.format_time(time / n):<7s} ± {utils.format_time(statistics.stdev(runs))}"
            f" per loop (mean ± std. dev. of {n} loops)"
        )
