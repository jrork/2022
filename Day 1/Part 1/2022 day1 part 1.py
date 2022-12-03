file1 = open("calories.data")
 # Reading from file
input = file1.readlines()
file1.close()

largest = 0
current = 0

for line in input:
    if line != '\n':
        print("Line is " + line)
        current += int(line)
        print("Current is " + str(current))
    else:
        print(" ")
        print("Current is " + str(current))
        print("Largest is " + str(largest))
        if current > largest:
            largest = current
            current = 0
        else:
            current = 0
print(largest)