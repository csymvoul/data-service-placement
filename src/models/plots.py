import matplotlib.pyplot as plt
import networkx as nx
import os

FIGURES_PATH = str(os.getcwd())+"/src/figures/"

def plot_graph(G):
    nx.draw(G, with_labels=True, font_weight='bold', node_color='red')
    print("Saving figure at: "+FIGURES_PATH+"graph.png")
    # print(os.getcwd())
    plt.savefig(FIGURES_PATH+"graph.png")
    plt.show()
    
def print_me():
    print("This is me")