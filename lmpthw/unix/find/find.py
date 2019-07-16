import argparse
import os
from pathlib import Path
from typing import List


def init_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Concatenate files.")
    dirs_group = parser.add_argument_group('Directories')
    filters_group = parser.add_argument_group('Filters')
    actions_group = parser.add_argument_group('Actions')

    dirs_group.add_argument(
        'dirs', default=".", help="search by file name"
    )

    filters_group.add_argument(
        "-n", "--name", type=str, nargs="*", help="search by file name"
    )

    filters_group.add_argument(
        "-t", "--type", type=str, nargs="+", help="search by file type"
    )

    actions_group.add_argument(
        "-p", "--print", type=bool, help="display results to console"
    )

    actions_group.add_argument(
        "-e", "--exec", help="Unix command to execute on results"
    )

    return parser.parse_args()


def find(dirname, name: str = None, type: List[str]=None, **kwargs):
    path = Path(dirname)
    contents = [x for x in path.iterdir()]
    pass



def main() -> None:
    args = init_args()
    dirs = [Path(x) for x in args.dirs]

    for dir in dirs:
        find(dir, **args)



if __name__ == "__main__":
    main()
