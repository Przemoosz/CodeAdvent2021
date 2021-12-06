from collections import namedtuple


class Submarine:
    def __init__(self):
        self.x_postion = 0
        self.y_postion = 0

    def __add__(self, other):
        self.x_postion = self.x_postion + other[0]
        self.y_postion = self.y_postion + other[1]

    def __str__(self):
        return f'Submarine Possition [x: {self.x_postion}, y: {self.y_postion}]'

    def postion_multiply(self) -> int:
        return self.x_postion * self.y_postion


def main() -> None:
    ubot = Submarine()
    with open('day_2_input_1.txt', 'r') as file:
        for line in file:
            vector = [0, 0]
            line = line.strip().split(' ')
            if 'forward' in line[0]:
                vector[0] = int(line[1])
            elif 'down' in line[0]:
                vector[1] = int(line[1])
            elif 'up' in line[0]:
                vector[1] = int(line[1]) * (-1)
            ubot + vector
            print(ubot)

    print(ubot.postion_multiply())
    pass


if __name__ == '__main__':
    main()
