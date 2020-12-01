# https://adventofcode.com/2020/day/1

def main():
    raw_inp = open("day_1_input.txt", "r")
    inp = list(map(int, raw_inp.read().split()))
    # print("Input: " + str(inp) + "\n")

    print("Part one: " + part_one(inp))
    print("Part two: " + part_two(inp))


def part_one(entries):
    for i in entries:
        for j in entries:
            if i + j == 2020:
                return str(i * j)


def part_two(entries):
    for i in entries:
        for j in entries:
            for k in entries:
                if i + j + k == 2020:
                    return str(i * j * k)


if __name__ == '__main__':
    main()
