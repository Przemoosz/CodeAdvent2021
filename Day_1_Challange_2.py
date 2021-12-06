from collections import deque
from typing import List
class Sums:
    def __init__(self):
        self.parmeter_sum = [0, 0, 0, 0, 0, 0, 0, 0]
        self.position = 0
        self.result = []
        self.total_increasing = 0
        self.result_list = []
        self.y_parameter = 1
        self.x_parameter = 1
        #self.c_parameter = 0
        self.sums =[0,0,0]

    def __str__(self):
        # print(self.result)
        return f'Total increasing {self.total_increasing}'

    def summing(self, line_number: int, line_value: int) -> None:
        # Case for first element
        # print(line_value, self.position,sep="---")
        if line_number == 0:
            self.parmeter_sum[0] += line_value
            self.position += 1
            return None
        if self.position in [0, 1, 2]:
            self.parmeter_sum[0] += line_value
        if self.position in [1, 2, 3]:
            self.parmeter_sum[1] += line_value
        if self.position in [2, 3, 4]:
            self.parmeter_sum[2] += line_value
        if self.position in [3, 4, 5]:
            self.parmeter_sum[3] += line_value
        if self.position in [4, 5, 6]:
            self.parmeter_sum[4] += line_value
        if self.position in [5, 6, 7]:
            self.parmeter_sum[5] += line_value
        if self.position in [6, 7, 8]:
            self.parmeter_sum[6] += line_value
        if self.position in [7, 8, 9]:
            self.parmeter_sum[7] += line_value
        if self.position != 9:
            self.position += 1
            return None
        if self.position == 9:
            for val in self.parmeter_sum:
                self.result.append(val)
            for val,letter in zip(self.parmeter_sum,['A','B','C','D','E','F','G','H']):
                print(val,letter,sep='--')
            print('Next')
            self.parmeter_sum = [0, 0, 0, 0, 0, 0, 0, 0]
            self.position = 0

    def new_summing(self,line_number: int, line_value: int) -> None:

        if self.y_parameter <= 3:
            self.sums[0] += line_value
        pass



    def increase_check(self) -> int:
        for ind, val in enumerate(self.result):
            if ind == 0:
                print(f'{val} - N/A')
                continue
            if self.result[ind - 1] < val :
                self.total_increasing += 1
                print(f'{val} - Increased')
            elif self.result[ind - 1] > val:
                print(f'{val} - Decreased')
            elif val == self.result[ind - 1]:
                print(f'{val} - N/C')
        return self.total_increasing

def increase_check(lista: List) -> int:
    total_increasing =0
    for ind, val in enumerate(lista):
        if ind == 0:
            print(f'{val} - N/A')
            continue
        if lista[ind - 1] < val :
            total_increasing += 1
            print(f'{val} - Increased')
        elif lista[ind - 1] > val:
            print(f'{val} - Decreased')
        elif val == lista[ind - 1]:
            print(f'{val} - N/C')
    print(total_increasing)
    return total_increasing
def new_read() -> None:
    return_list=[]
    with open('day_1_input_2.txt','r') as file:
        lines = deque()
        for line in file:
            lines.append(int(line))
    for num in range(len(lines)):
        if len(lines)<3:
            return_list.append(lines[0]+lines[1])
            return_list.append(lines[1])
            break
        value_sum= lines[0] + lines[1] + lines[2]
        print(value_sum)
        return_list.append(value_sum)
        lines.popleft()
    print(lines)
    increase_check(return_list)

def main() -> int:
    with open('day_1_input_2.txt', 'r') as file:
        total_increasing = 0
        parameter_sum = Sums()
        for line_number, line in enumerate(file):
            parameter_sum.summing(line_number, int(line))

        print(parameter_sum.increase_check())

    return total_increasing


if __name__ == '__main__':
    #main()
    new_read()
