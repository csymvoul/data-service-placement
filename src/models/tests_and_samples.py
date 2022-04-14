#%%

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

G.add_edges_from([("A","C"), ("B","D"), ("B","E"), ("C", "E")])
print("Nodes and Edges: ",G.nodes(), ", ", G.edges())

# Print vertex (i.e., node) degrees
print("Degrees: ", G.degree())

# Print degree of a specific vertex
print("Degree of A: ", G.degree("A"))

# Print adjacency view
print("Adjacency view: ", G.adj)

#%%
# Plot graph
# print_me()
Plots.plot_graph(G)

#%%
from user import User

user = User("15234")
user.get_id()
user.set_visited_node("A")
user.set_visited_node("B")
user.get_visited_nodes()
# %%