import sys

f = open(sys.argv[1],"r")
contents = f.readlines()
f.close()

rows, cols = (0,0)
for lines in contents:
    cols = len(lines)
    rows = len(contents)

grid = [row.strip() for row in contents]
print(contents)

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

    # handle goard moving up
    if nodeGrid[i][j].letter == up:
        # if we go off page, we are done
        if i - 1 < 0:
            return True, i, j
        else:
            # if we hit a '#', we rotate to right
            if nodeGrid[i-1][j].letter == obstacle:
                nodeGrid[i][j].letter = right
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = up
                nodeGrid[i - 1][j].letter = up
                return False, i - 1, j
    # handle goard moving right
    elif nodeGrid[i][j].letter == right:
        # if we go off page, we are done
        if j + 1 >= cols:
            return True, i, j
        else:
            # if we hit a '#', we rotate to guard's right, which is down
            if nodeGrid[i][j + 1].letter == obstacle:
                nodeGrid[i][j].letter = down
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = right
                nodeGrid[i][j + 1].letter = right
                return False, i, j + 1
    # handle goard moving down
    elif nodeGrid[i][j].letter == down:
        # if we go off page, we are done
        if i + 1 >= rows:
            return True, i, j
        else:
            # if we hit a '#', we rotate to guard's right, which is left
            if nodeGrid[i + 1][j].letter == obstacle:
                nodeGrid[i][j].letter = left
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = down
                nodeGrid[i + 1][j].letter = down
                return False, i + 1, j 
    # handle goard moving left
    elif nodeGrid[i][j].letter == left:
        # if we go off page, we are done
        if j - 1 < 0:
            return True, i, j
        else:
            # if we hit a '#', we rotate to guard's right, which is up
            if nodeGrid[i][j - 1].letter == obstacle:
                nodeGrid[i][j].letter = up
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = left
                nodeGrid[i][j - 1].letter = left
                return False, i, j - 1
            
def nextStepWithAntiLoopTechnology(guardRow, guardCol):
    i = guardRow
    j = guardCol

    # handle goard moving up
    if nodeGrid[i][j].letter == up:
        # if we go off page, we are done
        if i - 1 < 0:
            return True, i, j, False
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
                return False, i - 1, j
    # handle goard moving right
    elif nodeGrid[i][j].letter == right:
        # if we go off page, we are done
        if j + 1 >= cols:
            return True, i, j, False
        else:
            # if we hit a '#', we rotate to guard's right, which is down
            if nodeGrid[i][j + 1].letter == obstacle:
                nodeGrid[i][j].letter = down
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = right
                nodeGrid[i][j + 1].letter = right
                return False, i, j + 1
    # handle goard moving down
    elif nodeGrid[i][j].letter == down:
        # if we go off page, we are done
        if i + 1 >= rows:
            return True, i, j, False
        else:
            # if we hit a '#', we rotate to guard's right, which is left
            if nodeGrid[i + 1][j].letter == obstacle:
                nodeGrid[i][j].letter = left
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = down
                nodeGrid[i + 1][j].letter = down
                return False, i + 1, j 
    # handle goard moving left
    elif nodeGrid[i][j].letter == left:
        # if we go off page, we are done
        if j - 1 < 0:
            return True, i, j, False
        else:
            # if we hit a '#', we rotate to guard's right, which is up
            if nodeGrid[i][j - 1].letter == obstacle:
                nodeGrid[i][j].letter = up
                return False, i, j
            else:
                # otherwise, move the guard forward and change current letter to 'X'
                nodeGrid[i][j].letter = path
                nodeGrid[i][j].direction = left
                nodeGrid[i][j - 1].letter = left
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
    startingRow, startingCol, startingLetter = buildNodeGrid()

    # Foreach position in solutionPath; place an obstacle letter
    for block in solutionPath:
        blockRow = block.row
        blockCol = block.col

        nodeGrid[blockRow][blockCol].letter = obstacle
        nodeGrid[startingRow][startingCol] = startingLetter

        # nodeGrid is updated with potential block. Step through and see if we run into loop
        sum = 0
        finished = False
        nextRow = startingRow
        nextCol = startingCol
        looped = False
        while(not finished):
            finished, i, j, isLoop  = nextStepWithAntiLoopTechnology(nextRow, nextCol)
            nextRow = i
            nextCol = j
            looped = isLoop
        if looped:
            sum = sum + 1

        return sum


print('---')
print(partOne())
print(partTwo())
