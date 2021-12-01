import math
from time import perf_counter
from typing import Callable, Any


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
    est_runs = 10**(math.floor(math.log10(est_runs))) - 1

    for _ in range(est_runs):
        start = perf_counter()
        func()
        end = perf_counter()
        elapsed = end - start

        runs.append(elapsed)
        total_elapsed += elapsed

    return total_elapsed, runs, result

