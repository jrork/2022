#
# Adavent of Code 2022 Day 3 Part 2
#
# Requirements:
# To help prioritize item rearrangement, every item type can be converted to a priority:
#
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
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
        # print("Usage: " + sys.argv[0] + " inputfile");
        filename = "./Day 3/Part 1/rucksack.data"
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
    print("-----------")

    total_priority = 0
    rucksack_number = 0
    
    groups = divide_groups(lines)

    for group in groups:
        badge = find_duplicate(group)
        priority = find_priority(badge)
        total_priority = total_priority + priority

    # Do Part 1 work
    # print()
    # answer = "X"
    # print()
    print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, total_priority, color.END))

    # # Do Part 2 work
    # #print()
    # answer = "X"
    # #print()
    # #print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

def find_duplicate(group):
    print(group)
    for i in group[0]:
        if i in group[1]:
            if i in group[2]:
                return i

def find_priority(item):
    ascii_value = ord(item)
    priority = 0
    if ascii_value >= 65 and ascii_value <= 90:
        priority = ascii_value - 38
    elif ascii_value >= 97 and ascii_value <= 122:
        priority = ascii_value - 96

    return priority 

def divide_groups(list_of_rucksacks):
    group_list = []
    for rucksack in range(0, len(list_of_rucksacks), 3):
        position = rucksack
        group_list.append(list_of_rucksacks[position:position+3])
    return group_list

def find_badge_value(rucksacks):
    return 'A'

if __name__ == "__main__":
    main()
