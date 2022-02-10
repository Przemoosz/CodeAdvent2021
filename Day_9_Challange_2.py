from typing import List

"""
Creator: Przemysław Szewczak
Date: 14.12.2021
Source: https://adventofcode.com/2021/day/8
"""


class Plane:
    def __init__(self):
        self.plane_rows = Plane.load_rows()
        self.plane_x_len = len(self.plane_rows[0])
        self.plane_y_len = len(self.plane_rows)
        self.heat = 0
        # print(self.plane_x_len)
        # self.heat = self.heat + v + 1

    def __str__(self):
        print(self.plane_rows)
        return " "

    def __call__(self, *args, **kwargs):
        for i, v in enumerate(self.plane_rows):
            if i == 0 or i == self.plane_y_len - 1:
                self.check_corners(v, i)
                self.check_edges(v, i)
            else:
                self.check_inside(v, i)
    @staticmethod
    def load_rows() -> List[str]:
        rows = []
        with open('day_9_input_1.txt') as file:
            for line in file:
                rows.append(line.strip())
        return rows

    def check_corners(self, row: str, row_index: int) -> None:
        for i, v in enumerate(row):
            v = int(v)
            if v == 9:
                continue
            if i == 0 and row_index == 0 and v < int(row[i + 1]) and v < int(self.plane_rows[row_index + 1][0]):
                self.heat = self.heat + v + 1
            elif i == self.plane_x_len - 1 and row_index == 0 and v < int(row[i - 1]) and v < int(
                    self.plane_rows[row_index + 1][-1]):
                self.heat = self.heat + v + 1
            elif i == 0 and row_index == self.plane_y_len - 1 and v < int(row[i + 1]) and v < int(
                    self.plane_rows[row_index - 1][0]):
                self.heat = self.heat + v + 1
            elif i == self.plane_x_len - 1 and row_index == self.plane_y_len - 1 and v < int(row[i - 1]) and v < int(
                    self.plane_rows[row_index - 1][-1]):
                self.heat = self.heat + v + 1

    def check_edges(self, row: str, row_index: int) -> None:
        for i, v in enumerate(row):
            v = int(v)
            if i == 0 or i == self.plane_x_len - 1:
                continue
            if row_index == 0 and v < int(row[i - 1]) and v < int(row[i + 1]) and v < int(
                    self.plane_rows[row_index + 1][i]):
                self.heat = self.heat + v + 1
            elif row_index == self.plane_y_len - 1 and v < int(row[i - 1]) and v < int(row[i + 1]) and \
                    v < int(self.plane_rows[row_index - 1][i]):
                self.heat = self.heat + v + 1

    def check_inside(self, row: str, row_index: int) -> None:
        for i, v in enumerate(row):
            v = int(v)
            if i == 0 and v < int(row[i + 1]) and v < int(self.plane_rows[row_index - 1][0]) \
                    and v < int(self.plane_rows[row_index + 1][0]):
                self.heat = self.heat + v + 1
                continue
            elif i == self.plane_x_len - 1 and v < int(row[i - 1]) and v < int(self.plane_rows[row_index - 1][-1]) \
                    and v < int(self.plane_rows[row_index + 1][-1]):
                self.heat = self.heat + v + 1
                continue
            else:
                if i != self.plane_x_len - 1 and v < int(row[i - 1]) and v < int(row[i + 1]) \
                        and v < int(self.plane_rows[row_index - 1][i]) and v < int(self.plane_rows[row_index + 1][i]):
                    self.heat = self.heat + v + 1
        pass


def main() -> None:
    plane = Plane()
    plane()
    print(plane.heat)
    pass


if __name__ == '__main__':
    main()
