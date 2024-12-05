import sys

f = open(sys.argv[1],"r")
contents = f.readlines()
f.close()

rows, cols = (0,0)
for lines in contents:
    cols = len(lines)
    rows = len(contents)

grid = [row.rstrip('\n') for row in contents]

def check(currentRow, currentCol, letter):
    return grid[currentRow - 1][currentCol] == letter

def checkTop(currentRow, currentCol, letter):
    if currentRow - 1 < 0:
        return False
    if grid[currentRow - 1][currentCol] == letter:
        return True
    return False
    
def checkBot(currentRow, currentCol, letter):
    if currentRow + 1 >= rows:
        return False
    if grid[currentRow + 1][currentCol] == letter:
        return True
    return False
    
def checkRight(currentRow, currentCol, letter):
    if currentCol + 1 >= cols:
        return False
    if grid[currentRow][currentCol + 1] == letter:
        return True
    return False
    
def checkLeft(currentRow, currentCol, letter):
    if currentCol - 1 < 0:
        return False
    if grid[currentRow][currentCol - 1] == letter:
        return True
    return False

def checkTopLeft(currentRow, currentCol, letter):
    if currentCol - 1 < 0 or currentRow - 1 < 0:
        return False
    if grid[currentRow - 1][currentCol - 1] == letter:
        return True
    return False

def checkTopRight(currentRow, currentCol, letter):
    if currentCol + 1 >= cols or currentRow - 1 < 0:
        return False
    if grid[currentRow - 1][currentCol + 1] == letter:
        return True
    return False

def checkBotLeft(currentRow, currentCol, letter):
    if currentCol - 1 < 0 or currentRow + 1 >= rows:
        return False
    if grid[currentRow + 1][currentCol - 1] == letter:
        return True
    return False
    
def checkBotRight(currentRow, currentCol, letter):
    if currentCol + 1 >= cols or currentRow + 1 >= rows:
        return False
    if grid[currentRow + 1][currentCol + 1] == letter:
        return True
    return False

class Tile:
  def __init__(self, row, col, letter, direction):
    self.row = row
    self.col = col
    self.letter = letter
    self.direction = direction

def printAllTiles(tiles):
    for tile in tiles:    
        print("("+str(tile.row) + " , " + str(tile.col) + ')' + ': ' + tile.letter + " and going " + str(tile.direction))

def stepThroughQueue(queue, searchLetter):
    nextQueue = []
    while len(queue) > 0:
        curr = queue.pop()
        match curr.direction:
            case 'TL':
                if checkTopLeft(curr.row, curr.col, searchLetter):
                    nextQueue.append(Tile(curr.row - 1, curr.col - 1, searchLetter, 'TL'))
            case 'TOP':
                if checkTop(curr.row, curr.col, searchLetter):
                    nextQueue.append(Tile(curr.row - 1, curr.col, searchLetter, 'TOP'))
            case 'TR':
                if checkTopRight(curr.row, curr.col, searchLetter):
                    nextQueue.append(Tile(curr.row - 1, curr.col + 1, searchLetter, 'TR'))

            case 'L':
                if checkLeft(curr.row, curr.col, searchLetter):
                    nextQueue.append(Tile(curr.row, curr.col - 1, searchLetter, 'L'))
            case 'R':
                if checkRight(curr.row , curr.col, searchLetter):
                    nextQueue.append(Tile(curr.row , curr.col + 1, searchLetter, 'R'))

            case 'BL':
                if checkBotLeft(curr.row, curr.col, searchLetter):
                    nextQueue.append(Tile(curr.row + 1, curr.col - 1, searchLetter, 'BL'))
            case 'BOT':
                if checkBot(curr.row, curr.col, searchLetter):
                    nextQueue.append(Tile(curr.row + 1, curr.col, searchLetter, 'BOT'))
            case 'BR':
                if checkBotRight(curr.row, curr.col, searchLetter):
                    nextQueue.append(Tile(curr.row + 1, curr.col + 1, searchLetter, 'BR'))
    return nextQueue

def partOne():
    queue = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'X':
                queue.append(Tile(i, j, 'X', 'TL'))
                queue.append(Tile(i, j, 'X', 'TOP'))
                queue.append(Tile(i, j, 'X', 'TR'))
                queue.append(Tile(i, j, 'X', 'L'))
                queue.append(Tile(i, j, 'X', 'R'))
                queue.append(Tile(i, j, 'X', 'BL'))
                queue.append(Tile(i, j, 'X', 'BOT'))
                queue.append(Tile(i, j, 'X', 'BR'))

    mQueue = stepThroughQueue(queue, "M")
    aQueue = stepThroughQueue(mQueue, "A")
    sQueue = stepThroughQueue(aQueue, "S")

    return len(sQueue)

def partTwo():
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':
                # S.S
                # .A.
                # M.M
                if checkTopLeft(i, j, "S") and checkBotRight(i, j, "M") and checkBotLeft(i,j,"M") and checkTopRight(i, j, "S"):
                    sum = sum + 1
                # M.M
                # .A.
                # S.S
                if checkTopLeft(i, j, "M") and checkBotRight(i, j, "S") and checkBotLeft(i, j, "S") and checkTopRight(i, j, "M"):
                    sum = sum + 1
                # M.S
                # .A.
                # M.S
                if checkTopLeft(i, j, "M") and checkBotRight(i, j, "S") and checkBotLeft(i, j, "M") and checkTopRight(i, j, "S"):
                    sum = sum + 1
                # S.M
                # .A.
                # S.M
                if checkTopLeft(i, j, "S") and checkBotRight(i, j, "M") and checkBotLeft(i, j, "S") and checkTopRight(i, j, "M"):
                    sum = sum + 1
    return sum

print('---')
print(partOne())
print(partTwo())
