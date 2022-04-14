import matplotlib.pyplot as plt
import networkx as nx
import os


class Plots:
    @staticmethod
    def plot_graph(G: nx.Graph()) -> None:
        nx.draw(G, with_labels=True, font_weight='bold', node_color='red')
        plt.savefig("../figures/graph.png")
        plt.show()
        plt.close()