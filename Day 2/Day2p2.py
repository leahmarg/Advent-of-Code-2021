file = open("Day 2/input.txt", 'r')
direction = []

depth = 0
horizontal = 0
aim = 0

for line in file:
    direction.append(line)

    directionNum = list(map(lambda sub:int(''.join(
      [ele for ele in sub if ele.isnumeric()])), direction))

for i in range(len(direction)):
    if "forward" in direction[i]:
        horizontal += directionNum[i]
        depth = depth + (directionNum[i] * aim)

    elif "up" in direction[i]:
        aim -= directionNum[i]

    else:
        aim += directionNum[i]

finalPosition = depth * horizontal

print(finalPosition)



