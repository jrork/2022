file1 = open("calories.data")
 # Reading from file
input = file1.readlines()
file1.close()

elves_calorie_count = []
current = 0

for line in input:
    if line != '\n':
        current += int(line)
    else:
        elves_calorie_count.append(current)
        current = 0

elves_calorie_count.sort(reverse=True)
print("Elf 1 calorie count is " + str(elves_calorie_count[0]))
print("Elf 2 calorie count is " + str(elves_calorie_count[1]))
print("Elf 3 calorie count is " + str(elves_calorie_count[2]))

top3 = 0
for i in range(3):
    top3 += elves_calorie_count[i]
print("Top 3 combined is " + str(top3))
