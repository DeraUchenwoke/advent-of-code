import fileinput as fp
from collections import Counter
from typing import List


def read_file_lines(filename: str) -> List[str]:
    """
    Read lines in file input.
    Comma-delimited.
    """
    input = []
    with fp.input(files=(filename), encoding="utf-8") as f:
        for line in f:
            input = line.split(sep=",")
    return input


def invalid_substr(w: int, s: str) -> bool:
    # w = window, s = string
    size = len(s)
    cnt = Counter()

    if size % w != 0:
        # Example: 2121212118
        # We only want to search window sizes where there are no 'leftovers'
        # since len(leftovers) != window size so cannot be a repeat occurence
        return False

    # Slide through with step of w so there are no overlaps
    for i in range(0, size - w + 1, w):
        substr = s[i : i + w]
        cnt[substr] += 1

    valid_cnt_sz = len(cnt) == 1
    # print(f"{cnt=}")
    for key, value in cnt.items():
        if valid_cnt_sz and value > 1:
            # For a string that consist entirely of the same substring
            # the size of `cnt` should be 1
            # Also the key count must be > 1
            # print(f"{key=}")
            return True
    return False


def sol(ids: List[str]) -> int:
    total = 0

    for id_range in ids:
        start, end = id_range.split(sep="-")
        x, y = int(start), int(end)
        # print(f"{x=},{y=}")

        for raw_id in range(x, y + 1):
            id = str(raw_id)  # Might be unnecessary best to optimise
            sz = len(id)

            for i in range(1, sz + 1):
                window = i
                if invalid_substr(w=window, s=id):
                    # Early return if string is only comprised of repeating substring
                    # print(f"{raw_id=}")
                    total += raw_id
                    break

        # print(f"{total=}")
        # print("=" * 50)
    return total


def main():
    input = read_file_lines("test.txt")
    result = sol(input)
    print(f"Number of invalid ids: {result}")


main()
