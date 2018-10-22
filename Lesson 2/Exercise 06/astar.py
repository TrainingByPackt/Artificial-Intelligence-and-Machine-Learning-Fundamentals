import math
from simpleai.search import SearchProblem, astar


class ShortestPath(SearchProblem):
    def __init__(self, Size, Start, End, Obstacles):
        self.Size = Size
        self.Start = Start
        self.End = End
        self.Obstacles = Obstacles
        super(ShortestPath, self).__init__(initial_state=self.Start)

    def actions(self, state):
        (row, col) = state
        (maxRow, maxCol) = self.Size
        succStates = []
        if row > 1:
            succStates += [(row-1, col)]
        if col > 1:
            succStates += [(row, col-1)]
        if row < maxRow:
            succStates += [(row+1, col)]
        if col < maxCol:
            succStates += [(row, col+1)]
        return [s for s in succStates if s not in self.Obstacles]

    def result(self, state, action):
        return action

    def is_goal(self, state):
        return state == End

    def cost(self, state, action, newState):
        return 1

    def heuristic(self, state):
        (x, y) = state
        (u, v) = self.End
        return math.sqrt(abs(x-u) ** 2 + abs(y-v) ** 2)


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
