"""
User specification
    The User class specifies a set of attributes that a user has.
"""
class User:
    def __init__(self, id) -> None:
        self.id = id
        self.visited_nodes = []
        self.is_static = False
    
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
