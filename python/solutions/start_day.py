import argparse
from aocd import get_data
import os
import pathlib


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
parser.add_argument('--year', '-y', type=int, help="year of the advent-of-code challenge", required=True)
parser.add_argument('--day', '-d', type=int, help="day of the advent-of-code challenge", required=True)
parser.add_argument(
    '--inputs-path',
    '-i',
    type=str_to_dir,
    default=pathlib.Path(__file__).parent.resolve() / "../../inputs",
    help="Path to directory to store inputs"
)
parser.add_argument(
    '--solution-path',
    '-s',
    type=str_to_file,
    help="Path of file to create for the challenge's solution. If not provided, day_<day>.py will be used as default."
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
    with open(inputs_path, 'w') as fp:
        fp.write(data)

    solution_template = f"""from aocd import submit


def part_a(data):
    pass


def part_b(data):
    pass


if __name__ == "__main__":
    with open("{inputs_path}", 'r') as fp:
        data = fp.read()
    submit(part_a(data), part="a", day={args.day}, year={args.year})
    submit(part_b(data), part="b", day={args.day}, year={args.year})
"""
    default_solution_path.write_text(solution_template)

