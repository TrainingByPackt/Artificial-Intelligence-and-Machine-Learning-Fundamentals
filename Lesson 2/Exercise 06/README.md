# Exercise 06: A* Search in Practice using the simpleai library

Implement the A* algorithm using the SimpleAI library.

Installation:

```
pip install simpleai
```

Game field:

```
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
```

## Execution

Create a search problem, then use the `astar` algorithm to find the result:

```
searchProblem = ShortestPath(Size, Start, End, Obstacles)
result = astar( searchProblem, graph_search=True )
```

To extract the path, call

```
result.path()
```