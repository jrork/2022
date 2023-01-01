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

class Node:
    def __init__(self, type, name, size=0, parent=None):
        self.parent = parent
        self.children = []
        self.type = type
        self.name = name
        self.size = size

class File:
    def __init__(self, filename, file_size):
        self.name = filename
        self.size = file_size

#
# Main
#
def main():

    args = sys.argv[1:]
    if len(args) != 1:
	    # filename = "/Users/jrork/Documents/Development/advent of code/2022/Day 7/Part 1/example.data"
	    filename = "/Users/jrork/Documents/Development/advent of code/2022/Day 7/Part 1/filesystem.data"
#        print("Usage: " + sys.argv[0] + " inputfile");
#        return
    else:
	    filename = args[0]
    print("Input File:", filename)
    print()

    # Load data
    lines = loadData(filename)
    print(" Lines Read: ", len(lines))
    print()
    printLines(lines)
    print()
    print("-------------------------end of loadData--------------------")
    print()


    file_tree = build_file_tree(lines)
    calculate_directory_size(file_tree)
    total_space_used = file_tree.size
    print(f"Total space used on disk is {total_space_used}")
    print(find_all_directories_less_than_100000(file_tree))
    total_disk_space = 70000000
    disk_space_needed_for_update = 30000000
    disk_space_required_to_be_deleted = abs(total_disk_space - disk_space_needed_for_update - total_space_used)
    print(f"Total space that needs to be recovered: {disk_space_required_to_be_deleted}")
    directory_size_list = []
    create_directory_size_list(file_tree, directory_size_list)
    print(sorted(directory_size_list))
    # Do Part 1 work
    # print()
    # answer = "X"
    # print()
    # print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    #print()
    # answer = "X"
    #print()
    #print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

def build_file_tree(input):
    root = Node("dir", '/', 0)
    current_directory = root
    for line in input:
        if line[0] == '$':
            command = str(line).split(' ')
            if command[1] == 'cd':
                argument = command[2]
                if argument == "/":
                    next
                elif argument == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory.children.append(Node("dir", argument, 0, current_directory))
                    # make current_directory equal to the node that was just added
                    current_directory = current_directory.children[-1]
            # if command[1] == 'ls':
        elif line[0].isnumeric():
            command = str(line).split(' ')
            filename = command[1]
            size = int(command[0])
            current_directory.children.append(Node("file", filename, size, current_directory))

    return root

def calculate_directory_size(directory):
    directory_size = 0
    for child in directory.children:
        if child.type == 'file':
            directory_size = directory_size + child.size
        elif child.type == 'dir':
            directory_size = directory_size + calculate_directory_size(child)
        else:
            print("type doesn't make sense.")
    directory.size = directory_size
    return directory_size

def find_all_directories_less_than_100000(directory):
    directory_size = 0
    if directory.size < 100000:
        directory_size = directory_size + directory.size
    for child in directory.children:
        if child.type == 'dir':
            directory_size = directory_size + find_all_directories_less_than_100000(child)
    return directory_size

def create_directory_size_list(directory, directory_size_list):
    for child in directory.children:
        if child.type == 'dir':
            create_directory_size_list(child, directory_size_list)
            directory_size_list.append(child.size)
    return 

if __name__ == "__main__":
    main()
