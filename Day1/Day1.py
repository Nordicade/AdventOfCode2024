import sys

f = open(sys.argv[1],"r")
contents = f.read()
f.close()
print(contents)
contents = contents.split('\n')

leftList = []
rightList = []

for line in contents:
    left, right = line.split('   ')
    leftList.append(int(left))
    rightList.append(int(right))


def partOne(leftList, rightList):
    leftList.sort()
    rightList.sort()
    sum = 0
    for index in range(len(leftList)):
        sum = sum + abs(rightList[index] - leftList[index])
    return sum

def partTwo(leftList, rightList):
    # convert right to map and increment for frequency
    # use left list as key and sum = index + rightMap[index]
    rightMap = {}
    for val in rightList:
        if val in rightMap:
            rightMap[val] = rightMap[val] + 1
        else:
            rightMap[val] = 1
    
    sum = 0
    for val in leftList:
        if val in rightMap:
            sum = sum + val * rightMap[val]

    return sum

print('---')
print(partOne(leftList, rightList))
print(partTwo(leftList, rightList))
