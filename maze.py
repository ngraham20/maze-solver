from PIL import Image, ImageDraw
from tree import Tree
from typing import List


class Maze(object):

    matrix: List[List[Tree]]

    def __init__(self, size: int = None):
        if size:
            self.size = size
            if self.size % 2 == 0:
                self.size += 1
            self.image = Image.new('RGB', (self.size, self.size))
            self.draw = ImageDraw.Draw(self.image, "RGB")

            self.matrix = [[None] * self.size for _ in range(self.size)]

    def import_png(self, png: str):
        self.image = Image.open(png).convert('RGB')
        self.draw = ImageDraw.Draw(self.image, "RGB")
        self.size = self.image.size[0]
        self.matrix = [[None] * self.size for _ in range(self.size)]

    def setup_grid(self):
        for y in range(self.size):  # loop row
            if y % 2 == 1:  # every other row
                for x in range(self.size):  # every other pixel
                    if x % 2 == 1:
                        self.draw.point((x, y), (255, 255, 255))  # make it white
                        self.matrix[x][y] = Tree(x, y)  # add the node

    def connect(self, node_a: Tree, node_b: Tree):
        a_x = node_a.location[0]
        a_y = node_a.location[1]

        b_x = node_b.location[0]
        b_y = node_b.location[1]

        if a_x > b_x:  # if a is to the right of b
            node_a.west = node_b
            node_b.east = node_a
            self.draw.point((a_x - 1, a_y), (255, 255, 255))  # bridge
        elif b_x > a_x:  # if b is to the right of a
            node_b.west = node_a
            node_a.east = node_b
            self.draw.point((b_x - 1, b_y), (255, 255, 255))  # bridge
        elif a_y < b_y:  # if a is above b
            node_a.south = node_b
            node_b.north = node_a
            self.draw.point((a_x, a_y + 1), (255, 255, 255))  # bridge
        elif b_y < a_y:  # if b is above a
            node_b.south = node_a
            node_a.north = node_b
            self.draw.point((b_x, b_y + 1), (255, 255, 255))  # bridge

    def show(self):
        self.image.show()
