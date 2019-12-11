# default class for generating a maze
from maze import Maze
import time
import random
from abc import ABC, abstractmethod


class MazeGenerator:

    def __init__(self, size):
        self.maze = Maze(size)
        self.maze.setup_grid()
        self.name = "DEFAULT"
        self.size = size
        self.directory = self.directory = "mazes/" + self.name + "-" + str(self.size) + "x" + str(self.size) + "-" + hex(random.randint(0, 500))

        self.matrix = self.maze.matrix

        self.duration = 0

    def generate(self):
        pass

    def save_png(self):
        pass

    def print_results(self):
        pass

    @abstractmethod
    def maze_generator_factory(self, size: int):
        pass



