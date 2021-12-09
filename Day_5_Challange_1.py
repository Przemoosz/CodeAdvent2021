from typing import List


class CartesianPlane:
    def __init__(self):
        self.x_size, self.y_size = 1000, 1000
        self.plane = []
        for _ in range(self.x_size):
            row =[]
            self.plane.append([row.append(0) for _ in range(1000)])
    def __str__(self):
        return_str = ""
        for ind,row in enumerate(self.plane):
            return_str += f'{ind} - {row}\n'
        return return_str
    def add_straigh_line(self, line: List[int]) -> None:
        if line[0] == line[2]:
            static_x = line[0]
            static_y = False
        elif line[1] == line[3]:
            static_y = line[1]
            static_x = False

        pass


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
    # Passed, not used
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


def main() -> None:
    available_lines = load_lines()
    straight_lines(available_lines)
    plane = CartesianPlane()
    print(plane)
    # size = plane_size(available_lines)
    pass


if __name__ == '__main__':
    main()
