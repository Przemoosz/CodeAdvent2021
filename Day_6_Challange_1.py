from typing import List

"""
Creator: Przemysław Szewczak
Date: 10.12.2021
Source: https://adventofcode.com/2021/day/6
Note: Its better to use algorithm from challenge 2, it is more effective,
and don't load CPU so heavily like this one
"""


class LanternFish:
    def __init__(self, days: int):
        self.starting_days = days
        self.days = days
        self.life_status = True

    def __str__(self):
        return f"Days left {self.days}"

    def next_day(self) -> None:
        self.days -= 1

    def die(self):
        if self.days == 0:
            self.life_status = False
            return LanternFish(6)
        else:
            return None


def load_lanternfish() -> List[int]:
    # Passed
    with open('day_6_input_1.txt', 'r') as file:
        line = file.readline().strip().split(',')
        line = list(map(lambda x: int(x), line))
        print(line)
    return line


def main() -> None:
    starting_list = load_lanternfish()
    lantern_fish_list = []

    for i in starting_list:
        lantern_fish_list.append(LanternFish(i))
    # [print(i) for i in lantern_fish_list]
    for _ in range(81):
        # print(f"Day - {_}")
        # [print(i) for i in lantern_fish_list]
        new_fish = []
        fish_to_remove = []
        for fish in lantern_fish_list:
            if isinstance(fish.die(), LanternFish):
                # print("here")
                new_fish.append(fish.die())
                fish_to_remove.append(fish)
        fish_after_day = len(lantern_fish_list)
        for fish in fish_to_remove:
            lantern_fish_list.remove(fish)
        for fish in lantern_fish_list:
            fish.next_day()
        if len(new_fish) != 0:
            for i in new_fish:
                lantern_fish_list.append(i)
                lantern_fish_list.append(LanternFish(8))
        print(f"Day {_}")
    print(fish_after_day)


if __name__ == '__main__':
    main()
