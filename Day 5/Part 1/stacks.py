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
        line = line.rstrip()
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
        filename = "/Users/jrork/Documents/Development/advent of code/2022/Day 5/Part 1/stacks.data"
        # filename = "/Users/jrork/Documents/Development/advent of code/2022/Day 5/Part 1/example.data"
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
    print()
    print("Starting stacks")
    print_stacks(stacks)
    stacks = apply_directions(stacks, directions)
    # print_stacks(stacks)

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
    tallest_stack_height = 0
    number_of_stacks = len(stacks)
    for i in range(len(stacks)-1, -1, -1):
        current_stack_height = len(stacks[i])
        if current_stack_height > tallest_stack_height:
            tallest_stack_height = current_stack_height
    for i in range(tallest_stack_height-1, -1, -1):
        for j in range(number_of_stacks):
            current_stack_height = len(stacks[j])
            if i < current_stack_height:
                print(f"[{stacks[j][i]}] ", end="")
            else:
                print("    ", end="")
        print()
    
    for i in range(1, number_of_stacks+1):
        print(f"{i}   ", end="")

    print()
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
    for i in range(number_of_stacks):
        stacks.append([])

    for current_row in range(row_count-1, -1, -1):
        str_temp = data[current_row]
        new_str_temp = str_temp.ljust(length_of_list, " ")

        current_position = 1
        stack_number = 0
        while current_position < length_of_list:
            value = new_str_temp[current_position]
            if not str(value).isspace():
                stacks[stack_number].append(value)
            current_position = current_position + 4
            stack_number = stack_number + 1

    return stacks

def apply_directions(stacks, directions):
    move_stack = []
    for direction in directions:
        print()
        print("-----------------")
        from_stack = int(direction[1])
        number_of_crates = int(direction[0])
        to_stack = int(direction[2])
        print(f"Moving {number_of_crates} crate(s) from Stack {from_stack} to {to_stack}\n")

        for i in range(number_of_crates):
            stacks[to_stack-1].append(stacks[from_stack-1].pop())
        print_stacks(stacks)
    return stacks

if __name__ == "__main__":
    main()
