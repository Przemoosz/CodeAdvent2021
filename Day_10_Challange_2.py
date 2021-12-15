from typing import List

"""
Creator: Przemysław Szewczak
Date: 15.12.2021
Source: https://adventofcode.com/2021/day/10
"""


class MissingClosing:
    """This is class which handle missing ends of parenthesis"""

    def __init__(self, list_of_lines: List[str]):
        self.list_of_lines = list_of_lines
        self.points_list = []

    def __call__(self, *args, **kwargs) -> int:
        """All methods are private to not allow access from main function"""
        for line in self.list_of_lines:
            self._find_missing(line)
        return self._caluculate_result()

    def _caluculate_result(self) -> int:
        """Method to get median from list of points"""
        self.points_list.sort()
        ind = (len(self.points_list) - 1) / 2
        return self.points_list[int(ind)]

    def _find_missing(self, line: str) -> None:
        open_chars = '{[(<'
        close_chars = '>)]}'
        opening = []
        closing = []
        for char in line:
            if char in open_chars:
                opening.append(char)
            elif char in close_chars:
                closing.append(char)
                # Removing closed sequences
                if opening[-1] + char == "[]" or opening[-1] + char == "{}" or \
                        opening[-1] + char == "{}" or opening[-1] + char == "<>" or opening[-1] + char == "()":
                    opening.pop(-1)
                    closing.pop()
        else:
            # Passing to calculate result method, opening is list of parenthesis which
            # have no endings in line
            self._result_calculate(opening)

    def _result_calculate(self, opening: List[str]) -> None:
        """Calculating result using given formulas"""
        points = 0
        temp_str = ''
        opening.reverse()
        for i in opening:
            if i == '(':
                temp_str += ')'
                points = points * 5 + 1
            elif i == '[':
                temp_str += ']'
                points = points * 5 + 2
            elif i == '{':
                temp_str += '}'
                points = points * 5 + 3
            elif i == '<':
                temp_str += '>'
                points = points * 5 + 4
        self.points_list.append(points)


def load_data() -> List[str]:
    """Function loads data from txt file and saves it to list"""
    with open('day_10_input_1.txt') as file:
        return_list = [line.strip() for line in file]
    return return_list


def corrupted_func(line: str) -> bool:
    """Function used to search corrupted lines"""
    open_chars = '{[(<'
    close_chars = '>)]}'
    opening = []
    closing = []
    for char in line:
        if char in open_chars:
            opening.append(char)
        elif char in close_chars:
            closing.append(char)
            # Checking if new close char is connected with previous open char
            if opening[-1] + char == "[]" or opening[-1] + char == "{}" or \
                    opening[-1] + char == "{}" or opening[-1] + char == "<>" or opening[-1] + char == "()":
                # If yes then function remove this char from end of open list
                opening.pop(-1)
            else:
                # If line is corrupted then return False
                return False
    else:
        return True


def main() -> None:
    lines = load_data()
    to_remove = []
    for line in lines:
        result = corrupted_func(line)
        if not result:
            to_remove.append(line)
    [lines.remove(i) for i in to_remove]
    missing = MissingClosing(lines)
    print(missing())
    return None


if __name__ == '__main__':
    main()
