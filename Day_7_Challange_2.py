from typing import List
import multiprocessing

"""
Creator: Przemysław Szewczak
Date: 11.12.2021
Source: https://adventofcode.com/2021/day/7
Note: Multiprocessing is not necessary, it's used because i want to write program using them
For larger input like millions of points, multiprocessing program will by faster than the not parallel 
"""


def load_data() -> List[int]:
    """Loads data from txt file and change type to integer"""
    with open('day_7_input.txt', 'r') as file:
        positions = file.readline().strip().split(',')
        positions = list(map(lambda x: int(x), positions))
        return positions


def check_point(postion_lists: List[int], queue: multiprocessing.Queue, start: int, end: int) -> List[int]:
    """Calculating distance between crab position and destiny point(delta x),
    then summing fuel consumption(|delta x|)"""
    fuel_consuption = []
    for point in range(start, end):
        fuel_to_point = 0
        for position in postion_lists:
            fuel_to_point += sum(list(range(abs(position - point) + 1)))
        fuel_consuption.append(fuel_to_point)
    queue.put(fuel_consuption)
    return fuel_consuption


def check_point_temp(postion_lists: List[int], start: int, end: int) -> List[int]:
    """ Not used only for testing purpose"""
    fuel_consuption = []
    for point in range(start, end):
        fuel_to_point = 0
        for position in postion_lists:
            print(list(range(abs(position - point) + 1)), "-", sum(list(range(abs(position - point) + 1))), sep=" ")
            fuel_to_point += sum(list(range(abs(position - point) + 1)))
        fuel_consuption.append(fuel_to_point)
    print(fuel_consuption)
    return fuel_consuption


def multiprocessing_main_function() -> int:
    """Using multiprocessing to split tasks from one core to 4 cores"""
    position = load_data()
    position.sort(reverse=True)
    # Using queue to communicate with __main__ process
    queue = multiprocessing.Queue()
    proocess_list = []
    # Creating processes
    proocess_list.append(multiprocessing.Process(target=check_point, args=(position, queue, 0, 501,)))
    proocess_list.append(multiprocessing.Process(target=check_point, args=(position, queue, 501, 1001,)))
    proocess_list.append(multiprocessing.Process(target=check_point, args=(position, queue, 1001, 1501,)))
    proocess_list.append(multiprocessing.Process(target=check_point, args=(position, queue, 1501, 2001,)))
    # Starting process
    [process.start() for process in proocess_list]
    # Fetching process results
    core_results = [queue.get() for _ in range(4)]
    [process.join() for process in proocess_list]
    [process.close() for process in proocess_list]
    # Terminate process if it is not closed yet, then raise Exception
    if len(multiprocessing.active_children()) != 0:
        [process.terminate() for process in proocess_list]
        raise Exception("Process was not closed properly")
    min_val_list = []
    [result.sort() for result in core_results]
    [min_val_list.append(i[0]) for i in core_results]
    min_val_list.sort()
    print(min_val_list[0])
    return min_val_list[0]


def main() -> None:
    """ Not used only for testing purpose"""
    position = load_data()
    check_point(position, 5, 6)


if __name__ == '__main__':
    # main()
    multiprocessing_main_function()
