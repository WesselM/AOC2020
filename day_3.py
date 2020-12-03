# https://adventofcode.com/2020/day/3

def main():
    raw_inp = open("day_3_input.txt", "r")
    inp = list(map(str, raw_inp.read().strip().split('\n')))
    # print("Input: " + str(inp) + "\n")

    print("Part one: " + str(part_one(inp)))
    print("Part two: " + str(part_two(inp)))


def part_one(path):
    return tree_encounter(path, 3, 1)
    

def part_two(path):
    return (tree_encounter(path, 1, 1) *  tree_encounter(path, 3, 1) * tree_encounter(path, 5, 1) * \
            tree_encounter(path, 7, 1) *  tree_encounter(path, 1, 2))  


def tree_encounter(path, right, down):
    trees = 0

    for i in range(0, len(path), down):
        x = right * i // down % len(path[i])
        if path[i][x] == '#':
            trees += 1

    return trees


if __name__ == '__main__':
    main()
