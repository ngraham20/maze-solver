from PIL import Image, ImageDraw
from typing import Tuple


class PngHandler(object):

    def __init__(self, size):
        self.size = size
        self.pixel_matrix = Image.new('RGB', (size, size))
        self.draw = ImageDraw.Draw(self.pixel_matrix, "RGB")

    @staticmethod
    def import_png(png: str) -> Image.Image:
        return Image.open(png).convert('RGB')

    def setup_grid(self):
        for y in range(self.size):  # loop through row
            if y % 2 == 1:
                for x in range(self.size):
                    if x % 2 == 1:
                        self.draw.point((x, y), (255, 255, 255))

    def show(self):
        self.pixel_matrix.show()
