import argparse
from typing import List


def init_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Concatenate files.")

    parser.add_argument(
        "files", type=str, nargs="+", help="an integer for the accumulator"
    )

    return parser.parse_args()


def get_file_list() -> List[str]:
    return init_args().files


def get_text_from_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def concat_files(files: List[str]) -> str:
    return "".join([get_text_from_file(file) for file in files])


def main() -> None:
    files = get_file_list()
    combined_text = concat_files(files)
    print(combined_text)


if __name__ == "__main__":
    main()
