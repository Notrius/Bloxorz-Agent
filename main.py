
#State: (x1,y1) if the block is vertical else (x1,y1), (x2,y2)

#S(x): x is either up, down, right or left. It returns false(illegal move) or the next state.

#Initial state [3][3] and [4][3]

#Step cost: 1 for every state transformation.

"""


"""
class State(object):

    def __init__(self, coords, stance):
        self.coords = coords
        self.stance = stance
        self.cost   = 1

def loadBoard():
    boardMatrix = []
    board = open("board.txt", "r")
    for line in board.readlines():
        row = line.split(' ')
        boardMatrix.append(row)
    board.close()
    return boardMatrix

def printBoard(boardMatrix):
    boardMatrix = loadBoard()
    for i in range(len(boardMatrix)):
        for j in range(len(boardMatrix[i])):
            print(boardMatrix[i][j])

def checkHorizontal(boardMatrix, i, j):
    if i == 0:
        if j == 0:
            (i, j+1) if ((boardMatrix[i][j+1] == "S") or (boardMatrix[i+1][j] == "S")) else False
        elif j == (len(boardMatrix[i])-1):
            True if (((boardMatrix[i][j-1]) == "S") or (boardMatrix[i+1][j])) else False
        else:
            True if ((boardMatrix[i][j+1] == "S") or (boardMatrix[i][j-1] == "S") or (boardMatrix[i+1][j] == "S")) else False
    elif i == len(boardMatrix)-1:
        if j == 0:
            True if ((boardMatrix[i][j+1] == "S") or (boardMatrix[i-1][j] == "S")) else False
        elif j == (len(boardMatrix[i]) - 1):
            True if ((boardMatrix[i][j-1] == "S") or ( boardMatrix[i-1][j-1] == "S")) else False
        else:
            True if ((boardMatrix[i][j+1] == "S") or (boardMatrix[i][j-1] == "S") or (boardMatrix[i-1][j] == "S")) else False
    else:
        if j == 0:
            True if ((boardMatrix[i][j+1] == "S") or (boardMatrix[i-1][j] == "S") or (boardMatrix[i+1][j] == "S")) else False
        elif j == (len(boardMatrix[i]) - 1):
            True if (((boardMatrix[i][j-1] == "S") or (boardMatrix[i-1][j]) == "S") or (boardMatrix[i+1][j] == "S")) else False
        else:
            True if ((boardMatrix[i+1][j] == "S") or (boardMatrix[i-1][j] == "S") or (boardMatrix[i][j+1] == "S") or (boardMatrix[i][j-1] == "S")) else False





def getInitialState(boardMatrix):
    for i in range(len(boardMatrix)):
        for j in range(len(boardMatrix[i])):
            if boardMatrix[i][j] == "S":
               return True #return State(i) if checkHorizontal(boardMatrix, i, j)



def successorStates(queue, state, command):
    x = y


queue = []
boardMatrix = loadBoard()
checkHorizontal(boardMatrix, 0, 5)



