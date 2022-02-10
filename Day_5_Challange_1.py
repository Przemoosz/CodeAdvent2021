from typing import List, Dict
from math import sqrt

"""
Creator: Przemysław Szewczak
Date: 10.12.2021
Source: https://adventofcode.com/2021/day/5
"""


class CartesianPlane:
    def __init__(self):
        self.x_size, self.y_size = 1000, 1000
        self.plane = {}

    def get_plane(self) -> Dict:
        """Method returning plane"""
        print(self.plane)
        return self.plane

    def add_straigh_line(self, line: List[int]) -> None:
        """Adding lines to cartesian plane"""
        # Checking if x or y value is changing
        if line[0] == line[2]:
            static_x = line[0]
            static_y = False
        elif line[1] == line[3]:
            static_y = line[1]
            static_x = False

        if isinstance(static_x, int) and not static_y:
            # If x changes and y is static
            negative = False
            distance = line[3] - line[1]
            # if distance is negative - vector directed in x=0 value, activating negative variable
            if distance < 0:
                negative = True
            if negative:
                for y in range(distance * (-1) + 1):
                    pos = f'{static_x},{line[1] + y * (-1)}'

                    if pos in self.plane:
                        self.plane[pos] += 1
                    else:
                        self.plane.setdefault(pos, 1)
            else:
                for y in range(distance + 1):

                    pos = f'{static_x},{line[1] + y}'
                    if pos in self.plane:
                        self.plane[pos] += 1
                    else:
                        self.plane.setdefault(pos, 1)



        elif isinstance(static_y, int) and not static_x:
            # If y changes and x is static
            negative = False
            distance = line[2] - line[0]
            # if distance is negative - vector directed in y=0 value, activating negative variable
            if distance < 0:
                negative = True

            if negative:
                for x in range(distance * (-1) + 1):
                    pos = f'{line[0] + x * (-1)},{static_y}'
                    if pos in self.plane:
                        self.plane[pos] += 1
                    else:
                        self.plane.setdefault(pos, 1)
            else:
                for x in range(distance + 1):
                    pos = f'{line[0] + x},{static_y}'
                    if pos in self.plane:
                        self.plane[pos] += 1
                    else:
                        self.plane.setdefault(pos, 1)
        else:
            raise Exception


def straight_lines(lines: List[List[str]]) -> List[List[int]]:
    # Passed

    """Returning only straight lines"""
    straight_lines_list = []
    for line in lines:
        line = list(map(lambda x: int(x), line))
        if line[0] == line[2] or line[1] == line[3]:
            straight_lines_list.append(line)

    return straight_lines_list


def plane_size(lines: List[List[str]]) -> List[int]:
    # Passed, not used, typed 1000x1000 plane directly
    rows = []
    cols = []
    for line in lines:
        line = list(map(lambda x: int(x), line))
        rows.append(line[0])
        rows.append(line[2])
        cols.append(line[1])
        cols.append(line[3])
    rows.sort(reverse=True)
    cols.sort(reverse=True)
    return [rows[0], cols[0]]


def load_lines() -> List[List[str]]:
    # Passed
    """Spliting lines to gets cordinates"""
    with open('day_5_input_1.txt', 'r') as file:
        available_lines = []
        for line in file:
            formated_lines = line.strip().split(' -> ')
            splited_lines = []
            [splited_lines.append(i.split(',')) for i in formated_lines]
            line_to_save = [*splited_lines[0], *splited_lines[1]]
            available_lines.append(line_to_save)
    return available_lines


def main() -> int:
    available_lines = load_lines()
    lines = straight_lines(available_lines)
    plane = CartesianPlane()
    for line in lines:
        plane.add_straigh_line(line)
    cartesian_plane = plane.get_plane().values()
    cartesian_plane = list(cartesian_plane)
    crosses = 0
    for point in cartesian_plane:
        if point >= 2:
            crosses += 1
    print(crosses)

    return crosses


if __name__ == '__main__':
    main()
