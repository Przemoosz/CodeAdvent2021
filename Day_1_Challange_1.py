def main() -> int:
    with open('day_1_input_1.txt', 'r') as file, open('day_1_output_1.txt', 'w') as file_save:
        total_increasing = 0
        previous_line = None
        for line in file:
            line = line.strip()

            # First line argument
            if previous_line is None:
                print(f'{line} (N/A)')
                file_save.write(f'{line} (N/A)\n')
                previous_line = int(line)
                continue

            # Increasing Case
            elif previous_line < int(line):
                previous_line = int(line)
                file_save.write(f'{line} (increasing)\n')
                print(f'{line} (increasing)')
                total_increasing+=1
                continue

            # Decreasing Case
            elif previous_line > int(line):
                previous_line = int(line)
                file_save.write(f'{line} (decreasing)\n')
                print(f'{line} (decreasing)')
                continue


            else:
                print(f'{line} (No change)')
                continue
    return total_increasing


if __name__ == '__main__':
    #print(main())
    #print(1 in [1,2,4])
