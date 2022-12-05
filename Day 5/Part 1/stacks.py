#
# Adavent of Code Template
#
import sys

# Global Variables

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#
# Load the file into a data array
#
def loadData(filename):

    lines = []

    f = open(filename)
    for line in f:
        line = line.strip()
        lines.append(line)

    f.close()

    return lines


#
# Print Array
#
def printLines(lines):

    for line in lines:
      print(line)


#
# Main
#
def main():

    args = sys.argv[1:]
    if len(args) != 1:
        # filename = "/Users/jrork/Documents/Development/advent of code/2022/Day 5/Part 1/stacks.data"
        filename = "/Users/jrork/Documents/Development/advent of code/2022/Day 5/Part 1/example.data"
        # print("Usage: " + sys.argv[0] + " inputfile");
        # return
    else:
        filename = args[0]
    print("Input File:", filename)
    print()

    # Load data
    lines = loadData(filename)
    print(" Lines Read: ", len(lines))
    print()
    printLines(lines)
    print("-------------------------end of loadData---------------------------")
    print()

    # Do Part 1 work     
    directions = get_directions(lines)
    stacks = load_stacks(lines)
    print_stacks(stacks)

    print()
    answer = "X"
    print()
    print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    #print()
    answer = "X"
    #print()
    #print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))


def get_directions(data):
    directions = []

    for row in data:
        if row.find("move") != -1:
            temp = str(row).split(' ')
            number = int(temp[1])
            from_stack = int(temp[3])
            to_stack = int(temp[5])
            direction = [number, from_stack, to_stack]
            directions.append(direction)

    return directions

def print_stacks(stacks):
    print()
    for row in stacks:
        print('[', end="")
        for item in row:
            print(item, end="] [")
        print(']')
    return

def load_stacks(data):
    row_count = 0
    number_of_stacks = 0
    for row in data:
        if row.find('1') != -1:
            temp = str(row).split(' ')
            number_of_stacks = int(temp[-1])
            break
        else:
            row_count += 1

    print(f"The number of stacks is {number_of_stacks}")
    print(f"The number of rows is {row_count}")          
    length_of_list = number_of_stacks + 2 + (number_of_stacks-1)*3
    print(f"Length of list is {length_of_list}")

    stacks = []

    # current_row = row_count;
    for current_row in range(row_count-1, -1, -1):
        str_temp = data[current_row]
        new_str_temp = str_temp.ljust(length_of_list, " ")

        newlist = []
        current_position = 1
        while current_position < length_of_list:
            newlist.append(new_str_temp[current_position])
            current_position = current_position + 4

        print(newlist)
        stacks.append(newlist)

    # for row_index in range(row_count, -1, -1):
    #     new_temp = []
    #     for stack_number in range(0, number_of_stacks):
    #         new_temp.append('X')
    #     stacks.append(new_temp)

    return stacks

if __name__ == "__main__":
    main()
