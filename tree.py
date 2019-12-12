
class Tree:

    def __init__(self, x: int, y: int):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.visited = False
        self.location = (x, y)
