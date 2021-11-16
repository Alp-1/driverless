from collections import defaultdict

temp_graph = {'A': [('B', 3), ('G', 1)], 'B': [('C', 1)], 'C': [('E', 2)], 'D': [('B', 4)], 'E': [('F', 10), ('D', 3)],
              'G': [('I', 1)]}

graph = defaultdict(list)  # used to avoid using try, except or if clauses later
for i in temp_graph:  # converts normal dictionary to defaultdict.
    graph[i] = temp_graph[i]


def main_loop(target):
    # node = path of chars from start to a certain node. node[0] will be the current node.
    node = min(dij, key=dij.get)  # get the path to node with the lowest value, ie.shortest path

    if node[0] == target:  # if current node is target just return the target.
        return node

    for i in graph[node[0]]:  # go through the neighbours of the current node.
        dij[i[0] + node].append(dij[node][0] + i[1])
        # create new key(path from start to current node) with the value as the distance to that node.

    del dij[node]  # delete path to current node, as all future nodes are added to dij
    return main_loop(target)  # recurse until node[0] == target.


dij = defaultdict(list)  # defaultdict avoids using try, except or if conditions later on.
# dij stores the paths to nodes.

def init(starting_node, target):
    dij[starting_node].append(0)
    print(main_loop(target))


init('A', 'F')
