import fileinput as fp
from typing import List


def read_file_lines(filename: str) -> List[str]:
    """
    Read lines in file input.
    """
    input = []
    with fp.input(files=(filename), encoding="utf-8") as f:
        for line in f:
            input.append(line.strip("\n"))
    return input


def max_found(subset: List[str], start: int, end: int) -> tuple[str, int]:
    max_val = "0"  # Initialise with least possible value
    updated_start = start
    for i in range(start, end + 1):
        if subset[i] > max_val:
            max_val = subset[i]
            updated_start = i + 1
    return max_val, updated_start


def sol(batteries: List[str]) -> int:
    max_joltage = 0
    for battery in batteries:
        sz = len(battery)
        if sz < 12:
            return 0

        # Start and end of search range window
        start = 0
        end = sz - 12

        # Store characters to join later
        total_joltage = 12 * [""]

        i = 0
        while i < 12 and start <= end + 1 < len(battery):
            # Update end window,
            # start window is already updated in `max_found` function.
            end = sz - 12 + i

            max_val, start = max_found(battery, start, end)

            total_joltage[i] = max_val

            i += 1
        max_joltage += int("".join(total_joltage))

    return max_joltage


def main():
    input = read_file_lines("test.txt")
    result = sol(input)
    print(f"Joltage: {result}")


main()
