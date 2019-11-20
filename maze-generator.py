from PIL import Image
from typing import Tuple


def get_rgb(x: int, y: int, image: Image.Image) -> Tuple:
    """
    Returns the rgb value of an image at a specified location
    :param x: the x position
    :type x: int
    :param y: the y position
    :type y: int
    :param image: the Image object
    :type image: Image.Image
    :return: tuple containing the r, g, b values
    """
    return tuple(image.getpixel((x, y)))

