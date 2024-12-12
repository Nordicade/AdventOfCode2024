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
  def __init__(self, row, col, letter):
    self.row = row
    self.col = col
    self.letter = letter

def printAllNodes(nodes):
    for rows in nodes:
        for node in rows:   
            print("("+str(node.row) + " , " + str(node.col) + ')' + ': ' + node.letter)

nodeGrid = [[0]*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        nodeGrid[i][j] = Node(i, j, grid[i][j])

def nextStep():
    for i in range(rows):
        for j in range(cols):
            # handle goard moving up
            if nodeGrid[i][j].letter == up:
                # if we go off page, we are done
                if i - 1 < 0:
                    return True
                else:
                    # if we hit a '#', we rotate to right
                    if nodeGrid[i-1][j].letter == obstacle:
                        nodeGrid[i][j].letter = right
                    else:
                        # otherwise, move the guard forward and change current letter to 'X'
                        nodeGrid[i][j].letter = path
                        nodeGrid[i - 1][j].letter = up
                return False
            # handle goard moving right
            elif nodeGrid[i][j].letter == right:
                # if we go off page, we are done
                if j + 1 >= cols:
                    return True
                else:
                    # if we hit a '#', we rotate to guard's right, which is down
                    if nodeGrid[i][j + 1].letter == obstacle:
                        nodeGrid[i][j].letter = down
                    else:
                        # otherwise, move the guard forward and change current letter to 'X'
                        nodeGrid[i][j].letter = path
                        nodeGrid[i][j + 1].letter = right
                return False
            # handle goard moving down
            elif nodeGrid[i][j].letter == down:
                # if we go off page, we are done
                if i + 1 >= rows:
                    return True
                else:
                    # if we hit a '#', we rotate to guard's right, which is left
                    if nodeGrid[i + 1][j].letter == obstacle:
                        nodeGrid[i][j].letter = left
                    else:
                        # otherwise, move the guard forward and change current letter to 'X'
                        nodeGrid[i][j].letter = path
                        nodeGrid[i + 1][j].letter = down
                return False               
            # handle goard moving left
            elif nodeGrid[i][j].letter == left:
                # if we go off page, we are done
                if j - 1 < 0:
                    return True
                else:
                    # if we hit a '#', we rotate to guard's right, which is up
                    if nodeGrid[i][j - 1].letter == obstacle:
                        nodeGrid[i][j].letter = up
                    else:
                        # otherwise, move the guard forward and change current letter to 'X'
                        nodeGrid[i][j].letter = path
                        nodeGrid[i][j - 1].letter = left
                return False       

def partOne():
    sum = 0
    finished = False
    while(not finished):
        finished = nextStep()
    for i in range(rows):
        for j in range(cols):
            if nodeGrid[i][j].letter == path:
                sum = sum + 1
    sum = sum + 1 # to account for the guard still being on the map
    return sum


def partTwo():
    sum = 0
    return sum

print('---')
print(partOne())
print(partTwo())
