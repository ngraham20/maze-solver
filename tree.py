
class Tree:

    def __init__(self, x: int, y: int):
        self.root = None
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.visited = False
        self.location = (x, y)

    def update(self):  # recursive root update
        if self.north is not None and self.north.root != self.root:
            self.north.root = self.root
            self.north.update()
        if self.south is not None and self.south.root != self.root:
            self.south.root = self.root
            self.south.update()
        if self.east is not None and self.east.root != self.root:
            self.east.root = self.root
            self.east.update()
        if self.west is not None and self.west.root != self.root:
            self.west.root = self.root
            self.west.update()
