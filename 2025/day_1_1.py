import fileinput as fp
from typing import List


def read_file_lines(filename: str) -> List[str]:
    """
    Read lines in file input.
    """
    input = []
    with fp.input(files=(filename), encoding="utf-8") as f:
        for line in f:
            input.append(line)
    return input


def sol(dir: List[str]) -> int:
    pos = 50
    end = 100
    hits = 0

    for d in dir:
        rotation = d[0]
        amount = int(d[1:])
        offset = amount if rotation == "R" else -1 * amount
        next_pos = pos + offset

        if 0 < next_pos <= 99:
            pos += offset
        else:
            # Update position in dial
            pos = next_pos % end
        if pos == 0:
            hits += 1

    return hits


def main():
    input = read_file_lines("test.txt")
    result = sol(input)
    print(f"Number of zeros given sequence: {result}.")


main()
