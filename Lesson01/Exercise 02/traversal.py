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
    nodes_to_visit = [node]
    visited_nodes = []
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop(0)
        visited_nodes.append(current_node)
        nodes_to_visit.extend(successors(current_node))
    return visited_nodes


def dfs_tree(node):
    nodes_to_visit = [node]
    visited_nodes = []
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop()
        visited_nodes.append(current_node)
        nodes_to_visit.extend(successors(current_node))
    return visited_nodes
