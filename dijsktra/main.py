import make_graph
from collections import defaultdict
my_graph = make_graph.Make_graph()
my_graph.add_node('A', [('B',3)])
my_graph.add_node('A', [('G',1)])
my_graph.add_node('B', [('C',1)])
my_graph.add_node('C', [('E',2)])
my_graph.add_node('D', [('B',4)])
my_graph.add_node('E', [('F',10),('D',3)])
my_graph.add_node('G', [('I', 1)])
my_graph.add_node('F', [])
graph = my_graph.return_graph()
print(graph)
def main_loop(node):
    if str(node)[0] == target:
        return node
    for i in graph[str(node)[0]]:
        dij[i[0]+ node].append(dij[node][0] + i[1])
    del dij[node]
    return main_loop(min(dij, key=dij.get))


starting_node,target = 'A', 'F'
dij = defaultdict(list)
dij[starting_node].append(0)
print(main_loop('A')[::-1])
my_graph.draw_graph()









# dij[i[0]].append(dij[node][0] + i[1])
# paths[i[0]]= [node , paths[node]]
# paths[str(i[0]+ node)].append(paths[node][0] + i[1])