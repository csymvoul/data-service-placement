import networkx as nx 

"""
Node specification
    The Node class specifies a set of attributes that a node has.
"""
class Node:
    def __init__(self, 
                id:int,
                lat:float, 
                lon:float, 
                response_time:int = 5, 
                max_users:int = 10000, 
                cpu_cores:int = 2, 
                memory:int = 8, 
                capacity:int = 500) -> None:
        self.id = id
        self.lat = lat
        self.long = lon
        self.response_time = response_time
        self.max_users = max_users
        self.number_of_cpu_cores = cpu_cores
        self.memory = memory
        self.capacity = capacity

    def get_id(self) -> int: 
        return self.id
    
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

    def set_number_of_cpu_cores(self, cpu_cores) -> None:
        self.number_of_cpu_cores = cpu_cores
    
    def get_number_of_cpu_cores(self) -> int:
        self.number_of_cpu_cores
    
    def set_memory(self, memory) -> None:
        self.memory = memory

    def get_memory(self) -> int:
        return self.memory 
    
    def set_capacity(self, capacity) -> None:
        self.capacity = capacity

    def get_capacity(self) -> int:
        return self.capacity 