file = open("Day 1/input.txt", 'r')
numbers = []

increase = 0

for line in file:
    numbers.append(int(line))

for i in range(len(numbers)-2) :

    if i == 0:
        pass

    elif numbers[i]+ numbers[i+1]+ numbers[i+2] > numbers[i-1]+numbers[i]+numbers[i+1]:
        increase += 1

    else:
        pass

print(increase)

