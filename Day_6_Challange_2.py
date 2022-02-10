from typing import List
from collections import deque

"""
Creator: Przemysław Szewczak
Date: 10.12.2021
Source: https://adventofcode.com/2021/day/6
"""


def load_lanternfish() -> List[int]:
    """Simple load and transform from str to int type function"""
    with open('day_6_input_1.txt', 'r') as file:
        line = file.readline().strip().split(',')
        line = list(map(lambda x: int(x), line))
    return line


def deque_by_days(list_of_fish: List[int]) -> deque[int]:
    """Using double ended list for list which each index is day to gone by lanternfish"""
    deque_days = deque([0, 0, 0, 0, 0, 0, 0, 0, 0], 9)
    for fish in list_of_fish:
        deque_days[fish] += 1
    return deque_days


def main() -> int:
    """After each day pops left number, then add it to 6 day and append to the end of deque (day 8)"""
    list_of_all_fish = load_lanternfish()
    deque_days = deque_by_days(list_of_all_fish)
    for days in range(2):
        poped_fish = deque_days.popleft()
        deque_days[6] += poped_fish
        deque_days.append(poped_fish)
        print(deque_days)
    print(sum(deque_days))
    return sum(deque_days)


if __name__ == '__main__':
    main()
