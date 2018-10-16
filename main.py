
#State: (x1,y1) if the block is vertical else (x1,y1), (x2,y2)

#S(x): x is either up, down, right or left. It returns false(illegal move) or the next state.

#Initial state [3][3] and [4][3]

#Step cost: 1 for every state transformation.



import heapq
"""


"""
class State(object):

    def __init__(self, coords, stance):
        self.coords = coords # If the stance is horizontal, the first tuple in the coords array must be the upper or left part of the block.
        self.stance = stance
        self.cost   = -1
        if stance == "vertical":
            self.id  = (coords[0])
        else:
            self.id = (coords[0], coords[1])
    def __lt__(self, other):
        if self.cost != other.cost:
            return self.cost < other.cost
        else:
            return False

def loadBoard(filename):
    boardMatrix = []
    board = open(filename, "r")
    lines = board.readlines()
    count = 0
    for line in lines:

        line = str(line)
        row = line[:-1].split(' ') if count < (len(lines) - 1) else line.split(' ')
        boardMatrix.append(row)
        count += 1
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
            #True if ((boardMatrix[i][j+1] == "S") or (boardMatrix[i+1][j] == "S")) else False
            if boardMatrix[i][j + 1] == "S":
                return (i, j+1)
            elif boardMatrix[i+1][j] == "S":
                return (i+1, j)
            else:
                return False
        elif j == (len(boardMatrix[i])-1):
            #True if (((boardMatrix[i][j-1]) == "S") or (boardMatrix[i+1][j])) else False
            if boardMatrix[i][j-1] == "S":
                return (i, j-1)
            elif boardMatrix[i+1][j] == "S":
                return (i+1, j)
            else:
                return False
        else:
            #True if ((boardMatrix[i][j+1] == "S") or (boardMatrix[i][j-1] == "S") or (boardMatrix[i+1][j] == "S")) else False
            if boardMatrix[i][j+1] == "S":
                return (i, j+1)
            elif boardMatrix[i][j-1] == "S":
                return (i, j-1)
            elif boardMatrix[i+1][j] == "S":
                return (i+1, j)
            else:
                return False
    elif i == len(boardMatrix)-1:
        if j == 0:
            #True if ((boardMatrix[i][j+1] == "S") or (boardMatrix[i-1][j] == "S")) else False
            if boardMatrix[i][j+1] == "S":
                return (i, j+1)
            elif boardMatrix[i-1][j] == "S":
                return (i-1, j)
            else:
                return False
        elif j == (len(boardMatrix[i]) - 1):
            #True if ((boardMatrix[i][j-1] == "S") or ( boardMatrix[i-1][j-1] == "S")) else False
            if boardMatrix[i][j-1] == "S":
                return (i, j-1)
            elif boardMatrix[i-1][j-1] == "S":
                return boardMatrix[i-1][j-1]
            else:
                return False
        else:
            #True if ((boardMatrix[i][j+1] == "S") or (boardMatrix[i][j-1] == "S") or (boardMatrix[i-1][j] == "S")) else False
            if boardMatrix[i][j+1] == "S":
                return (i, j+1)
            elif boardMatrix[i][j-1] == "S":
                return (i, j-1)
            elif boardMatrix[i-1][j] == "S":
                return (i-1, j)
            else:
                return False
    else:
        if j == 0:
           # True if ((boardMatrix[i][j+1] == "S") or (boardMatrix[i-1][j] == "S") or (boardMatrix[i+1][j] == "S")) else False
            if boardMatrix[i][j+1] == "S":
                return (i, j+1)
            elif boardMatrix[i-1][j] == "S":
                return (i-1, j)
            elif boardMatrix[i+1][j] == "S":
                return (i+1, j)
            else:
                return False
        elif j == (len(boardMatrix[i]) - 1):
            #True if (((boardMatrix[i][j-1] == "S") or (boardMatrix[i-1][j]) == "S") or (boardMatrix[i+1][j] == "S")) else False
            if boardMatrix[i][j-1] == "S":
                return (i, j-1)
            elif boardMatrix[i-1][j] == "S":
                return (i-1, j)
            elif boardMatrix[i+1][j] == "S":
                return (i+1, j)
            else:
                return False
        else:
            #True if ((boardMatrix[i+1][j] == "S") or (boardMatrix[i-1][j] == "S") or (boardMatrix[i][j+1] == "S") or (boardMatrix[i][j-1] == "S")) else False
            if boardMatrix[i+1][j] == "S":
                return (i+1, j)
            elif boardMatrix[i-1][j] == "S":
                return (i-1, j)
            elif boardMatrix[i][j+1] == "S":
                return (i, j+1)
            elif boardMatrix[i][j-1] == "S":
                return (i, j-1)
            else:
                return False






def getInitialState(boardMatrix):
    for i in range(len(boardMatrix)):
        for j in range(len(boardMatrix[i])):
            if boardMatrix[i][j] == "S":
                secondSquareCoords = checkHorizontal(boardMatrix, i, j)
                if secondSquareCoords:
                    if secondSquareCoords[0] == i: # If the X2 and X1 are equal, then the block is horizontal(parallel to the board) and extends from left to right.
                        return State([(i, j),secondSquareCoords], "horizontal-horizontal")
                    else:
                        return State([(i, j), secondSquareCoords], "horizontal-vertical")
                else:
                    return State([(i, j)], "vertical")

def getGoalStateCoords(boardMatrix):
    for i in range(len(boardMatrix)):
        for j in range(len(boardMatrix[i])):
            if boardMatrix[i][j] == "G":
                return (i, j)

def moveVerticalBlock(boardMatrix, command, state, queue, visited, stateCosts):
    if command == "up":
        if ((state.coords[0][0] > 1) and (boardMatrix[state.coords[0][0] - 2][state.coords[0][1]] != "X") and (boardMatrix[state.coords[0][0] - 1][state.coords[0][1]] != "X")):
            newSt = State([(state.coords[0][0] - 2, state.coords[0][1]), (state.coords[0][0] - 1, state.coords[0][1])], "horizontal-vertical")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:
                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)
    elif command == "down":
        if ((state.coords[0][0] < (len(boardMatrix) - 2)) and (boardMatrix[state.coords[0][0] + 2][state.coords[0][1]] != "X") and (boardMatrix[state.coords[0][0] + 1][state.coords[0][1]] != "X")):
            newSt = State([(state.coords[0][0] + 1, state.coords[0][1]), (state.coords[0][0] + 2, state.coords[0][1])], "horizontal-vertical")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:
                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)
    elif command == "left":
        if ((state.coords[0][1] > 1) and (boardMatrix[state.coords[0][0]][state.coords[0][1] - 2] != "X") and (boardMatrix[state.coords[0][0]][state.coords[0][1] - 1] != "X")):
            newSt = State([(state.coords[0][0], state.coords[0][1] - 2 ), ( state.coords[0][0], state.coords[0][1] - 1)], "horizontal-horizontal")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:
                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)
    elif command == "right":
        if ((state.coords[0][1] < (len(boardMatrix[0]) - 2)) and (boardMatrix[state.coords[0][0]][state.coords[0][1] + 2] != "X") and (boardMatrix[state.coords[0][0]][state.coords[0][1] + 1] != "X")):
            newSt = State([(state.coords[0][0], state.coords[0][1] + 1 ), (state.coords[0][0], state.coords[0][1] + 2 )], "horizontal-horizontal" )
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:
                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)
def moveHorizontalVerticalBlock(boardMatrix, command, state, queue, visited, stateCosts):
    if command == "up":
        if (state.coords[0][0] != 0) and (boardMatrix[state.coords[0][0] - 1][state.coords[0][1]] != "X"):
            newSt = State([(state.coords[0][0] - 1, state.coords[0][1])], "vertical")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:
                print("WOW")

                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)
    elif command == "down":
        if (state.coords[1][0] != (len(boardMatrix) - 1)) and (boardMatrix[state.coords[1][0] + 1][state.coords[1][1]] != "X"):
            newSt = State([(state.coords[0][0] + 2, state.coords[0][1])], "vertical")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:
                print("WOW")

                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)
    elif command == "left":
        if ((state.coords[0][1] != 0 ) and (boardMatrix[state.coords[0][0]][state.coords[0][1] - 1] != "X") and (boardMatrix[state.coords[1][0]][state.coords[1][1] - 1] != "X")):
            newSt = State([(state.coords[0][0], state.coords[0][1] - 1), (state.coords[1][0], state.coords[1][1] - 1)], "horizontal-vertical")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:
                print("WOW")

                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)

    elif command == "right":
        if (state.coords[0][1] != (len(boardMatrix[0]) - 1) and (boardMatrix[state.coords[0][0]][state.coords[0][1] + 1] != "X") and (boardMatrix[state.coords[1][0]][state.coords[1][1] + 1] != "X")):
            newSt = State([(state.coords[0][0], state.coords[0][1] + 1), (state.coords[1][0], state.coords[1][1] + 1)], "horizontal-vertical")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:
                print("WOW")

                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)

def moveHorizontalHorizontalBlock(boardMatrix, command, state, queue, visited, stateCosts):

    if command == "up":
        if ((state.coords[0][0] != 0) and (boardMatrix[state.coords[0][0] - 1][state.coords[0][1]] != "X") and (boardMatrix[state.coords[1][0] - 1][state.coords[1][1]] != "X")):
            newSt = State([(state.coords[0][0]-1, state.coords[0][1]), (state.coords[1][0]-1, state.coords[1][1])], "horizontal-horizontal")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:

                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)
    elif command == "down":
        if ((state.coords[0][0] != (len(boardMatrix) - 1)) and (boardMatrix[state.coords[0][0] + 1][state.coords[0][1]] != "X") and (boardMatrix[state.coords[1][0] + 1][state.coords[1][1]] != "X")):
            newSt = State([(state.coords[0][0] + 1, state.coords[0][1]), (state.coords[1][0] + 1, state.coords[1][1])], "horizontal-horizontal")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:

                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)
    elif command == "left":
        if ((state.coords[0][1] != 0) and (boardMatrix[state.coords[0][0]][state.coords[0][1] - 1]) != "X"):
            newSt = State([(state.coords[0][0], state.coords[0][1] - 1)], "vertical")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:

                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)
    elif command == "right":
        if ((state.coords[1][1] != (len(boardMatrix[0]) - 1)) and (boardMatrix[state.coords[1][0]][state.coords[1][1] + 1] != "X")):
            newSt = State([(state.coords[1][0], state.coords[1][1] + 1)], "vertical")
            newSt.cost = state.cost + 1
            if newSt.id not in stateCosts:
                stateCosts[newSt.id] = newSt.cost
            elif newSt.cost < stateCosts[newSt.id]:
                stateCosts[newSt.id] = newSt.cost
            if newSt.id not in visited:
                queue.append(newSt)
                heapq.heapify(queue)

def successorState(boardMatrix, state, queue, visited, stateCosts):
     #TODO Control if state is already visited BEFORE calling this function.
     if state.stance == "vertical":
        moveVerticalBlock(boardMatrix, "up", state, queue, visited, stateCosts)
        moveVerticalBlock(boardMatrix, "down", state, queue, visited, stateCosts)
        moveVerticalBlock(boardMatrix, "left", state, queue, visited, stateCosts)
        moveVerticalBlock(boardMatrix, "right", state, queue, visited, stateCosts)
     elif state.stance == "horizontal-vertical":
        moveHorizontalVerticalBlock(boardMatrix, "up", state, queue, visited, stateCosts)
        moveHorizontalVerticalBlock(boardMatrix, "down", state, queue, visited, stateCosts)
        moveHorizontalVerticalBlock(boardMatrix, "left", state, queue, visited, stateCosts)
        moveHorizontalVerticalBlock(boardMatrix, "right", state, queue, visited, stateCosts)
     elif state.stance == "horizontal-horizontal":
         moveHorizontalHorizontalBlock(boardMatrix, "up", state, queue, visited, stateCosts)
         moveHorizontalHorizontalBlock(boardMatrix, "down", state, queue, visited, stateCosts)
         moveHorizontalHorizontalBlock(boardMatrix, "left", state, queue, visited, stateCosts)
         moveHorizontalHorizontalBlock(boardMatrix, "right", state, queue, visited, stateCosts)
     else:
         print("STATE STANCE IS INVALID.")



queue = []
visited = {}
stateCosts = {}
boardMatrix = loadBoard("board2.txt")
goalStateId = getGoalStateCoords(boardMatrix)
print(goalStateId)
initState = getInitialState(boardMatrix)
initState.cost = 0
stateCosts[initState.id] = initState.cost

queue.append(initState)
goalStateReached = False

"""
Psuedo-code:

while game is not over
    if queue is empty, terminate.
    state is popped from queue
    check if state is already visited.
    if not visited then visit it
        look for successor states
        add them to stateCost if they were not seen before
        otherwise update their costs if the new cost is less.
    if goal state is seen and its cost is lesser than the first element in the heap, terminate the algorithm.

"""
while not goalStateReached:

    if len(queue) > 0:
        currentState = queue.pop(0)
        heapq.heapify(queue) # Maintain the heap property of the queue(frontier).
        if currentState.id not in visited:
            successorState(boardMatrix, currentState, queue, visited, stateCosts)

           # if (goalStateMinCost > -1) and (goalStateMinCost > stateCosts[goalStateId]):
           #     goalStateMinCost = stateCosts[goalStateId]
            visited[currentState.id] = True
        if goalStateId in stateCosts:
            if len(queue) == 0:
                    print("?d")
                    print("Minimum amount of steps required to get to the goal state is:", stateCosts[goalStateId])

                    goalStateReached = True
            elif stateCosts[goalStateId] < queue[0].cost:
                print(queue[0].cost)
                print("Minimum amount of steps required to get to the goal state is:", stateCosts[goalStateId])
                goalStateReached = True
    else:
        print("FAILURE")
