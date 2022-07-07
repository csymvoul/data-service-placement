"""
User specification
    The User class specifies a set of attributes that a user has.
"""
class User:
    def __init__(self, id) -> None:
        self.id = id
        self.visited_nodes = []
        self.is_static = False
        self.optimal_node_id = -1 # If optimal_node_id == 1, it is not yet set
    
    def set_id(self, id:str) -> None:
        self.id = id
    
    def get_id(self) -> str:
        return self.id

    def set_visited_node(self, visited_node:str) -> None:
        self.visited_nodes.append(visited_node)
    
    def get_visited_nodes(self) -> list:
        return self.visited_nodes

    def set_static(self, is_static) -> None:
        self.is_static = is_static

    def is_static(self) -> bool:
        return self.is_static
    
    def set_optimal_node_id(self, optimal_node_id) -> None:
        self.optimal_node_id = optimal_node_id
    
    def get_optimal_node_id(self) -> int: # may be a str as well
        return self.optimal_node_id
    
    # Add data to the user