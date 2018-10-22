# 0. Paste the code in the Jupyter QtConsole
# 1. Execute:  bfs_tree( root )
# 2. Execute:  dfs_tree( root )

root = {'value': 1, 'depth': 1}


def successors(node):
    if node['value'] == 5:
        return []
    elif node['value'] == 4:
        return [{'value': 5, 'depth': node['depth']+1}]
    else:
        return [
            {'value': node['value']+1, 'depth':node['depth']+1},
            {'value': node['value']+2, 'depth':node['depth']+1}
        ]


def bfs_tree(node):
    nodesToVisit = [node]
    visitedNodes = []
    while len(nodesToVisit) > 0:
        currentNode = nodesToVisit.pop(0)
        visitedNodes.append(currentNode)
        nodesToVisit.extend(successors(currentNode))
    return visitedNodes


def dfs_tree(node):
    nodesToVisit = [node]
    visitedNodes = []
    while len(nodesToVisit) > 0:
        currentNode = nodesToVisit.pop()
        visitedNodes.append(currentNode)
        nodesToVisit.extend(successors(currentNode))
    return visitedNodes
