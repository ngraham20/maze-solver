# functions to handle png manipulation
import os


def save_frame(image, directory, frame_number):

    if not os.path.exists(directory):
        os.makedirs(directory)

    image.save(directory + "/" + str(frame_number) + ".png", "PNG")
