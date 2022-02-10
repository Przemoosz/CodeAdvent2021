from typing import List

"""
Creator: Przemysław Szewczak
Date: 06.12.2021
Source: https://adventofcode.com/2021/day/4
"""


class Board:
    finished = 0

    # TODO
    # Stworzyc nazwe, metode klasowa liczaca skonczone bordy
    # potem zobaczyc ktore sie skonczyły a ktore ni prawdopodobnie jeden jest dwa razy konczony ale nie zwraca True
    # albo przerobic algorytm liczacy puste pola ponownie
    def __init__(self, row_list: List[List[int]]):
        self.rows = []
        self.val = None
        self.finished = False
        [self.rows.append(i) for i in row_list]
        self.columns = [[], [], [], [], []]
        for row in self.rows:
            for ind, val in enumerate(row):
                self.columns[ind].append(val)

    def __str__(self):
        return_string = f'{self.rows[0]}\n' \
                        f'{self.rows[1]}\n' \
                        f'{self.rows[2]}\n' \
                        f'{self.rows[3]}\n' \
                        f'{self.rows[4]}'
        # eturn_string = f'{self.columns}'
        return return_string

    def bingo_check(self, drawn_numbers: List[int]) -> bool:
        """
        Checking if typed numbers for a Bingo.
        If yes returning True and printing sum of unmarked numbers times last drawn number
        If no returning False, and another board is checking.
        """
        bingo_value=[]
        bingo_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in drawn_numbers:
            if i in self.rows[0]:
                bingo_value[0] += 1

            if i in self.rows[1]:
                bingo_value[1] += 1

            if i in self.rows[2]:
                bingo_value[2] += 1

            if i in self.rows[3]:
                bingo_value[3] += 1

            if i in self.rows[4]:
                bingo_value[4] += 1

            if i in self.columns[0]:
                bingo_value[5] += 1

            if i in self.columns[1]:
                bingo_value[6] += 1

            if i in self.columns[2]:
                bingo_value[7] += 1

            if i in self.columns[3]:
                bingo_value[8] += 1

            if i in self.columns[4]:
                bingo_value[9] += 1

        #print(bingo_value)
        for i in bingo_value:
            if i >= 5:
                self.finished = True
                Board.add_finished()
                self.sum_not_typed(drawn_numbers)
                return True
            else:
                continue
        return False
    def sum_not_typed(self, drawn_numbers: List[int]) -> int:
        """Method summing and returning value if Bingo occurred"""
        sum_not = 0
        for row in self.rows:
            for val in row:
                if val not in drawn_numbers:
                    sum_not += val
        self.val = sum_not * drawn_numbers[-1]
        return sum_not * drawn_numbers[-1]


    @classmethod
    def add_finished(cls) -> None:
        cls.finished += 1
        pass

    @classmethod
    def class_info(cls) -> None:
        #print(f"Total finished: {cls.finished}")
        return cls.finished


class DrawnNumbers:
    """Class for numbers that will return numbers which takes part in Bingo game"""

    def __init__(self):
        """Saving all available numbers to one variable then, taking first 5 to drawn number variable"""
        with open('day_4_input_1.txt', 'r') as file:
            self.available_numbers = file.readline().strip().split(',')
        self.drawn_numbers = list(map(lambda x: int(x), self.available_numbers[:5]))
        self.available_numbers = self.available_numbers[5:]

    def __str__(self):
        return_string = f'Drawn numbers: {self.drawn_numbers}\n' \
                        f'Available numbers: {self.available_numbers}'
        return return_string

    def get_drawn_numbers(self) -> List[int]:
        return self.drawn_numbers

    def draw_next(self) -> List:
        self.drawn_numbers.append(int(self.available_numbers[0]))
        self.available_numbers = self.available_numbers[1:]
        return self.drawn_numbers


def create_boards() -> List[Board]:
    board_list = []
    with open('day_4_input_1.txt', 'r') as file:
        """Skipping first 2 lines - number drawn and gap line"""
        [file.readline() for _ in range(2)]
        board_rows = []
        for line in file:

            board_rows.append(line.strip().split(' '))
            if len(board_rows) == 5:
                """Skipping gap line, removing '' from rows, creating Board object,
                 saving them and preparing list for another board"""
                file.readline()
                # Here will be object creation
                for i in board_rows:
                    if '' in i:
                        i.remove('')
                    if '' in i:
                        i.remove('')
                    if '' in i:
                        i.remove('')
                rows_to_save = []
                """ Changing type from str to integer type """
                [rows_to_save.append(list(map(lambda x: int(x), i))) for i in board_rows]
                board_list.append(Board(rows_to_save))

                board_rows = []
                continue
        return board_list


def main() -> None:
    # should return 17408
    """ Creating, and handling drawn numbers and available boards."""
    numbers = DrawnNumbers()
    drawn = numbers.get_drawn_numbers()
    boards = create_boards()

    while True:
        if len(boards) == 1:
            break_while = True
            while not boards[0].finished:
                boards[0].bingo_check(drawn)
                numbers.draw_next()
                drawn = numbers.get_drawn_numbers()
                #print(boards[0].val)
            return boards[0].val
        finish = []
        for i in boards:
            i.bingo_check(drawn)
            if i.finished:
                finish.append(i)
        [boards.remove(i) for i in finish]
        numbers.draw_next()
        drawn = numbers.get_drawn_numbers()

if __name__ == '__main__':
    print(f'Last bingo result {main()}')
