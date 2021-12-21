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

    def __str__(self):
        if self.block:
            return ""
        for cols in self.cols:
            print("".join(cols))
        return ""

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
        """Handling folding on x axis"""
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

    def points_after_one_fold(self):
        """Handling one fold and call private methods depends on which axis fold have to be done"""
        for fold in self.folding_data:
            axis, val = fold.split('=')
            if axis == 'x':
                self._fold_on_x(int(val))
            else:
                self._fold_on_y(int(val))
            break
        return len(self.points)


def main() -> None:
    plane = Plane()
    plane()
    print(plane.points_after_one_fold())
    pass


if __name__ == '__main__':
    main()
