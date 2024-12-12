import sys
import random

f = open(sys.argv[1],"r")
contents = f.read()
f.close()
print(contents)
contents = contents.split('\n\n')
rules = contents[0].split('\n')
pages = contents[1].split('\n')

ruleMap = {}

def isPageGood(page):
    pageSet = [ int(x) for x in page.split(',')]
    pageSet.reverse()
    added = []
    safe = True
    # For 75 in 75,47,61,53,29
    for step in pageSet:
        # ruleMap[75] = { / / }
        if not safe:
            break
        if step in ruleMap:
            for curr in added:
                if curr in ruleMap[step] and ruleMap[step][curr]:
                    safe = False
                    break
        added.insert(0, step)
    if  safe and len(added) == len(pageSet):
        return True
    else:
        return False

def divideGoodAndBadPages():
    good = []
    bad = []

    for rule in rules:
        split = rule.split('|')
        # L must come before R
        # we store ruleMap[R] = {L, L, L}
        left = int(split[0])
        right = int(split[1])
        if not right in ruleMap:
            ruleMap[right] = {left: True}
        else:
            ruleMap[right][left] = True

    for page in pages:
        pageSet = [ int(x) for x in page.split(',')]
        pageSet.reverse()
        if isPageGood(page):
            good.append(pageSet)
        else:
            bad.append(pageSet)

    return good, bad

def partOne(good):
    sum = 0
    for pageSet in good:
        sum = sum + pageSet[(len(pageSet) // 2)]
        safe = True
        added = []
            
    return sum


def partTwo(bad):
    sum = 0
    return sum


good, bad = divideGoodAndBadPages()
print('---')
print(partOne(good))
print(partTwo(bad))

# Idea:
# Create nested dicts
# We have a rule 1 | 3 (one must come before 3)
# We want to verify the following "1 2 3 4"
# place 4
# want to place 3, check the dict at [3] = {1} 
# 3 does not exist yet in the 'placed' list

# also have 2 | 1 (two must come before 1)
# we have already placed 3, 4
# read 2, and place becuase [2] = { // empty}

# want to place 1, [1] = {2}
# fail