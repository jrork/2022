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
        # filename = "/Users/jrork/Documents/Development/advent of code/2022/Day 6/Part 1/example.data"
        filename = "/Users/jrork/Documents/Development/advent of code/2022/Day 6/Part 1/signal.data"
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
    print("------------------------end of LoadData-----------------------")
    print()

    start_of_packet = find_start_of_packet_value(lines, 14)
    print(start_of_packet)

    # Do Part 1 work
    print()
    answer = "X"
    print()
    print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    #print()
    answer = "X"
    #print()
    #print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

def find_start_of_packet_value(stream, key_length):
    key = []
    #Prime the list
    for i in range(key_length):
        key.append(stream[0][i])
    if not check_four_for_dupes(key):
        return i + 1
    for i in range(key_length, len(stream[0])):
        key.append(stream[0][i])
        del key[0]
        if not check_four_for_dupes(key):
            return i + 1

    return 0

def check_four_for_dupes(list):
    for i in range(len(list)):
        for j in range(len(list)-1, i, -1):
            if list[i] == list[j]:
                print(f"Found a dupe in {list}")
                return True
    return False

if __name__ == "__main__":
    main()
