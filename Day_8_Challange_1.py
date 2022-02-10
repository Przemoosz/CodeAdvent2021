from typing import List

"""
Creator: Przemysław Szewczak
Date: 14.12.2021
Source: https://adventofcode.com/2021/day/8
Note: Im not proud of this code...
"""


def load_lines() -> List[str]:
    with open('day_8_input_1.txt') as file:
        return_list = [line.strip().split(" | ")[1] for line in file]
        return return_list


def search_unique(output: List[str]) -> int:
    unique_count = 0
    for line in output:
        digits = line.split(" ")
        print(digits)
        for i in digits:
            if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
                unique_count += 1
    print(unique_count)
    return unique_count


def main() -> None:
    lines = load_lines()
    search_unique(lines)
    pass


if __name__ == '__main__':
    main()
