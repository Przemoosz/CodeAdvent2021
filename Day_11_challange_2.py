from typing import List

"""
Creator: Przemysław Szewczak
Date: 20.12.2021
Source: https://adventofcode.com/2021/day/11
"""


class Octopus:
    blinks = 0
    zeros = 0
    steps = 0

    def __init__(self, energy: int):
        self.energy_level = energy
        self.blinked = False
        self.steps = 0

    def __str__(self):
        return str(self.energy_level)

    def __call__(self, *args, **kwargs) -> bool:
        if self.blinked:
            # If octopus blinked before do nothing
            return False
        if self.energy_level + 1 > 9:
            # If energy after increment is bigger than 9 then return True as a signal, and block next blink
            self.energy_level += 1
            self.blinked = True
            Octopus.count_blinks()
            return True
        elif not self.blinked:
            # Normal case
            self.energy_level += 1
            self.steps += 1
            return False

    def deactivate(self) -> None:
        """Deactivate blockade"""
        self.blinked = False

    def reset_energy(self) -> None:
        """Reset energy level to 0"""
        self.energy_level = 0
        Octopus.count_zeros()

    @classmethod
    def count_zeros(cls) -> None:
        """Class method which adds one for every 0 on plane"""
        cls.zeros += 1
        if cls.zeros == 100:
            print(f"All zero after step: {cls.steps}")

    @classmethod
    def reset_counter(cls) -> bool:
        """Class method to reset counter or to return True while all plane is filed with 0"""
        if cls.zeros == 100:
            return True
        cls.zeros = 0

    @classmethod
    def count_blinks(cls) -> None:
        """Calculates total blinks"""
        cls.blinks += 1

    @classmethod
    def get_blinks_ammount(cls) -> int:
        return cls.blinks


class Plane:
    def __init__(self):
        self.rows = Plane.load_plane()
        self.Octopus_row = self.init_Octopus()
        self.y_size = len(self.rows) - 1
        self.x_size = len(self.rows[0]) - 1

    def __str__(self):
        for row in self.Octopus_row:
            for Octopus in row:
                print(Octopus, end="")
            print('\n', end="")
        return ""

    def step(self) -> None:
        """
        "Step" function, increment all energy by one at first then
        handles octopus with energy higher than 9
        """
        blinked = []
        blinked_Octopus = []
        for y_val, row in enumerate(self.Octopus_row):
            for x_val, Octopus in enumerate(row):
                Octopus.deactivate()
                if Octopus():
                    blinked.append(str(x_val) + str(y_val))
                    blinked_Octopus.append(Octopus)
                else:
                    pass
        self._blink_after_step(blinked)
        [i.reset_energy() for i in blinked_Octopus]
        # Handling blink after first blink
        while True:
            break_while = True
            blinked = []
            blinked_Octopus = []
            for y_val, row in enumerate(self.Octopus_row):
                for x_val, Octopus in enumerate(row):
                    if Octopus.energy_level > 9:
                        blinked.append(str(x_val) + str(y_val))
                        blinked_Octopus.append(Octopus)
                    else:
                        pass
            self._blink_after_step(blinked)
            [i.reset_energy() for i in blinked_Octopus]
            for row in self.Octopus_row:
                for Octopus in row:
                    if Octopus.energy_level > 9:
                        break_while = False
            if break_while:
                break

    def _blink_after_step(self, list_of_blinks: List[str]) -> None:
        """Private function which increment all energy around blinked octopus"""
        for cordinates in list_of_blinks:
            x, y = int(cordinates[0]), int(cordinates[1])
            # Corners case x = 0 y = 0
            if x == 0 and y == 0:
                self.Octopus_row[y][x + 1]()
                self.Octopus_row[y + 1][x + 1]()
                self.Octopus_row[y + 1][x]()
            elif x == self.x_size and y == 0:
                # Corners case x = max y = 0
                self.Octopus_row[y][x - 1]()
                self.Octopus_row[y + 1][x - 1]()
                self.Octopus_row[y + 1][x]()
            elif x == 0 and y == self.y_size:
                # Corners case x = 0 y = max
                self.Octopus_row[y][x + 1]()
                self.Octopus_row[y - 1][x + 1]()
                self.Octopus_row[y - 1][x]()
            elif x == self.x_size and y == self.y_size:
                # Corners case x = max y = max
                self.Octopus_row[y][x - 1]()
                self.Octopus_row[y - 1][x - 1]()
                self.Octopus_row[y - 1][x]()
            elif y == 0:
                # First row case
                self.Octopus_row[y][x - 1]()
                self.Octopus_row[y][x + 1]()
                self.Octopus_row[y + 1][x - 1]()
                self.Octopus_row[y + 1][x]()
                self.Octopus_row[y + 1][x + 1]()
            elif y == self.y_size:
                # Last row case
                self.Octopus_row[y][x - 1]()
                self.Octopus_row[y][x + 1]()
                self.Octopus_row[y - 1][x - 1]()
                self.Octopus_row[y - 1][x]()
                self.Octopus_row[y - 1][x + 1]()
            elif x == 0:
                # Start line Case
                self.Octopus_row[y][x + 1]()
                self.Octopus_row[y + 1][x + 1]()
                self.Octopus_row[y + 1][x]()
                self.Octopus_row[y - 1][x + 1]()
                self.Octopus_row[y - 1][x]()
            elif x == self.x_size:
                # End of line case
                self.Octopus_row[y][x - 1]()
                self.Octopus_row[y + 1][x - 1]()
                self.Octopus_row[y + 1][x]()
                self.Octopus_row[y - 1][x - 1]()
                self.Octopus_row[y - 1][x]()
            else:
                # Normal case
                self.Octopus_row[y][x - 1]()
                self.Octopus_row[y][x + 1]()
                self.Octopus_row[y - 1][x - 1]()
                self.Octopus_row[y - 1][x]()
                self.Octopus_row[y - 1][x + 1]()
                self.Octopus_row[y + 1][x - 1]()
                self.Octopus_row[y + 1][x]()
                self.Octopus_row[y + 1][x + 1]()
        pass

    def init_Octopus(self) -> List[List[Octopus]]:
        """Creating octopus"""
        rows = []
        for row in self.rows:
            row = [Octopus(int(energy)) for energy in row]
            rows.append(row)
        return rows

    @staticmethod
    def load_plane() -> List[str]:
        """Load plane from file"""
        with open('day_11_input_1.txt', 'r') as file:
            plane = [line.strip() for line in file]
        return plane


def main() -> None:
    plane = Plane()
    for i in range(1000):
        Octopus.steps = i + 1
        plane.step()
        if Octopus.reset_counter():
            break
    pass


if __name__ == '__main__':
    main()
