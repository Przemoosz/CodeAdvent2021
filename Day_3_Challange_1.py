from typing import List


def rate(bit_sum: List[int], lines: int) -> int:
    gamma_binary = ''
    epsilon_binary = ''
    for i in bit_sum:
        if i > lines / 2:
            gamma_binary += '1'
            epsilon_binary += '0'
        else:
            gamma_binary += '0'
            epsilon_binary += '1'
    epsilon = int(epsilon_binary, 2)
    gamma = int(gamma_binary, 2)
    power = gamma * epsilon
    print(power)
    return power


def main():
    bit_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_ammount = 0
    with open('day_3_input_1.txt', 'r') as file:
        for line in file:
            line = line.strip()
            line_ammount += 1
            for ind, bit in enumerate(line):
                bit_sum[ind] += int(bit)
        print(bit_sum)
    rate(bit_sum, line_ammount)


if __name__ == '__main__':
    main()
