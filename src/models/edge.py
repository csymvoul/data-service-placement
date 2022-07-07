import networkx as nx 
from node import Node
from math import sqrt, pow

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
    
    def calculate_distance(self, node1:Node, node2:Node) -> None:
        self.distance = sqrt( pow(node2.get_lan()-node1.get_lan(), 2) + pow(node2.get_lon() - node1.get_lon(), 2) )

    def get_distance(self) -> float:
        return self.distance