#%% 
# Graph (G), edges, and nodes initialization

import networkx as nx
from plots import Plots

# Creation of an empty graph
G = nx.Graph()
print("Nodes and Edges: ",G.nodes(), ", ", G.edges())

# Add nodes
G.add_node("A")
G.add_node("B")
print("Nodes and Edges: ",G.nodes(), ", ", G.edges())

# Add multiple nodes
G.add_nodes_from(['C', 'D', 'E'])
print("Nodes and Edges: ",G.nodes(), ", ", G.edges())

# Add edges
G.add_edge(*("A", "B"))
print("Nodes and Edges: ",G.nodes(), ", ", G.edges())

# Add multiple edges
G.add_edges_from([("A","C"), ("B","D"), ("B","E"), ("C", "E")])
print("Nodes and Edges: ",G.nodes(), ", ", G.edges())

# Print vertex (i.e., node) degrees
print("Degrees: ", G.degree())

# Print degree of a specific vertex
print("Degree of A: ", G.degree("A"))

# Print adjacency view
print("Adjacency view: ", G.adj)

#%% 
# Graph plotting

Plots.plot_graph(G)

#%%
# User initialization

from user import User

user1 = User("1")
user1.get_id()
user1.set_visited_node("A")
user1.set_visited_node("B")
user1.get_visited_nodes()

user2 = User("1")
user2.get_id()
user2.set_visited_node("A")
user2.set_visited_node("C")
user2.set_visited_node("E")
user2.get_visited_nodes()

# %%