import argparse
import pathlib

from aocd import get_data


def str_to_dir(path: str) -> pathlib.Path:
    path = pathlib.Path(path)
    if path.is_dir():
        return path
    raise ValueError(f"Unresolved path, could not locate directory at: {path}")


def str_to_file(path: str) -> pathlib.Path:
    path = pathlib.Path(path)
    if not path.exists():
        return path
    raise ValueError(f"Cannot create solution at: {path}, file already exists")


parser = argparse.ArgumentParser()
parser.add_argument("--year", "-y", type=int, help="year of the advent-of-code challenge", required=True)
parser.add_argument("--day", "-d", type=int, help="day of the advent-of-code challenge", required=True)
parser.add_argument(
    "--inputs-path",
    "-i",
    type=str_to_dir,
    default=pathlib.Path(__file__).parent.resolve() / "../../inputs",
    help="Path to directory to store inputs",
)
parser.add_argument(
    "--solution-path",
    "-s",
    type=str_to_file,
    help="Path of file to create for the challenge's solution. If not provided, day_<day>.py will be used as default.",
)

if __name__ == "__main__":
    args = parser.parse_args()

    if not args.solution_path:
        default_solution_path = pathlib.Path(f"day{args.day:02d}.py")
        if default_solution_path.exists():
            raise FileExistsError(
                f"Solution path was not provided and the default path ({default_solution_path}) already exists"
            )
    else:
        default_solution_path = args.solution_path

    data = get_data(day=args.day, year=args.year)
    inputs_path = args.inputs_path / f"day{args.day:02d}.txt"
    with open(inputs_path, "w") as fp:
        fp.write(data)

    solution_template = f"""import time

from aocd import submit

from . import utils


def parse(data):
    pass


def part_a(data):
    pass


def part_b(data):
    pass


if __name__ == "__main__":
    with open("{inputs_path}", 'r') as fp:
        data = fp.read()

    data = parse(data)

    print("Running day {args.day} part A")
    start_a = time.perf_counter()

    solution_a = part_a(data)

    stop_a = time.perf_counter()
    elapsed_a = stop_a - start_a
    print(f"Part A finished in {{utils.format_time(elapsed_a)}} with solution: {{solution_a}}, submitting...")
    submit(solution_a, part="a", day={args.day}, year={args.year})

    print("Running day {args.day} part B")
    start_b = time.perf_counter()

    solution_b = part_b(data)

    stop_b = time.perf_counter()
    elapsed_b = stop_b - start_b
    print(f"Part B finished in {{utils.format_time(elapsed_b)}} with solution: {{solution_b}}, submitting...")
    submit(solution_b, part="b", day={args.day}, year={args.year})
"""
    default_solution_path.write_text(solution_template)
