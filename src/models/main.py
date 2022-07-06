#%%

import networkx as nx
from plots import plot_graph

"""
Graph Creation file
    The Simulation class is used for the graph composition, along 
    with the active users creation.
"""

class Simulation: 
    def __init__(self, nr_users, nr_edges, nr_nodes, cpu_range, mem_range, disk_range, mobility_probability, network_type) -> None:
        self.number_of_users = nr_users
        self.number_of_edges = nr_edges
        self.number_of_nodes = nr_nodes
        self.cpu_range = cpu_range
        self.memory_range = mem_range
        self.disk_range = disk_range
        self.mobility_probability = mobility_probability
        self.network_type = network_type
        # ...

    def create_network():
        pass

    def place_users():
        pass

    def start_simulation():
        """
            options: 
                - place data
                - retrieve data 
                - move user 
        """
        pass
# Add getters and setters