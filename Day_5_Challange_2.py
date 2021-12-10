from typing import List, Dict

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
        return self.plane

    def add_straigh_line(self, line: List[int]) -> None:
        """Adding straight lines to cartesian plane"""
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

    def add_diagonal_line(self, line: List[int]) -> None:
        """Adding diagonal lines to cartesian plane"""
        x_delta = line[2] - line[0]
        y_delta = line[3] - line[1]
        if abs(x_delta) != abs(y_delta):
            raise ValueError
        """
        Tangent value determines if this line is increasing y value or decreasing
        tangent = -1 - decrease
        tangent = 1 - increase
        This is abstract if we have x_point2 > x_point2, but i consider tan(alfa) looking from (0,0) point
        """
        tangent = int(y_delta / abs(x_delta))
        if tangent > 0 and x_delta > 0:
            for vector in range(x_delta + 1):
                pos = f"{line[0] + vector},{line[1] + vector}"
                if pos in self.plane:
                    self.plane[pos] += 1
                else:
                    self.plane.setdefault(pos, 1)
            return None

        elif tangent > 0 and x_delta < 0:
            for vector in range(abs(x_delta) + 1):
                pos = f"{line[0] - vector},{line[1] + vector}"
                if pos in self.plane:
                    self.plane[pos] += 1
                else:
                    self.plane.setdefault(pos, 1)
            return None

        elif tangent < 0 and x_delta < 0:
            for vector in range(abs(x_delta) + 1):
                pos = f"{line[0] - vector},{line[1] - vector}"
                if pos in self.plane:
                    self.plane[pos] += 1
                else:
                    self.plane.setdefault(pos, 1)
            return None

        elif tangent < 0 and x_delta > 0:
            for vector in range(x_delta + 1):
                pos = f"{line[0] + vector},{line[1] - vector}"
                if pos in self.plane:
                    self.plane[pos] += 1
                else:
                    self.plane.setdefault(pos, 1)
            return None


def straight_lines(lines: List[List[str]]) -> List[List[int]]:
    # Passed

    """Returning only straight lines"""
    straight_lines_list = []
    for line in lines:
        line = list(map(lambda x: int(x), line))
        if line[0] == line[2] or line[1] == line[3]:
            straight_lines_list.append(line)

    return straight_lines_list


def diagonal_lines(lines: List[List[str]]) -> List[List[int]]:
    # Passed
    """Returning only diagonal lines"""
    diagonal_lines_list = []
    for line in lines:
        # Change to integer type
        line = list(map(lambda x: int(x), line))
        # Considering only lines where tangent(alfa) = 1 or -1 where tangent(alfa) = y/x
        if abs(line[0] - line[2]) == abs(line[1] - line[3]):
            diagonal_lines_list.append(line)

    return diagonal_lines_list


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
    s_lines = straight_lines(available_lines)
    d_lines = diagonal_lines(available_lines)
    plane = CartesianPlane()
    [plane.add_straigh_line(line) for line in s_lines]
    [plane.add_diagonal_line(line) for line in d_lines]
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
