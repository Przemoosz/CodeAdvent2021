from typing import List


"""
Creator: Przemysław Szewczak
Date: 14.12.2021
Source: https://adventofcode.com/2021/day/8
Note: Im not proud of this code...
"""
"""
    0000
   3     1
   3     1
   3     1
    5555    
   4     2
   4     2
   4     2
    6666
"""


class Digits:
    def __init__(self, list_of_digits: List[str]):
        self.inp = list_of_digits[0]
        self.output = list_of_digits[1]
        self.decoded = 0
        self.code = {0: "", 1: "", 2: "", 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        self.position = {'0pos': "", '1pos': "", '2pos': "", '3pos': "", '4pos': "", '5pos': "", '6pos': ""}

    def __call__(self, *args, **kwargs):
        self._finding_unique()
        self._finding_0pos()
        self._finding_6pos()
        self._finding_4pos()
        self._finding_5pos()
        self._finding_1pos()
        self._finding_2pos()
        self._finding_3pos()
        self.finding_rest_digits()
        self.sort_values()
        self.decode_output()

    def __str__(self):
        print(self.code)
        print(self.position)
        print(self.decoded)
        return ''

    def sort_values(self) -> None:
        new_dict = {}
        for k, v in self.code.items():
            sorted_code = sorted(v)
            new_dict[k] = ''.join(sorted_code)
        self.code = new_dict

    def finding_rest_digits(self) -> None:
        digits = self.inp.split(" ")
        for i in digits:
            if len(i) == 5 and i not in self.code.values():
                self.code[5] = i
            elif len(i) == 6 and self.position['5pos'] in i and i not in self.code.values():
                self.code[6] = i
            elif len(i) == 6 and i not in self.code.values():
                self.code[0] = i

    def _finding_unique(self) -> None:
        digits = self.inp.split(" ")
        print(digits)
        for i in digits:
            if len(i) == 2:
                self.code[1] = i
            elif len(i) == 3:
                self.code[7] = i
            elif len(i) == 4:
                self.code[4] = i
            elif len(i) == 7:
                self.code[8] = i

    def _finding_0pos(self) -> None:
        for i in self.code[7]:
            print(self.code[2])
            if i not in self.code[1][0] and i not in self.code[1][1]:
                self.position['0pos'] = i
        pass

    def _finding_1pos(self) -> None:
        second_digit = ''
        digits = self.inp.split(' ')
        for i in digits:
            if len(i) == 5 and i != self.code[3] and self.position['0pos'] in i and self.position['5pos'] in i \
                    and self.position['4pos'] in i and self.position['6pos'] in i:
                second_digit = i
        for i in second_digit:
            if i not in self.position['6pos'] + self.position['0pos'] + self.position['5pos'] + self.position['4pos']:
                self.position['1pos'] = i
        self.code[2] = second_digit

    def _finding_2pos(self) -> None:
        for i in self.code[1]:
            if i != self.position['1pos']:
                self.position['2pos'] = i
        pass

    def _finding_3pos(self) -> None:
        for i in self.code[8]:
            if i not in self.position.values():
                self.position['3pos'] = i
        pass

    def _finding_4pos(self) -> None:
        for i in self.code[8]:
            if i not in self.code[4] + self.position['0pos'] + self.position['6pos']:
                self.position['4pos'] = i

        pass

    def _finding_5pos(self) -> None:
        third_digit = ''
        digits = self.inp.split(' ')
        for i in digits:
            if len(i) == 5 and self.position['6pos'] in i and self.code[7][0] in i and self.code[7][1] in i \
                    and self.code[7][2] in i:
                third_digit = i
        for i in third_digit:
            if i not in self.position['6pos'] + self.code[7]:
                self.position['5pos'] = i
        self.code[3] = third_digit
        pass

    def _finding_6pos(self) -> None:
        ninth_digit = ''
        digits = self.inp.split(' ')
        for i in digits:
            if len(i) == 6 and self.position['0pos'] in i and self.code[4][0] in i and self.code[4][1] in i \
                    and self.code[4][2] in i and self.code[4][3] in i:
                ninth_digit = i
        for i in ninth_digit:
            # print(i)
            if i not in self.position['0pos'] + self.code[4]:
                self.position['6pos'] = i
        self.code[9] = ninth_digit

    def decode_output(self) -> None:
        output = self.output.split(" ")
        digits = []
        for digit in output:
            d = sorted(digit)
            digits.append("".join(d))
        # print(digits)
        return_str = ''
        for digit in digits:
            for k, v in self.code.items():
                if digit == v:
                    return_str += str(k)
        self.decoded = int(return_str)


def load_lines() -> List[List[str]]:
    with open('day_8_input_1.txt') as file:
        return_list = [line.strip().split(" | ") for line in file]
        return return_list


def main() -> None:
    lines = load_lines()
    total_sum=0
    for line in lines:
        code = Digits(line)
        code()
        total_sum +=code.decoded
    print(total_sum)
    pass


if __name__ == '__main__':
    main()
