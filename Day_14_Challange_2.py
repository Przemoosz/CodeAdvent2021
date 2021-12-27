from typing import List

"""
Creator: Przemysław Szewczak
Date: 27.12.2021
Source: https://adventofcode.com/2021/day/14
Language: Python 3.9
"""


class Polymers:

    def __init__(self):
        self.polymer = ""
        self.polymer_template = {}
        self.pairs = {}
        self._load_data()
        self._create_first_pairs()

    def __call__(self, *args, **kwargs) -> None:
        for _ in range(40):
            self._create_pairs()
        pass

    def __str__(self):
        """Not used in challange 2"""
        print(self.polymer)
        [print(f"{k} - {v}") for k, v in self.polymer_template.items()]
        return ''

    def _load_data(self) -> None:
        """Private load data from file method used in __init__"""
        with open('test_input.txt', 'r') as file:
            self.polymer = file.readline().strip()
            file.readline()
            for line in file:
                k, v = line.strip().split(' -> ')
                self.polymer_template[k] = v
        return None

    def _create_first_pairs(self) -> None:
        """Init creation first set of paris"""
        for starting_ind in range(int(len(self.polymer) - 1)):
            pair = (self.polymer[starting_ind] + self.polymer[(starting_ind + 1)])
            if pair in self.pairs:
                self.pairs[pair] += 1
            else:
                self.pairs[pair] = 1

    def _create_pairs(self) -> None:
        """Create pairs and add them to pair dictionary, removing previous pairs"""
        pair_keys = self.pairs.keys()
        to_add = {}
        for pair in pair_keys:
            first_new_pair = pair[0] + self.polymer_template[pair]
            second_new_pair = self.polymer_template[pair] + pair[1]
            if first_new_pair in to_add.keys():
                to_add[first_new_pair] += self.pairs[pair]
            else:
                to_add[first_new_pair] = self.pairs[pair]
            if second_new_pair in to_add.keys():
                to_add[second_new_pair] += self.pairs[pair]
            else:
                to_add[second_new_pair] = self.pairs[pair]
            if pair in to_add.keys():
                to_add[pair] -= self.pairs[pair]
            else:
                to_add[pair] = (self.pairs[pair]) * (-1)
        for k, v in to_add.items():
            if k in self.pairs.keys():
                self.pairs[k] += v
            else:
                self.pairs[k] = v
            if self.pairs[k] == 0:
                del (self.pairs[k])
        return None

    def _count_letters(self) -> List[int]:
        """Counting letters private method"""
        letters = {}
        for pair in self.pairs:
            if pair[0] in letters:
                letters[pair[0]] += self.pairs[pair]
            else:
                letters[pair[0]] = self.pairs[pair]
        letters[self.polymer[-1]] += 1
        # print(self.pairs)
        return [max(letters.values()), min(letters.values())]

    def return_answer(self) -> int:
        """Answer return method"""
        numbers = self._count_letters()
        return numbers[0] - numbers[1]


def main() -> None:
    polymer = Polymers()
    polymer()
    print(f"Solution is: {polymer.return_answer()}")
    return None


if __name__ == '__main__':
    main()
