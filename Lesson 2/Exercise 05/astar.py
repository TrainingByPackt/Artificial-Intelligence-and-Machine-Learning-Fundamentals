import math
import heapq

Size = (7,9)
Start=(5,3)
End=(6,9)
Obstacles = {
    (3,4),(3,5),(3,6),(3,7),(3,8),
    (4,5),
    (5,5),(5,7),(5,9),
    (6,2),(6,3),(6,4),(6,5),(6,7),
    (7,7)
}

# Returns the successor nodes of State, excluding nodes in VisitedNodes
def succ( State, VisitedNodes ):
    (row, col) = State
    (maxRow, maxCol) = Size
    succStates = []
    if row > 1: succStates += [(row-1,col)]
    if col > 1: succStates += [(row,col-1)]
    if row < maxRow: succStates += [(row+1,col)]
    if col < maxCol: succStates += [(row, col+1)] 
    return [s for s in succStates if s not in VisitedNodes if s not in Obstacles]

# Creates a matrix of Size, start node Start, and infinite cost
# in all nodes except Start
def initializeCosts( Size, Start ):
    costs = [ [math.inf] * 9 for i in range(7) ]
    (x,y) = Start
    costs[x-1][y-1] = 0
    return costs

Frontier = []
Internal = set()
heapq.heappush( Frontier, (0, Start) )
costs = initializeCosts( Size, Start )

def distanceHeuristic( node, goal ):
    (x,y) = node
    (u,v) = goal
    return math.sqrt( abs( x - u ) ** 2 + abs( y - v ) ** 2 )

def astar( Start, End ):
    Frontier = []
    Internal = set()
    heapq.heappush( Frontier, (0, Start ) )
    costs = initializeCosts( Size, Start )
    def getDistanceFromStart( node ):
        return costs[ node[0] - 1][ node[1]  - 1]
    def setDistanceFromStart( node, newDistance ):
        costs[ node[0] - 1][ node[1]  - 1] = newDistance
    while len( Frontier ) > 0:
        (priority, node) = heapq.heappop( Frontier )
        if node == End:
            return priority
        Internal.add( node )
        successors = succ( node, Internal )
        for s in successors:
            newDistance = getDistanceFromStart( node ) + 1
            if newDistance < getDistanceFromStart( s ):
                setDistanceFromStart( s, newDistance )
                Frontier = [ n for n in Frontier if s != n[1] ] # Filter previous entries of s
                heapq.heappush( Frontier, (
                    newDistance + distanceHeuristic(s,End), s
                    )
                )

# A* algorithm implementation logging the process
def astar_verbose( Start, End ):
    Frontier = []
    Internal = set()
    heapq.heappush( Frontier, (0, Start ) )
    costs = initializeCosts( Size, Start )
    def getDistanceFromStart( node ):
        return costs[ node[0] - 1][ node[1]  - 1]
    def setDistanceFromStart( node, newDistance ):
        costs[ node[0] - 1][ node[1]  - 1] = newDistance
    steps = 0;
    while len( Frontier ) > 0:
        steps += 1
        print( 'step ', steps, '. Frontier: ', Frontier )
        (priority, node) = heapq.heappop( Frontier )
        print( 'Node ', node, 'has been popped from Frontier with priority',  priority )
        if node == End:
            print( 'Optimal path found. Steps: ', steps )
            print( 'Costs matrix: ', costs )
            return priority
        Internal.add( node )
        successors = succ( node, Internal )
        print( 'successors', successors )
        for s in successors:
            newDistance = getDistanceFromStart( node ) + 1
            print( 's:', s, 'new distance:', newDistance, ' old distance:', getDistanceFromStart( s ) )
            if newDistance < getDistanceFromStart( s ):
                setDistanceFromStart( s, newDistance )
                Frontier = [ n for n in Frontier if s != n[1] ] # Filter previous entries of s
                newPriority = newDistance + distanceHeuristic(s,End)
                heapq.heappush( Frontier, (newPriority, s ) )
                print( 'Node', s, 'has been pushed to Frontier with priority', newPriority )
    print( 'Frontier', Frontier )
    print( 'Internal', Internal )
    print( costs )

# returns the path to endNode
def getShortestPath( endNode ):
    path = [endNode]
    distance = getDistanceFromStart( endNode )
    while distance > 0:
        for neighbor in succ( path[-1], [] ):
            newDistance = getDistanceFromStart( neighbor )
            if newDistance < distance:
                path += [neighbor]
                distance = newDistance
                break #for
    return path

# A* algorithm constructing the shortest path between Start and End
def astar_with_path( Start, End ):
    Frontier = []
    Internal = set()
    heapq.heappush( Frontier, (0, Start ) )
    costs = initializeCosts( Size, Start )
    def getDistanceFromStart( node ):
        return costs[ node[0] - 1][ node[1]  - 1]
    def setDistanceFromStart( node, newDistance ):
        costs[ node[0] - 1][ node[1]  - 1] = newDistance
    def getShortestPath( endNode ):
        path = [endNode]
        distance = getDistanceFromStart( endNode )
        while distance > 0:
            for neighbor in succ( path[-1], [] ):
                newDistance = getDistanceFromStart( neighbor )
                if newDistance < distance:
                    path += [neighbor]
                    distance = newDistance
                    break #for
        return path
    while len( Frontier ) > 0:
        (priority, node) = heapq.heappop( Frontier )
        if node == End:
            return getShortestPath( End )
        Internal.add( node )
        successors = succ( node, Internal )
        for s in successors:
            newDistance = getDistanceFromStart( node ) + 1
            if newDistance < getDistanceFromStart( s ):
                setDistanceFromStart( s, newDistance )
                Frontier = [ n for n in Frontier if s != n[1] ] # Filter previous entries of s
                heapq.heappush( Frontier, (
                    newDistance + distanceHeuristic(s,End), s
                    )
                )

