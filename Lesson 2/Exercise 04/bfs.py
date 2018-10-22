import math

Size = (7, 9)
Start = (5, 3)
End = (6, 9)
Obstacles = {
    (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
    (4, 5),
    (5, 5), (5, 7), (5, 9),
    (6, 2), (6, 3), (6, 4), (6, 5), (6, 7),
    (7, 7)
}


def successors(State, VisitedNodes):
    (row, col) = State
    (maxRow, maxCol) = Size
    succStates = []
    if row > 1:
        succStates += [(row-1, col)]
    if col > 1:
        succStates += [(row, col-1)]
    if row < maxRow:
        succStates += [(row+1, col)]
    if col < maxCol:
        succStates += [(row, col+1)]
    return [s for s in succStates if s not in VisitedNodes if s not in Obstacles]


def initializeCosts(Size, Start):
    (h, w) = Size
    costs = [[math.inf] * w for i in range(h)]
    (x, y) = Start
    costs[x-1][y-1] = 0
    return costs


def updateCosts(costs, currentNode, successorNodes):
    newCost = costs[currentNode[0]-1][currentNode[1]-1] + 1
    for (x, y) in successorNodes:
        costs[x-1][y-1] = min(costs[x-1][y-1], newCost)


def bfs_tree(node):
    nodesToVisit = [node]
    visitedNodes = []
    costs = initializeCosts(Size, Start)
    while len(nodesToVisit) > 0:
        currentNode = nodesToVisit.pop(0)
        visitedNodes.append(currentNode)
        successorNodes = successors(currentNode, visitedNodes)
        updateCosts(costs, currentNode, successorNodes)
        nodesToVisit.extend(successorNodes)
    return costs


def bfs_tree_verbose(node):
    nodesToVisit = [node]
    visitedNodes = []
    costs = initializeCosts(Size, Start)
    stepCounter = 0
    while len(nodesToVisit) > 0:
        stepCounter += 1
        currentNode = nodesToVisit.pop(0)
        visitedNodes.append(currentNode)
        successorNodes = successors(currentNode, visitedNodes)
        updateCosts(costs, currentNode, successorNodes)
        nodesToVisit.extend(successorNodes)
        if currentNode == End:
            print('End node has been reached in ', stepCounter, ' steps')
            return costs
    return costs
