from typing import List

"""
Creator: Przemysław Szewczak
Date: 21.12.2021
Source: https://adventofcode.com/2021/day/13
Version: 2
Note: Version 1 uses not effective algorithm and data structures. I modified that version to use
algorithm which handles fold using vector operation and # points instead of whole field with every point.
"""


class Plane:
    def __init__(self):
        self.points = []
        self.folding_data = []
        self.x_size = 0
        self.y_size = 0
        pass

    def __call__(self, *args, **kwargs):
        self._load_plane()
        self._fold()

    def __str__(self):
        return ""

    def return_last(self) -> None:
        """Return plane after last fold"""
        x_vals = [x[0] for x in self.points]
        y_vals = [y[1] for y in self.points]
        self.x_size = max(x_vals)
        self.y_size = max(y_vals)
        cols = []
        for y in range(self.y_size + 1):
            x_row = []
            for x in range(self.x_size + 1):
                if [x, y] in self.points:
                    x_row.append("#")
                else:
                    x_row.append(" ")
            cols.append(x_row)
        for col in cols:
            print("".join(col))

    def _load_plane(self) -> None:
        """
        Loads points from data file. Plane name is used but its not plane,
        this name left from previous version
        """
        with open('day_13_input_1.txt', 'r') as file:
            points = []
            for line in file:
                line = line.strip()
                if ',' in line:
                    point = line.split(',')
                    points.append(list(map(lambda x: int(x), point)))

                elif 'fold' in line:
                    self.folding_data.append(line.split('fold along ')[1])
        self.points = points
        # print(points)

    def _fold_on_x(self, val):
        """Handling folding on x axis"""
        new_points = []
        for point in self.points:
            if point[0] > val:
                new_poit = [point[0] - 2 * abs(point[0] - val), point[1]]
                if new_poit in new_points:
                    continue
                else:
                    new_points.append(new_poit)
            else:
                if point in new_points:
                    continue
                else:
                    new_points.append(point)
        self.points = new_points

    def _fold_on_y(self, val: int) -> None:
        """Handling folding on y axis"""
        new_points = []
        for point in self.points:
            if point[1] > val:
                new_poit = [point[0], point[1] - 2 * abs(point[1] - val)]
                if new_poit in new_points:
                    continue
                else:
                    new_points.append(new_poit)
            else:
                if point in new_points:
                    continue
                else:
                    new_points.append(point)
        self.points = new_points

    def _fold(self):
        """Handling fold and call private methods depends on which axis fold have to be done"""
        for fold in self.folding_data:
            axis, val = fold.split('=')
            if axis == 'x':
                self._fold_on_x(int(val))
            else:
                self._fold_on_y(int(val))


def main() -> None:
    plane = Plane()
    plane()
    # print(plane)
    plane.return_last()
    pass


if __name__ == '__main__':
    main()
