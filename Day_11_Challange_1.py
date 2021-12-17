from typing import List


class Octupus:
    def __init__(self, energy: int):
        self.energy_level = energy
        self.blinked = False

    def __str__(self):
        return str(self.energy_level)

    def __call__(self, *args, **kwargs) -> bool:
        if self.blinked:
            return False
        if self.energy_level + 1 > 9:
            self.energy_level = 0
            self.blinked = True
            return True
        elif not self.blinked:
            self.energy_level += 1
            return False

    def deactivate(self) -> None:
        self.blinked = False


class Plane:
    def __init__(self):
        self.rows = Plane.load_plane()
        self.octupus_row = self.init_octupus()
        self.y_size = len(self.rows) - 1
        self.x_size = len(self.rows[0]) - 1

    def __str__(self):
        for row in self.octupus_row:
            for octupus in row:
                print(octupus, end="")
            print('\n', end="")
        return ""

    def step(self) -> None:

        blinked = []
        for y_val, row in enumerate(self.octupus_row):
            for x_val, octupus in enumerate(row):
                octupus.deactivate()
                if octupus():
                    blinked.append(str(x_val) + str(y_val))
                else:
                    pass
        print(blinked)
        self._blink_after_step(blinked)
        print("Checking if any octupus have energy greater than 9")
        break_while = True
        while True:
            break_while = True
            for y_val, row in enumerate(self.octupus_row):
                for x_val, octupus in enumerate(row):
                    if octupus.energy_level > 9:
                        print("UUUU dude i found one")
                        print([str(x_val) + str(y_val)])
                        octupus()

                        self._blink_after_step([str(x_val) + str(y_val)])

            for row in self.octupus_row:
                for octupus in row:
                    if octupus.energy_level > 9:
                        print("++++++++++++++++++++++++++++++++++++++++")
                        break_while = False
            if break_while:
                break


    def _blink_after_step(self, list_of_blinks: List[str]) -> None:
        for cordinates in list_of_blinks:
            x, y = int(cordinates[0]), int(cordinates[1])
            # Corners case x = 0 y = 0
            if x == 0 and y == 0:
                self.octupus_row[y][x + 1]()
                self.octupus_row[y + 1][x + 1]()
                self.octupus_row[y + 1][x]()
            elif x == self.x_size and y == 0:
                # Corners case x = max y = 0
                print("Here")
                self.octupus_row[y][x - 1]()
                self.octupus_row[y + 1][x - 1]()
                self.octupus_row[y + 1][x]()
            elif x == 0 and y == self.y_size:
                # Corners case x = 0 y = max
                print("Here")
                self.octupus_row[y][x + 1]()
                self.octupus_row[y - 1][x + 1]()
                self.octupus_row[y - 1][x]()
            elif x == self.x_size and y == self.y_size:
                # Corners case x = max y = max
                print("Here")
                self.octupus_row[y][x - 1]()
                self.octupus_row[y - 1][x - 1]()
                self.octupus_row[y - 1][x]()
            elif y == 0:
                # First row case
                print(f"First line case ({x},{y})")
                self.octupus_row[y][x - 1]()
                self.octupus_row[y][x + 1]()
                self.octupus_row[y + 1][x - 1]()
                self.octupus_row[y + 1][x]()
                self.octupus_row[y + 1][x + 1]()
            elif y == self.y_size:
                # Last row case
                self.octupus_row[y][x - 1]()
                self.octupus_row[y][x + 1]()
                self.octupus_row[y - 1][x - 1]()
                self.octupus_row[y - 1][x]()
                self.octupus_row[y - 1][x + 1]()
            elif x == 0:
                self.octupus_row[y][x + 1]()
                self.octupus_row[y + 1][x + 1]()
                self.octupus_row[y + 1][x]()
                self.octupus_row[y - 1][x - 1]()
                self.octupus_row[y - 1][x]()
            elif x == self.x_size:
                self.octupus_row[y][x - 1]()
                self.octupus_row[y + 1][x - 1]()
                self.octupus_row[y + 1][x]()
                self.octupus_row[y - 1][x - 1]()
                self.octupus_row[y - 1][x]()
            else:
                # Normal case
                self.octupus_row[y][x - 1]()
                self.octupus_row[y][x + 1]()
                self.octupus_row[y - 1][x - 1]()
                self.octupus_row[y - 1][x]()
                self.octupus_row[y - 1][x + 1]()
                self.octupus_row[y + 1][x - 1]()
                self.octupus_row[y + 1][x]()
                self.octupus_row[y + 1][x + 1]()
        pass

    def init_octupus(self) -> List[List[Octupus]]:
        rows = []
        for row in self.rows:
            row = [Octupus(int(energy)) for energy in row]
            rows.append(row)
        return rows
        pass

    @staticmethod
    def load_plane() -> List[str]:
        with open('test_input.txt', 'r') as file:
            plane = [line.strip() for line in file]
        return plane


def main() -> None:
    plane = Plane()
    # plane.rows
    # print(plane)
    print("Starting state:")
    print(plane)

    print("After step 1:")
    plane.step()
    print(plane)
    print("After step 2:")
    plane.step()
    print(plane)

    pass


if __name__ == '__main__':
    main()
