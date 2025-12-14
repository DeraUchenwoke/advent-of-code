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
    if w < 2:
        # Ignore window size < 2
        return True

    size = len(s)
    cnt = Counter()
    # Slide through with step of w so there are no overlaps
    for i in range(size - w + 1, w):
        substr = s[i : i + w]
        cnt[substr] += 1
    for _, value in cnt.items():
        if value > 1:
            return False
    return True


def sol(ids: List[str]) -> int:
    total = 0

    for id_range in ids:
        start, end = id_range.split(sep="-")
        x, y = int(start), int(end)
        # print(f"{x=},{y=}")

        for raw_id in range(x, y + 1):
            id = str(raw_id)  # Might be unnecessary best to optimise
            sz = len(id)
            front, back = id[: sz // 2], id[sz // 2 :]
            invalid = True

            if front == back:
                # Create function where as `sz` increases up to `sz // 2`
                # return False if there exists a substring which occurs more than once
                for i in range(len(front)):
                    window = i + 1
                    # print(f"{window=}, {front=}")
                    if not invalid_substr(w=window, s=front):
                        invalid = False
                if invalid:
                    # print(f"{raw_id=}")
                    total += raw_id

        # print(f"{total=}")
        # print("=" * 50)
    return total


def main():
    input = read_file_lines("test.txt")
    result = sol(input)
    print(f"Number of invalid ids: {result}")


main()
