

ComboIndices = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

EMPTY_SIGN = '.'
AI_SIGN = 'X'
OPPONENT_SIGN = 'O'


def gameWonBy(Board):
    for index in ComboIndices:
        if Board[index[0]] == Board[index[1]] == Board[index[2]] != EMPTY_SIGN:
            return Board[index[0]]
    return EMPTY_SIGN


def allMovesFromBoard(Board, sign):
    moveList = []
    for i, v in enumerate(Board):
        if v == EMPTY_SIGN:
            moveList.append(Board[:i] + sign + Board[i+1:])
    return moveList


def allMovesFromBoardList(BoardList, sign):
    moveList = []
    for Board in BoardList:
        moveList.extend(allMovesFromBoard(Board, sign))
    return moveList


def filterWins(moveList, aiWins, opponentWins):
    for Board in moveList:
        wonBy = gameWonBy(Board)
        if wonBy == AI_SIGN:
            aiWins.append(Board)
            moveList.remove(Board)
        elif wonBy == OPPONENT_SIGN:
            opponentWins.append(Board)
            moveList.remove(Board)


def countPossibilities():
    Board = EMPTY_SIGN * 9
    moveList = [Board]
    aiWins = []
    opponentWins = []
    for i in range(9):
        print('step ' + str(i) + '. Moves: ' + str(len(moveList)))
        sign = AI_SIGN if i % 2 == 0 else OPPONENT_SIGN
        moveList = allMovesFromBoardList(moveList, sign)
        filterWins(moveList, aiWins, opponentWins)
    print('First player wins: ' + str(len(aiWins)))
    print('Second player wins: ' + str(len(opponentWins)))
    print('Draw', str(len(moveList)))
    print('Total', str(len(aiWins) + len(opponentWins) + len(moveList)))


def initUtilityMatrix(Board):
    return [0 if cell == EMPTY_SIGN else -1 for cell in Board]


def generateAddScore(Utilities, i, j, k):
    def addScore(points):
        if Utilities[i] >= 0:
            Utilities[i] += points
        if Utilities[j] >= 0:
            Utilities[j] += points
        if Utilities[k] >= 0:
            Utilities[k] += points
    return addScore


def utilityMatrix(Board):
    Utilities = initUtilityMatrix(Board)
    for [i, j, k] in ComboIndices:
        addScore = generateAddScore(Utilities, i, j, k)
        Triple = [Board[i], Board[j], Board[k]]
        if Triple.count(EMPTY_SIGN) == 1:
            if Triple.count(AI_SIGN) == 2:
                addScore(1000)
            elif Triple.count(OPPONENT_SIGN) == 2:
                addScore(100)
        elif Triple.count(EMPTY_SIGN) == 2 and Triple.count(AI_SIGN) == 1:
            addScore(10)
        elif Triple.count(EMPTY_SIGN) == 3:
            addScore(1)
    return Utilities


def bestMovesFromBoard(Board, sign):
    moveList = []
    utilities = utilityMatrix(Board)
    maxUtility = max(utilities)
    for i, v in enumerate(Board):
        if utilities[i] == maxUtility:
            moveList.append(Board[:i] + sign + Board[i+1:])
    return moveList


def allMovesFromBoardList(BoardList, sign):
    moveList = []
    getMoves = bestMovesFromBoard if sign == AI_SIGN else allMovesFromBoard
    for Board in BoardList:
        moveList.extend(getMoves(Board, sign))
    return moveList
