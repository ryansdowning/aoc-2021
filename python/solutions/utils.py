import math
from statistics import quantiles, stdev
from time import perf_counter
from typing import Any, Callable


def format_time(seconds: float) -> str:
    if seconds > 1e0:
        return f"{seconds:.2f} sec"
    if seconds > 1e-3:
        return f"{int(seconds * 1e3)} ms"
    if seconds > 1e-6:
        return f"{int(seconds * 1e6)} μs"
    if seconds > 1e-9:
        return f"{int(seconds * 1e9)} ns"
    return str(seconds)


def timeit(func: Callable[[], Any], max_time=15) -> tuple[float, list[float], Any]:
    runs = []

    start = perf_counter()
    result = func()
    end = perf_counter()

    total_elapsed = end - start
    runs.append(total_elapsed)

    est_runs = max_time // total_elapsed
    est_runs = 10 ** (math.floor(math.log10(est_runs))) - 1

    for _ in range(est_runs):
        start = perf_counter()
        func()
        end = perf_counter()
        elapsed = end - start

        runs.append(elapsed)
        total_elapsed += elapsed

    return total_elapsed, runs, result


def format_results(name, total_elapsed, runs, result=None, verbose=2):
    if verbose == 0:
        return ""

    n = len(runs)
    mu = total_elapsed / n
    std = stdev(runs)
    name = f"{name}:"
    line1 = f"{name:<8}{format_time(mu):>8} ± {format_time(std):<8} per loop (mean ± std. dev. of {n} loops)"

    if verbose == 1:
        return line1

    low, high = min(runs), max(runs)
    low_o, *_, high_o = quantiles(runs, n=100)
    line2 = (
        f"min: {format_time(low):>5}, max: {format_time(high):>5}, "
        f"1%: {format_time(high_o):>5}, 99%: {format_time(low_o):>5}"
    )
    if verbose == 2:
        return f"{line1}\n{line2}"

    results_str = f"Result: {result}\n" if result is not None else ""
    return f"{results_str}\n{line1}\n{line2}"
