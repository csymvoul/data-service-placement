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
            Options / Actions in the system: 
                - place data
                - retrieve data 
                - move user 
            
            Scenarios: 
                - start with the creation of an edge network constituting of 50 edge servers with the following characteristics:
                    - cpu cores range: [2, 16]
                    - memory range: [4, 64]
                    - storage (capacity) range: [500, 3000]
                    - connection type: *TBD*
                - create clusters of edge nodes, based on adjacency, that are comprised of maximum 10 nodes (at least 5 regions will be created)
                - insert XXX users with a variating number of data 
                    - each data will have a data size: [1, 500]
                - mobility: 
                    - 
        """
        pass

    def set_number_of_users(self, number_of_users) -> None:
        self.number_of_users = number_of_users

    def get_number_of_users(self) -> int:
        return self.number_of_users

    def set_number_of_nodes(self, number_of_nodes) -> None:
        self.number_of_nodes = number_of_nodes

    def get_number_of_nodes(self) -> int:
        return self.number_of_nodes

    def set_number_of_edges(self, number_of_edges) -> None:
        self.number_of_edges = number_of_edges

    def get_number_of_edges(self) -> int:
        return self.number_of_edges

    def set_cpu_range(self, cpu_range) -> None:
        self.cpu_range = cpu_range

    def get_cpu_range(self) -> int:
        return self.cpu_range

    def set_memory_range(self, memory_range) -> None:
        self.memory_range = memory_range

    def get_memory_range(self) -> int:
        return self.memory_range    

    def set_disk_range(self, disk_range) -> None:
        self.disk_range = disk_range

    def get_disk_range(self) -> int:
        return self.disk_range   

    def set_mobility_probability(self, mobility_probability) -> None:
        self.disk_range = disk_range

    def get_mobility_probability(self) -> float:
        return self.mobility_probability
    
    def set_network_type(self, network_type) -> None:
        self.network_type = network_type

    def get_network_type(self) -> str:
        return self.network_type