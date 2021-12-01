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


def timeit(func: Callable[[], Any]) -> tuple[float, list[float], Any]:
    runs = []

    start = perf_counter()
    result = func()
    end = perf_counter()

    total_elapsed = start - end
    runs.append(total_elapsed)

    return total_elapsed, runs, result

