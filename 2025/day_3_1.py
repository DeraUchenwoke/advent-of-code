import fileinput as fp
from typing import List


def read_file_lines(filename: str) -> List[str]:
    """
    Read lines in file input.
    """
    input = []
    with fp.input(files=(filename)) as f:
        for line in f:
            input.append(line.strip("\n"))
    return input


def find_pos(char: str, bank: str) -> int:
    """
    Find position of first occurence of `char`.
    """
    for pos in range(len(bank)):
        if bank[pos] == char:
            return pos


def sol(batteries: List[str]) -> int:
    total = 0

    for bank in batteries:
        # Note: lexographically '9' > '1'
        first_char = max(
            bank[:-1]
        )  # Do not include last value incase it's a max number for `first_char`
        pos_first_char = find_pos(first_char, bank)
        second_char = max(bank[pos_first_char + 1 :])

        bank_total = int(first_char + second_char)
        # print(f"{bank_total=}, {first_char=}, {second_char=}")
        total += bank_total

    return total


def main():
    input = read_file_lines("test.txt")
    result = sol(input)
    # print(input)
    # print("=" * 50)
    print(f"Total output joltage: {result}")


main()
