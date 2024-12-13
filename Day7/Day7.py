import sys

f = open(sys.argv[1],"r")
contents = f.read()
f.close()
print(contents)
contents = contents.split('\n')

answers = []
values = []

for line in contents:
    answer = line.split(':')[0]
    value = line.split(':')[1]
    currValues = value.strip().split(' ')
    answers.append(answer)
    values.append(currValues)

def generateOperators(n):
    operatorsList = [f"{i:0{n}b}" for i in range(2**n)]
    for i in range(len(operatorsList)):
        curr = operatorsList[i]
        curr = curr.replace('0', '+')
        curr = curr.replace('1', '*')
        curr = curr + ' '
        operatorsList[i] = curr
    return operatorsList

def leftToRightEvaluation(equation):
    pointer = 0
    numberOfOperators = 0
    while pointer != len(equation):
        current = equation[0:pointer]
        lookAhead = equation[0:pointer+1]
        opCount = lookAhead.count('+')
        opCount = opCount + lookAhead.count('*')
        if opCount % 2 == 0 and opCount > 0:
            currResult = eval(current)
            currEquation = str(currResult) + equation[pointer:]
            return leftToRightEvaluation(currEquation)
        pointer = pointer + 1
    return eval(equation)

def isComboValid(answer, values, operators):
    valuesQueue = []
    operatorsQueue = []
    equation = ''
    for value in values:
        valuesQueue.insert(0, value)
    for operator in operators:
        operatorsQueue.insert(0, operator)
    for i in range(len(values)):
        equation = equation + valuesQueue.pop() + operatorsQueue.pop()
    output = leftToRightEvaluation(equation)
    return str(output) == answer

def partOne():
    sum = 0
    # i = index for the row 
    for i in range(len(answers)):
        combinations = generateOperators(len(values[i]) - 1)
        for j in range(len(combinations)):
            if isComboValid(answers[i], values[i], combinations[j]):
                sum = sum + int(answers[i])
                break
    return sum


def partTwo():
    sum = 0
    return sum

print('---')
print(partOne())
print(partTwo())
