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

class Tree:
    def __init__(self, height):
        self.height = int(height)
        self.visible = False
        self.scenic_score = 0

#
# Load the file into a data array
#
def loadData(filename):

    lines = []

    f = open(filename)
    for line in f:
        line = line.strip()
        row = []
        for height in line:
            tree = Tree(height)
            row.append(tree)
        
        lines.append(row)
    f.close()

    return lines


#
# Print Array
#
def printTreeMap(map):

    for row in map:
        for tree in row:
            print(f"{tree.height}-{tree.visible}:{tree.scenic_score}", end="  ")
        print("\n")


#
# Main
#
def main():

    args = sys.argv[1:]
    if len(args) != 1:
	    # filename = "/Users/jrork/Documents/Development/advent of code/2022/Day 8/Part 1/example.data"
	    filename = "/Users/jrork/Documents/Development/advent of code/2022/Day 8/Part 1/puzzle.data"
        # print("Usage: " + sys.argv[0] + " inputfile");
        # return
    else:
	    filename = args[0]

    print("Input File:", filename)
    print()

    # Load data
    map = loadData(filename)
    print(" Lines Read: ", len(map))
    print()
    printTreeMap(map)
    print()
    print("-------------------------end of loadData--------------------")
    print()

    map = check_visibility_from_left_side(map)
    print("Tree map after left check")
    printTreeMap(map)
    print()

    map = check_visibility_from_right_side(map)
    print("Tree map after right check")
    printTreeMap(map)
    print()

    map = check_visibility_from_top_side(map)
    print("Tree map after top check")
    printTreeMap(map)
    print()

    map = check_visibility_from_bottom_side(map)
    print("Tree map after bottom check")
    printTreeMap(map)
    print()

    tree_count = count_visible_trees(map)
    print(f"Visible tree count is {tree_count}.\n\n")

    map = calculate_scenic_scores(map)
    print("Tree map after scenic scores")
    printTreeMap(map)
    print()

    highest_scenic_score = find_highest_scenic_score(map)
    print(f"Highest scenic score is {highest_scenic_score}")

    # Do Part 1 work
    # print()
    # answer = "X"
    # print()
    # print("{}Part 1 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

    # Do Part 2 work
    #print()
    answer = "X"
    #print()
    #print("{}Part 2 Answer: {}{}{}".format(color.CYAN, color.YELLOW, answer, color.END))

def check_visibility_from_left_side(map):
    row_length = len(map)
    column_length = len(map[0])
    for i in range(row_length):
        map = check_span_in_order(map, i, i+1, 0, column_length)
    return map

def check_visibility_from_right_side(map):
    row_length = len(map)
    column_length = len(map[0])
    for i in range(row_length):
        map = check_span_in_order(map, i, i+1, column_length-1, -1)
    return map

def check_visibility_from_top_side(map):
    row_length = len(map)
    column_length = len(map[0])
    for i in range(column_length):
        map = check_span_in_order(map, 0, row_length, i, i+1)
    return map

def check_visibility_from_bottom_side(map):
    row_length = len(map)
    column_length = len(map[0])
    for i in range(column_length):
        map = check_span_in_order(map, row_length-1, -1, i, i+1)
    return map

def check_span_in_order(map, starting_row, ending_row, starting_column, ending_column):
    
    tallest_tree = -1

    if (starting_row <= ending_row):
        row_step = 1
    else: 
        row_step = -1
    if (starting_column <= ending_column):
        column_step = 1
    else: 
        column_step = -1

    for row in range(starting_row, ending_row, row_step):
        for column in range(starting_column, ending_column, column_step):
            tree = map[row][column]
            if tree.height > tallest_tree:
                tree.visible = True
                tallest_tree = tree.height
    return map

def count_visible_trees(map):
    count = 0
    row_length = len(map)
    column_length = len(map[0])
    for row in range(row_length):
        for column in range(column_length):
            tree = map[row][column]
            if tree.visible == True:
                count = count + 1
    return count

def calculate_scenic_scores(map):
    row_length = len(map)
    column_length = len(map[0])
    for row in range(0, row_length):
        for column in range(0, column_length):
            span = get_span_to_right(map, row, column)
            scenic_score = calculate_span_score(span)
            print(f"{row},{column}:Score to the right: {scenic_score}")
            span = get_span_to_left(map, row, column)
            scenic_score = scenic_score * calculate_span_score(span)
            print(f"{row},{column}:Score to the left: {scenic_score}")
            span = get_span_up(map, row, column)
            scenic_score = scenic_score * calculate_span_score(span)
            print(f"{row},{column}:Score up: {scenic_score}")
            span = get_span_down(map, row, column)
            scenic_score = scenic_score * calculate_span_score(span)
            print(f"{row},{column}:Score dowm: {scenic_score}")
            map[row][column].scenic_score = scenic_score

    return map

def get_span_to_right(map, row, column):
    span = []
    column_length = len(map[0])
    for i in range(column, column_length):
        span.append(map[row][i])
    return span

def get_span_to_left(map, row, column):
    span = []
    for i in range(column, -1, -1):
        span.append(map[row][i])
    return span
    
def get_span_up(map, row, column):
    span = []
    for i in range(row, -1, -1):
        span.append(map[i][column])
    return span

def get_span_down(map, row, column):
    span = []
    row_length = len(map)
    for i in range(row, row_length):
        span.append(map[i][column])
    return span

def calculate_span_score(span):
    span_score = 0
    span_length = len(span)
    highest_tree_height = span[0].height
    for i in range(1, span_length):
        if span[i].height < highest_tree_height:
            span_score = span_score + 1
        elif span[i].height == highest_tree_height:
            span_score = span_score + 1
            break
        else:
            span_score += 1
            break
    return span_score

def find_highest_scenic_score(map):
    highest_scenic_score = 0
    row_length = len(map)
    column_length = len(map[0])
    for row in range(row_length):
        for column in range(column_length):
            tree = map[row][column]
            if tree.scenic_score > highest_scenic_score:
                highest_scenic_score = tree.scenic_score
    return highest_scenic_score

if __name__ == "__main__":
    main()
