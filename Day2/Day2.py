import sys

f = open(sys.argv[1],"r")
contents = f.read()
f.close()
print(contents)
contents = contents.split('\n')

levels = []
for line in contents:
    levels.append(line.split(' '))


def isLevelSafe(level):
    descending = (int(level[0]) - int(level[1])) > 0
    safe = True
    for index in range(len(level) - 1):
        diff = int(level[index]) - int(level[index + 1])
        if descending: 
            if diff < 0 or abs(diff) < 1 or abs(diff) > 3:
                safe = False
                break
        else: 
            if diff > 0 or abs(diff) < 1 or abs(diff) > 3:
                safe = False
                break
    return safe


def partOne(levels):
    sum = 0
    for level in levels:
        safe = isLevelSafe(level)
        if safe:
            sum = sum + 1
    return sum


def partTwo(levels):
    sum = 0
    for level in levels:
        wholeLevelSafe = isLevelSafe(level)
        if wholeLevelSafe:
            sum = sum + 1
        else:
            for index in range(len(level)):
                reducedLevel = level.copy()
                reducedLevel.pop(index)
                reducedSafe = isLevelSafe(reducedLevel)
                if reducedSafe: 
                    sum = sum + 1
                    break
                
    return sum

print('---')
print(partOne(levels))
print(partTwo(levels))
