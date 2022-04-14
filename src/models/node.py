import networkx as nx 

"""
Node specification
    The Node class specifies a set of attributes that a node has.
"""
class Node:
    def __init__(self, lat:float, lon:float, response_time:int = 5, max_users:int = 10000) -> None:
        self.lat = lat
        self.long = lon
        self.response_time = response_time
        self.max_users = max_users

    def set_lan(self, lan:int) -> None:
        self.lan = lan

    def get_lan(self) -> int:
        return self.lan

    def set_lon(self, lon:int) -> None:
        self.lon = lon

    def get_lon(self) -> int:
        return self.lon

    def set_response_time(self, response_time:int) -> None:
        self.response_time = response_time

    def get_response_time(self) -> int:
        return self.response_time

    def set_max_users(self, max_users:int) -> None:
        self.max_users = max_users

    def get_max_users(self) -> None:
        return self.max_users