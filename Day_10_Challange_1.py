from typing import List


def load_data() -> List[str]:
    """Function loads data from txt file and saves it to list"""
    with open('day_10_input_1.txt') as file:
        return_list = [line.strip() for line in file]
    return return_list


def check_if_corrupted(line: str) -> bool:
    """Prototype function used in first attempt.
      Not used in program directly"""
    char_dict = {}
    # print(line)
    for i in "{[(<>)]}":
        char_dict[i] = 0
    for char in line:
        char_dict[char] += 1
        # print(char_dict)

        if char_dict['('] >= 1 and char_dict[')'] >= 1:
            char_dict['('] -= 1
            char_dict[')'] -= 1
        if char_dict['{'] >= 1 and char_dict['}'] >= 1:
            char_dict['{'] -= 1
            char_dict['}'] -= 1
        if char_dict['['] >= 1 and char_dict[']'] >= 1:
            char_dict['['] -= 1
            char_dict[']'] -= 1
        if char_dict['<'] >= 1 and char_dict['>'] >= 1:
            char_dict['<'] -= 1
            char_dict['>'] -= 1
    for i in char_dict.values():
        if i == 0:
            return True
        else:
            return False


def corrupted_func(line: str) -> str:
    """Function used to search corrupted lines"""
    open_chars = '{[(<'
    close_chars = '>)]}'
    opening = []
    closing = []
    for char in line:
        if char in open_chars:
            opening.append(char)
        elif char in close_chars:
            closing.append(char)
            # Checking if new close char is connected with previous open char
            if opening[-1] + char == "[]" or opening[-1] + char == "{}" or \
                    opening[-1] + char == "{}" or opening[-1] + char == "<>" or opening[-1] + char == "()":
                # If yes then function remove this char from end of open list
                opening.pop(-1)
            else:
                # If False then return this char as corrupted char
                not_fine = char
                break
    else:
        return "Fine"
    return not_fine


def capture_corrupted(lines: List[str]) -> List[str]:
    # Old not used function to check if length of str can be divided by 2
    possibly_corrupted = []
    for line in lines:
        if len(line) % 2 == 0:
            possibly_corrupted.append(line)
    return possibly_corrupted


def main() -> None:
    lines = load_data()
    char_dict = {}
    for i in ">)]}":
        char_dict[i] = 0
    points = 0
    for line in lines:
        result = corrupted_func(line)
        # print(result)
        if result != "Fine":
            char_dict[result] += 1
    # print(char_dict)
    # Counting points
    points += char_dict[")"] * 3
    points += char_dict["]"] * 57
    points += char_dict["}"] * 1197
    points += char_dict[">"] * 25137
    print(points)
    return None


if __name__ == '__main__':
    main()
