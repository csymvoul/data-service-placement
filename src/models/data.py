"""
Data specification
    The Data class specifies a set of attributes that a data has.
"""
class Data:
    def __init__(self, id) -> None:
        self.id = id
        self.size = -1
    
    def set_size(self, size) -> None:
        self.size = size

    def get_size(self) -> int:
        return self.size