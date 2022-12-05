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
        filename = "./Day 4/Part 1/input.data"
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
    print("--------------------end of loaded data--------------------------")
    print()
    # Do Part 1 work
    fully_contained_pair_count = 0
    for line in lines:
        assignments = fill_out_section_list(line)
        fully_contained_pair_count = fully_contained_pair_count + find_fully_contained_count(assignments)
    answer = fully_contained_pair_count
    # print()
    # answer = "X"
    # print()
    print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    #print()
    answer = "X"
    #print()
    #print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

def fill_out_section_list(input):
    sections = input.split(',')
    section1 = str(sections[0]).split('-')
    section2 = str(sections[1]).split('-')

    section_1_start = int(section1[0])
    section_1_end   = int(section1[1])+1
    section_2_start = int(section2[0])
    section_2_end   = int(section2[1])+1
    assignments = []
    first_pair = []
    second_pair = []
    for i in range(section_1_start, section_1_end):
        first_pair.append(i)

    for i in range(section_2_start, section_2_end):
        second_pair.append(i)

    assignments.append(first_pair)
    assignments.append(second_pair)

    return assignments

def find_fully_contained_count(assignments):
    contained_pair_count = 0
    first_pair = assignments[0]
    second_pair = assignments[1]
    containment_found = False

    if is_pair_contained(first_pair, second_pair):
        contained_pair_count = contained_pair_count + 1
        containment_found = True
        print(f"Pair 2 {second_pair} is in Pair 1 {first_pair}.\n")
    else:
        print(f"Pair 2 {second_pair} is NOT in Pair 1 {first_pair}.\n")

    if not containment_found:
        if is_pair_contained(second_pair, first_pair):
            contained_pair_count = contained_pair_count + 1
            print(f"Pair 1 {first_pair} is in Pair 2 {second_pair}.\n")
        else:
            print(f"Pair 1 {first_pair} is NOT in Pair 2 {second_pair}.\n")

    return contained_pair_count

def is_pair_contained(pair1, pair2):
    for i in pair2:
        if i not in pair1:
            return False
    return True


if __name__ == "__main__":
    main()
