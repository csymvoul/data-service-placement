import networkx as nx 

"""
Edges specification
    The Edge class specifies a set of attributes that an edge has.
"""

class Edge:
    def __init__(self, latency=1, distance=1) -> None:
        self.latency = latency
        self.distance = distance

    def set_latency(self, latency) -> None:
        self.latency = latency

    def get_latency(self) -> int:
        return self.latency
    
    def set_distance(self, distance) -> None:
        self.distance = distance

    def get_distance(self) -> float:
        return self.distance