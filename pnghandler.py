from PIL import Image
from typing import Tuple


class PngHandler(object):

    def __init__(self, size):
        self.size = size
        self.pixel_matrix = Image.new('RGB', size)

    @staticmethod
    def import_png(png: str) -> Image.Image:
        return Image.open(png).convert('RGB')

    @staticmethod
    def get_rgb(x: int, y: int, image: Image.Image) -> Tuple:
        return tuple(image.getpixel((x, y)))

    def setup_grid(self):
        for x in range(self.size[0]):  # loop through row
            for y in range(self.size[1]):  # loop through column
                print("x: ", x, "y: ", y, self.get_rgb(x, y, self.pixel_matrix))

    def show(self):
        self.pixel_matrix.show()
