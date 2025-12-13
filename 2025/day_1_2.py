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
            # print(f"action: {d}, pos: {pos}, num_rotations: {hits}\n")
        else:
            rots = abs(next_pos) // end
            if rotation == "R" or pos == 0:
                # Example: pos = 0 and offset is R100
                # Note: Ignore case of offset R0 since we only care about clicks
                # Example: pos = 0 and offset is L5
                hits += rots
            else:
                # Example: pos = 95 and offset is L96 (pos ends at 99) or L95 (pos ends at 0)
                hits += rots + 1

            # Update position in dial
            pos = next_pos % end

            # print(f"action: {d}, pos: {pos}, num_rotations: {hits}\n")

    return hits


def main():
    input = read_file_lines("test.txt")
    result = sol(input)
    print(f"Number of zeros given sequence: {result}.")


main()


"""
# Original solution

import fileinput as fp
from typing import List


def read_file_lines(filename: str) -> List[str]:
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
            # print(f"action: {d}, pos: {pos}, num_rotations: {hits}\n")
        else:
            rots = abs(next_pos) // end
            if rotation == "R":
                # Example: pos = 0 and offset is R100
                # Note: Ignore case of offset R0 since we only care about clicks
                hits += rots
            else:
                if pos == 0:
                    # Example: pos = 0 and offset is L5
                    hits += rots
                else:
                    # Example: pos = 95 and offset is L96 (pos ends at 99) or L95 (pos ends at 0)
                    hits += rots + 1

            # Update position in dial
            pos = next_pos % end

            # print(f"action: {d}, pos: {pos}, num_rotations: {hits}\n")

    return hits


def main():
    input = read_file_lines("test.txt")
    result = sol(input)
    print(f"Number of zeros given sequence: {result}.")


main()

"""
