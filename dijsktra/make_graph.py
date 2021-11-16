from collections import defaultdict

import networkx as nx
from matplotlib import pyplot as plt


class Make_graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def add_node(self, vertex, neighbours):
        for i in neighbours:
            self.graph[vertex].append(i)


    def return_graph(self):
        return self.graph

    def draw_graph(self):
        G = nx.DiGraph()
        temp_dict = defaultdict()
        for i in self.return_graph():
            for j in self.return_graph()[i]:
                G.add_edge(i, j[0], label=j[1])
                temp_dict[(i, j[0])] = j[1]

        pos = nx.shell_layout(G)
        nx.draw_networkx(G, pos)
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=nx.get_edge_attributes(G, 'label'),
            font_color='red'
        )

        plt.show()