#%%
import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(G):
    nx.draw(G, with_labels=True, font_weight='bold', node_color='red')
    plt.show()
    plt.savefig("../figures/graph.png")