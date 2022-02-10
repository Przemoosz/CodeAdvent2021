from typing import List

"""
Creator: Przemysław Szewczak
Date: 21.12.2021
Source: https://adventofcode.com/2021/day/13
Version: 1
Note: Version 1 uses not effective algorithm and data structures. Checkout version 2 with
much effective, and less space consuming algorithm and data structures. Version 2 is much more faster
and much easier to understand.
"""


class Plane:
    def __init__(self):
        self.cols = []
        self.rows = []
        self.folding_data = []
        self.x_size = 0
        self.y_size = 0
        self.block = False
        pass

    def __call__(self, *args, **kwargs):
        self._load_plane()
        self._fold()

    def __str__(self):
        if self.block:
            return ""
        for cols in self.cols:
            print("".join(cols))
        return ""

    def print_cols(self) -> None:
        """Printing plane using rows"""
        for col in self.rows:
            print(col)

    def _create_rows(self) -> None:
        """Method which redefine rows atribute after changes to plane had been made"""
        col = []
        for row_ind, row in enumerate(self.cols):
            # print(row)
            for col_ind, item in enumerate(row):
                # print(col_ind,'---', item)
                if row_ind == 0:
                    col.append([item])
                else:
                    col[col_ind].append(item)
        self.rows = col

    def _redefine_cols(self) -> None:
        """Method which redefine cols atribute after changes to plane had been made"""
        row = []
        for col_ind, col in enumerate(self.rows):
            # print(row)
            for row_ind, item in enumerate(col):
                # print(col_ind,'---', item)
                if col_ind == 0:
                    row.append([item])
                else:
                    row[row_ind].append(item)
        self.cols = row

    def _load_plane(self) -> None:
        """
        Load points and folding info from file, and create cartesian plane using list
        """
        with open('day_13_input_1.txt', 'r') as file:
            points = []
            for line in file:
                line = line.strip()
                if ',' in line:
                    points.append(line)
                elif 'fold' in line:
                    self.folding_data.append(line.split('fold along ')[1])
            x_vals = [int(x.split(',')[0]) for x in points]
            y_vals = [int(y.split(',')[1]) for y in points]
            self.x_size = max(x_vals)
            self.y_size = max(y_vals)
            # print(points)
            for y in range(self.y_size + 1):
                x_row = []
                for x in range(self.x_size + 1):

                    if (str(x) + "," + str(y)) in points:
                        x_row.append("#")
                    else:
                        x_row.append(" ")
                self.cols.append(x_row)

    def _fold(self) -> None:
        """Handling fold and call private methods depends on which axis fold have to be done"""
        for fold in self.folding_data:
            axis, val = fold.split('=')
            # print(axis, val)
            if axis == 'x':
                self._fold_on_x(int(val))
            else:
                self._fold_on_y(int(val))
            break
        pass

    def _fold_on_x(self, val: int) -> None:
        """Handling folding on x axis"""
        self._create_rows()
        to_fold = self.rows[val + 1:]
        to_fold.reverse()
        not_to_fold = self.rows[:val]
        for ind in range(len(not_to_fold)):
            for char_ind in range(len(not_to_fold[ind])):
                # if not_to_fold[ind][char_ind] == to_fold[ind][char_ind]:
                #     continue
                if to_fold[ind][char_ind] == "#":
                    not_to_fold[ind][char_ind] = "#"
                else:
                    continue
        self.rows = not_to_fold
        self._redefine_cols()

    def _fold_on_y(self, val: int) -> None:
        """Handling folding on x axis"""
        to_fold = self.cols[val + 1:]
        to_fold.reverse()
        not_to_fold = self.cols[:val]
        for ind in range(len(not_to_fold)):
            for char_ind in range(len(not_to_fold[ind])):
                # if not_to_fold[ind][char_ind] == to_fold[ind][char_ind]:
                #     continue
                if to_fold[ind][char_ind] == "#":
                    not_to_fold[ind][char_ind] = "#"
                else:
                    continue
        self.cols = not_to_fold
        pass

    def count_hashes(self) -> int:
        """Counting hash(#) points on plane"""
        total_hashes = 0
        for row in self.cols:
            total_hashes += row.count('#')
        return total_hashes


def main() -> None:
    plane = Plane()
    plane()
    print(plane.count_hashes())
    pass


if __name__ == '__main__':
    main()
