#
# Adavent of Code 2022 Day 3 Part 1
#
# Requirements:
# To help prioritize item rearrangement, every item type can be converted to a priority:
#
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
#

import sys
from collections import Counter


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

    total_priority = 0
    rucksack_number = 0

    for line in lines:
        rucksack_number = rucksack_number + 1
        duplicate = find_duplicate(line)
        priority = find_priority(duplicate)
        print(f"Rucksack #{rucksack_number} has duplicate item {duplicate}.")
        print(f"Rucksack #{rucksack_number} has a priority of {priority}.")
        print() 
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

def find_duplicate(rucksack):
    rucksack_size = len(rucksack)
    compartment1 = rucksack[0:rucksack_size//2]
    compartment2 = rucksack[rucksack_size//2:]
    print(f"Compartment 1: {compartment1}")
    print(f"Compartment 2: {compartment2}")
    for i in range(0,len(compartment2)):
        if compartment2[i] in compartment1:
            return compartment2[i]

    # duplicate = str((Counter(compartment1) - Counter(compartment2)).elements())

    print(f"Item found in both compartments: {duplicate}")
    return duplicate

def find_priority(item):
    ascii_value = ord(item)
    priority = 0
    if ascii_value >= 65 and ascii_value <= 90:
        priority = ascii_value - 38
    elif ascii_value >= 97 and ascii_value <= 122:
        priority = ascii_value - 96

    return priority 

if __name__ == "__main__":
    main()
