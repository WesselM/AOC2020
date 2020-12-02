# https://adventofcode.com/2020/day/2

def main():
    raw_inp = open("day_2_input.txt", "r")
    inp = list(map(str, raw_inp.read().split('\n')))
    # print("Input: " + str(inp) + "\n")

    print("Part one: " + str(part_one(inp)))
    print("Part two: " + str(part_two(inp)))


def part_one(passwords):
    valids = 0
    for i in passwords:
        # if password.count(char) >= min and password.count(char) <= max:
        if i.split(': ')[1].count(i.split(': ')[0].split(' ')[1]) >= int(i.split(': ')[0].split(' ')[0].split('-')[0]) and \
            i.split(': ')[1].count(i.split(': ')[0].split(' ')[1]) <= int(i.split(': ')[0].split(' ')[0].split('-')[1]):
            valids += 1

    return valids


def part_two(passwords):
    valids = 0
    for i in passwords:
        # if  (password[first_pos] == char) != (password[second_pos] == char):
        if  (i.split(': ')[1][int(i.split(': ')[0].split(' ')[0].split('-')[0]) - 1] == i.split(': ')[0].split(' ')[1]) != \
            (i.split(': ')[1][int(i.split(': ')[0].split(' ')[0].split('-')[1]) - 1] == i.split(': ')[0].split(' ')[1]):
            valids += 1

    return valids


if __name__ == '__main__':
    main()