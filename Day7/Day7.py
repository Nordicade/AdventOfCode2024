import sys

f = open(sys.argv[1],"r")
contents = f.read()
f.close()
print(contents)
contents = contents.split('\n')


class Node:
  def __init__(self, row, col, letter, direction):
    self.row = row
    self.col = col
    self.letter = letter
    self.direction = direction

def partOne():
    sum = 0
    return sum


def partTwo():
    sum = 0
    return sum

print('---')
print(partOne())
print(partTwo())
