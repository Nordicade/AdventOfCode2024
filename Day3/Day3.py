import sys
import re

f = open(sys.argv[1],"r")
contents = f.read()
f.close()

contents = contents.replace('\n', '')


def partOne(content):
    sum = 0
    multRegex = "mul\(\d{1,3},\d{1,3}\)"
    allMatches = re.findall(multRegex, content)
    for match in allMatches:
        split = match.split(',')
        left = int(split[0][4:])
        right = int(split[1][:-1])
        sum = sum + (left * right)
    return sum


def partTwo(content):
    multRegex = "mul\(\d{1,3},\d{1,3}\)"
    doDontRegex = "(?<=do\(\))(.*?)(?=don't\(\))"
    # cheeky little do() to start with enable to True
    content = 'do()' + content + 'don\'t()'
    sum = 0
    doDontMatches = re.findall(doDontRegex, content, re.M | re.U)
    for match in doDontMatches:
        multMatches = re.findall(multRegex, match)
        for match in multMatches:
            split = match.split(',')
            left = int(split[0][4:])
            right = int(split[1][:-1])
            sum = sum + (left * right)
    return sum

print('\n---\n')
print(partOne(contents))
print(partTwo(contents))
