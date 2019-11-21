from PIL import Image
from typing import Tuple


class PngHandler:

    def __init__(self, png):
        self.pixel_matrix = self.import_png(png)
    
    @staticmethod
    def import_png(png: str) -> Image.Image:
        return Image.open(png).convert('RGB')

    @staticmethod
    def get_rgb(x: int, y: int, image: Image.Image) -> Tuple:
        return tuple(image.getpixel((x, y)))

