# https://adventofcode.com/2020/day/5

def main():
    inp_file = open("day_5_input.txt", "r")
    inp = list(map(str, inp_file.read().split('\n')))
    # print("Input: " + str(inp) + "\n")

    print("Part one: " + str(part_one(inp)))
    print("Part two: " + str(part_two(inp)))


def part_one(boarding_passes):
    highest_ID = 0

    for passes in boarding_passes:
        rows, columns = [i for i in range(128)], [i for i in range(8)]
        row, column = passes[0:7], passes[7:10]

        seat_ID = search(rows, row, 'B', 'F') * 8 + search(columns, column, 'R', 'L')

        if seat_ID > highest_ID:
            highest_ID = seat_ID
        
    return highest_ID



def part_two(boarding_passes):
    seats = []

    for passes in boarding_passes:
        rows, columns = [i for i in range(128)], [i for i in range(8)]
        row, column = passes[0:7], passes[7:10]

        seat_ID = search(rows, row, 'B', 'F') * 8 + search(columns, column, 'R', 'L')
        seats.append(seat_ID)
    
    seats.sort()

    for i in range(len(seats)):
        if i not in seats and (i+1) in seats and (i-1) in seats:
            return i

    

def search(scope, pos, upper, lower):
    for region in pos:
        if region == lower:
            scope = scope[:len(scope)//2]
        if region == upper:
            scope = scope[len(scope)//2:]
    
    return scope[0]


if __name__ == '__main__':
    main()
