

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
