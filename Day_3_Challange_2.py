from typing import List
import time


def file_reformat(bit_value: bool, file_name: str, bit_check: int) -> str:
    """
    bit_value = True - 1 is most common bit
    bit_value = False - 0 is most common bit
    """
    if bit_value:
        with open(file_name, 'r') as file:
            lines_to_save = []
            for line in file:

                if line[bit_check] == '1':
                    lines_to_save.append(line.strip())
                else:
                    continue
            with open('temp.txt', 'w') as write_file:
                for line in lines_to_save:
                    if line == lines_to_save[-1]:
                        write_file.write(line)
                    else:
                        write_file.write(line + '\n')
        file_name = 'temp.txt'
        return (file_name)
    else:
        with open(file_name, 'r') as file:
            lines_to_save = []
            for line in file:
                if line[bit_check] == '0':
                    lines_to_save.append(line.strip())
                else:
                    continue
            with open('temp.txt', 'w') as write_file:
                for line in lines_to_save:
                    if line == lines_to_save[-1]:
                        write_file.write(line)
                    else:
                        write_file.write(line + '\n')
    file_name = 'temp.txt'
    if len(lines_to_save) == 1:
        return False
    return file_name


def bit_check_oxygen(file_name: str, bit_check: int, mode: bool):
    """
    mode - True - Oxygen search
    mode - False - Co2 search
    """
    total_lines = 0
    bit_sum = 0
    with open(file_name, 'r') as file:

        for line in file:
            total_lines += 1
            bit_sum += int(line[bit_check])
    if bit_sum >= total_lines / 2 and mode:
        return file_reformat(True, file_name, bit_check)
    elif bit_sum < total_lines / 2 and mode:
        return file_reformat(False, file_name, bit_check)
    elif bit_sum < total_lines / 2 and not mode:
        print("here")
        return file_reformat(True, file_name, bit_check)
    elif bit_sum >= total_lines / 2 and not mode:
        return file_reformat(False, file_name, bit_check)


def bit_length_check() -> int:
    with open('day_3_input_1.txt', 'r') as file:
        return (len(file.readline().strip())) - 1


def main():
    #Oxygen
    file_name = bit_check_oxygen('day_3_input_1.txt', 0, True)
    for i in range(bit_length_check()):
        file_name = bit_check_oxygen(file_name, i + 1, True)
    with open('temp.txt', 'r') as file:
        oxygen_value = file.readline().strip()
    #CO2
    file_name = bit_check_oxygen('day_3_input_1.txt', 0, False)

    for i in range(bit_length_check()):
        file_name = bit_check_oxygen(file_name, i + 1, False)
        if not file_name:
            break
    with open('temp.txt', 'r') as file:
        co_value = file.readline().strip()
    print(co_value,oxygen_value, end='\n')
    life_support_rating = int(co_value,2)*int(oxygen_value,2)
    print(life_support_rating)
if __name__ == '__main__':
    main()
