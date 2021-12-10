file = open("Day 3/input.txt", 'r')
data = []

for line in file:
    data.append(line.strip('\n'))

def getSilver(data):
    gammaRate = ''
    epsilonRate = ''

    bit = 0
    while bit < len(data[1]):
        ones = 0
        zeros  = 0 
        for i in range(len(data)):
            if data[i][bit] == '1':
                ones += 1
            else:
                zeros += 1

        if ones >= zeros: 
            gammaRate += '1'
            epsilonRate += '0'
        else:
            gammaRate += '0'
            epsilonRate += '1'
        bit += 1

    powerCon = (int(gammaRate, 2)) * (int(epsilonRate, 2))
    return powerCon

def getGold(data):
    
    bit = 0
    maxData = data.copy()
    while bit < len(maxData[0]):
        if len(maxData) == 1:
            break

        ones = []
        zeros = []
        for i in range(len(maxData)):
            if maxData[i][bit] == '1':
                ones.append(maxData[i])
            else:
                zeros.append(maxData[i])

        if len(ones) >= len(zeros): 
            maxData = ones
        else:
            maxData = zeros
        bit += 1

    bit = 0
    minData = data.copy()
    while bit < len(minData[0]):
        if len(minData) == 1:
            break

        ones = []
        zeros = []
        for i in range(len(minData)):
            if minData[i][bit] == '1':
                ones.append(minData[i])
            else:
                zeros.append(minData[i])

        if len(ones) >= len(zeros): 
            minData = zeros
        else:
            minData = ones
        bit += 1

    lifeSupport = (int(maxData[0], 2)) * (int(minData[0], 2))
    return lifeSupport

def main():
    print("The power consumption is:", getSilver(data))
    print("The life support rating is:", getGold(data))

main()
