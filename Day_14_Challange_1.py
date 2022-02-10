from typing import List
from collections import deque

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
        self._load_data()
        self.pairs = deque()

    def __call__(self, *args, **kwargs):
        for _ in range(20):
            self._create_pairs()
            self._pair_insertion()

        pass

    def __str__(self):
        print(self.polymer)
        [print(f"{k} - {v}") for k, v in self.polymer_template.items()]
        return ''

    def _load_data(self) -> None:
        """Private load data from file method used in __init__"""
        with open('day_14_input_1.txt', 'r') as file:
            self.polymer = file.readline().strip()
            file.readline()
            for line in file:
                k, v = line.strip().split(' -> ')
                self.polymer_template[k] = v
        return None

    def _create_pairs(self) -> None:
        for starting_ind in range(int(len(self.polymer)-1)):
            self.pairs.append(self.polymer[starting_ind]+self.polymer[(starting_ind+1)])
        #print(self.pairs)
        return None

    def _pair_insertion(self) -> None:
        new_polymer = ''
        for pair in self.pairs:
            #print(pair)
            #print(f"To insert {self.polymer_template[pair]}")
            new_pair = pair[0] + self.polymer_template[pair]
            #print(new_pair)
            new_polymer+=new_pair
        self.polymer = new_polymer + self.polymer[-1]
        self.pairs = []
        return None
    def _count_letters(self)-> List[int]:
        letters = {}
        for letter in self.polymer:
            if letter in letters:
                letters[letter] +=1
            else:
                letters[letter] = 1
        return [max(letters.values()),min(letters.values())]
    def return_answer(self) -> int:
        numbers = self._count_letters()
        return numbers[0] - numbers[1]
def main() -> None:
    polymer = Polymers()
    # print(polymer)
    polymer()
    print(polymer.return_answer())
    return None


if __name__ == '__main__':
    main()
