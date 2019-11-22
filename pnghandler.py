from PIL import Image, ImageDraw
from tree import Tree
from typing import Optional, List, Any, Union
from typing import List


class PngHandler(object):

    matrix: List[List[Tree]]

    def __init__(self, size):
        self.size = size
        self.image = Image.new('RGB', (size, size))
        self.draw = ImageDraw.Draw(self.image, "RGB")

        self.matrix = [[None] * size for _ in range(size)]

    @staticmethod
    def import_png(png: str) -> Image.Image:
        return Image.open(png).convert('RGB')

    def setup_grid(self):
        for y in range(self.size):  # loop row
            if y % 2 == 1:  # every other row
                for x in range(self.size):  # every other pixel
                    if x % 2 == 1:
                        self.draw.point((x, y), (255, 255, 255))  # make it white
                        self.matrix[x][y] = Tree(x, y)  # add the node

    def show(self):
        self.image.show()
