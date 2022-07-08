#%%

import networkx as nx
from plots import plot_graph

"""
Graph Creation file
    The Simulation class is used for the graph composition, along 
    with the active users creation.
"""

class Simulation: 
    def __init__(self, 
                 nr_users:int, 
                 nr_edges:int, 
                 nr_nodes:int, 
                 cpu_range:int, 
                 mem_range:int, 
                 disk_range:int, 
                 mobility_probability:float, 
                 network_type:str) -> None:
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
                    - including information about the size of the data placed
                - retrieve data 
                    - including information about the size of the data retrieved
                - move user 
            
            Scenario description: 
                - start with the creation of an edge network constituting of 50 edge servers with the following characteristics:
                    - lat, lon
                    - cpu cores range: [2, 16]
                    - memory range: [4, 64]
                    - storage (capacity) range: [500, 3000]
                    - connection type: *TBD*
                    - edges with the following characteristics: 
                        - distance: calculated using the (lat,long) of the two nodes
                        - latency: would be in the this space [1, 10] - the greater the distance, the bigger the probability that latency will be higher
                            - we find the min and max distances - split distances into 5 classes, where first class is the lowest distance space and the fifth the highest
                                - if a distance belongs in the first class, it has a 80% probability the latency belong in the space [1,2], 18% belonging in [3, 8] and 2% of belonging in the [9,10]
                                - similarly for the remaining classes: 
                                    - second class: latency has 80% prob of being in the [3, 4] space, 5% of being in the [1,2] space, 10% of being in the [4,8], and 5% prob of being in the [9,10]
                                    - third class: latency has 80% prob of being in the [5, 6] space, 5% of being in the [3,4] space, 10% of being in the [7,10], and 5% prob of being in the [1,2]
                                    - fourth class: latency has 80% prob of being in the [7, 8] space, 5% of being in the [1,3] space, 10% of being in the [4,6], and 5% prob of being in the [9,10]
                                    - fifth class: latency has 80% prob of being in the [9, 10] space, 2% of being in the [1,2] space, 10% of being in the [5,8], and 8% prob of being in the [3,4]
                                    - once the probability space is selected, randomly select one of the values as latency
                - create clusters of edge nodes, based on adjacency, that are comprised of maximum 10 nodes (at least 5 regions will be created)
                - insert XXX users with the following characteristics 
                    - each data will have a data size: [1, 500]
                    - probability of movement: 
                        - cluster 1: for 70% of the total users the movement probability should be 0 (stay in the same node)
                        - for 30% of the total users the movement probability should be 1:
                            - cluster 2: out of those, 80% will have a high movement, i.e., they will travel in nodes out of their region 
                            - cluster 3: the remaining 20% will travel accross their own region
                - mobility: 
                    - cluster 1 will be static users
                    - cluster 2 will be mobile users
                    - cluster 3 will be static users
                        - for those users, the most used node will be identified as the optimal node
                - placement and retrieval actions: 
                    - 
                - data to keep for each user: 
                    - list of visited nodes including the location of the nodes
                    - edges between the nodes and their info (latency, distance, etc.)
                    - data sizes exchanged
                    - type of action (place or retrieval)               
        """
        pass

    def set_number_of_users(self, number_of_users:int) -> None:
        self.number_of_users = number_of_users

    def get_number_of_users(self) -> int:
        return self.number_of_users

    def set_number_of_nodes(self, number_of_nodes:int) -> None:
        self.number_of_nodes = number_of_nodes

    def get_number_of_nodes(self) -> int:
        return self.number_of_nodes

    def set_number_of_edges(self, number_of_edges:int) -> None:
        self.number_of_edges = number_of_edges

    def get_number_of_edges(self) -> int:
        return self.number_of_edges

    def set_cpu_range(self, cpu_range:int) -> None:
        self.cpu_range = cpu_range

    def get_cpu_range(self) -> int:
        return self.cpu_range

    def set_memory_range(self, memory_range:int) -> None:
        self.memory_range = memory_range

    def get_memory_range(self) -> int:
        return self.memory_range    

    def set_disk_range(self, disk_range:int) -> None:
        self.disk_range = disk_range

    def get_disk_range(self) -> int:
        return self.disk_range   

    def set_mobility_probability(self, mobility_probability:float) -> None:
        self.mobility_probability = mobility_probability

    def get_mobility_probability(self) -> float:
        return self.mobility_probability
    
    def set_network_type(self, network_type:str) -> None:
        self.network_type = network_type

    def get_network_type(self) -> str:
        return self.network_type
# %%
