'''
Advent of Code 2022 - Day 6
'''
import aocd


def get_start_of_message(start_bits: int) -> int:
    sop = [str(i) for i in range(start_bits)]
    for index, char in enumerate(input):
        sop[index % start_bits] = char
        if index >= start_bits-1:
            if len(set(sop)) == start_bits:
                return index + 1


if __name__ == '__main__':
    AOC_YEAR = 2022
    AOC_DAY = 6

    input = open("input.txt").read()
    input = aocd.get_data(year=AOC_YEAR, day=AOC_DAY)

    a = get_start_of_message(4)
    print(f'{a = }')
    aocd.submit(answer=a, part='a', year=AOC_YEAR, day=AOC_DAY)

    b = get_start_of_message(14)
    print(f'{b = }')
    aocd.submit(answer=b, part='b', year=AOC_YEAR, day=AOC_DAY)