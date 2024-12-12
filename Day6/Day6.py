import sys

f = open(sys.argv[1],"r")
contents = f.readlines()
f.close()

rows, cols = (0,0)
for lines in contents:
    cols = len(lines)
    rows = len(contents)

grid = [row.strip() for row in contents]

up = '^'
left ='<'
right = '>'
down = 'v'
obstacle = '#'
path = 'X'

class Node:
  def __init__(self, row, col, letter, direction):
    self.row = row
    self.col = col
    self.letter = letter
    self.direction = direction

def printAllNodes(nodes):
    for rows in nodes:
        for node in rows:   
            print("("+str(node.row) + " , " + str(node.col) + ')' + ': ' + node.letter + " , " + node.direction)

def printGrid(nodes):
    for rows in nodes:
        line = ''
        for node in rows:
            line = line + node.letter
        print(line)

nodeGrid = [[0]*cols for _ in range(rows)]
solutionPath = []

def buildNodeGrid():
    startingRow = 0
    startingCol = 0
    startingLetter = 'panic'
    for i in range(rows):
        for j in range(cols):
            nodeGrid[i][j] = Node(i, j, grid[i][j], '')
            curr = grid[i][j]
            if curr == down or curr == left or curr == right or curr == up:
                startingRow = i
                startingCol = j
                startingLetter = grid[i][j]
    return startingRow, startingCol, startingLetter

def nextStep(guardRow, guardCol):
    i = guardRow
    j = guardCol

    # handle guard moving up
    if nodeGrid[i][j].letter == up:
        # if we go off page, we are done
        if i - 1 < 0:
            return True, i, j
        else:
            # if we hit a '#', we rotate to right
            if nodeGrid[i-1][j].letter == obstacle:
                nodeGrid[i][j].letter = right
                nodeGrid[i][j].direction = right
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = up
                nodeGrid[i - 1][j].letter = up
                nodeGrid[i - 1][j].direction = up
                return False, i - 1, j
    # handle guard moving right
    elif nodeGrid[i][j].letter == right:
        # if we go off page, we are done
        if j + 1 >= cols:
            return True, i, j
        else:
            # if we hit a '#', we rotate to guard's right, which is down
            if nodeGrid[i][j + 1].letter == obstacle:
                nodeGrid[i][j].letter = down
                nodeGrid[i][j].direction = down
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = right
                nodeGrid[i][j + 1].letter = right
                nodeGrid[i][j + 1].direction = right
                return False, i, j + 1
    # handle guard moving down
    elif nodeGrid[i][j].letter == down:
        # if we go off page, we are done
        if i + 1 >= rows:
            return True, i, j
        else:
            # if we hit a '#', we rotate to guard's right, which is left
            if nodeGrid[i + 1][j].letter == obstacle:
                nodeGrid[i][j].letter = left
                nodeGrid[i][j].direction = left
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = down
                nodeGrid[i + 1][j].letter = down
                nodeGrid[i + 1][j].direction = down
                return False, i + 1, j 
    # handle guard moving left
    elif nodeGrid[i][j].letter == left:
        # if we go off page, we are done
        if j - 1 < 0:
            return True, i, j
        else:
            # if we hit a '#', we rotate to guard's right, which is up
            if nodeGrid[i][j - 1].letter == obstacle:
                nodeGrid[i][j].letter = up
                nodeGrid[i][j].direction = up
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = left
                nodeGrid[i][j - 1].letter = left
                nodeGrid[i][j - 1].direction = left
                return False, i, j - 1
            
def partOne():
    startingRow, startingCol, _ = buildNodeGrid()
    sum = 0
    finished = False
    nextRow = startingRow
    nextCol = startingCol
    while(not finished):
        finished, i, j  = nextStep(nextRow, nextCol)
        nextRow = i
        nextCol = j
    for i in range(rows):
        for j in range(cols):
            if nodeGrid[i][j].letter == path or nodeGrid[i][j].letter == down or nodeGrid[i][j].letter == left or nodeGrid[i][j].letter == right or nodeGrid[i][j].letter == up:
                sum = sum + 1
                solutionPath.append(nodeGrid[i][j])
    return sum


def partTwo():
    sum = 0
    # Foreach position in solutionPath; place an obstacle letter
    for block in solutionPath:
        startingRow, startingCol, startingLetter = buildNodeGrid()
        blockRow = block.row
        blockCol = block.col

        nodeGrid[blockRow][blockCol].letter = obstacle
        nodeGrid[startingRow][startingCol].letter = startingLetter

        # nodeGrid is updated with potential block. Step through and see if we run into loop
        finished = False
        nextRow = startingRow
        nextCol = startingCol
        loopDetector = {}
        while(not finished):
            finished, i, j  = nextStep(nextRow, nextCol)
            loopKey = (i, j, nodeGrid[i][j].direction)
            if not finished and loopKey in loopDetector:
                sum = sum + 1
                break
            loopDetector[loopKey] = True
            nextRow = i
            nextCol = j

    return sum


print('---')
print(partOne())
print(partTwo())
