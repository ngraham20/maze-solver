# functions to handle png manipulation
import os


def save_frame(image, directory, frame_number):
    """
    Helper function to specify a file name for individual frames of an animation
    @param image: the image object containing the PNG data
    @param directory: a string describing where to save the PNG
    @param frame_number: the frame to save
    @return:
    """

    if not os.path.exists(directory):
        os.makedirs(directory)

    image.save(directory + "/" + str(frame_number) + ".png", "PNG")
