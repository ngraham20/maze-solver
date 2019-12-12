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

    def analyze(self, count):
        """
        run and print multiple iterations of the maze generation, without saving the PNG
        @param count: the number of iterations to execute
        """
        durations = []
        for _ in range(count):
            self.__init__(self.size)
            self.generate(save_png=False)
            durations.append(self.duration)
        print(self.name + ":", str(durations))

    def generate(self, history_log=None, save_png=True):
        """
        Generate the maze based off the parameters specified in the object parameters
        @param history_log: an array of command tuples in the form (<command_string>, <param1>, <param2>, ...)
        @param save_png: boolean value indicating if the PNG result should be saved
        """
        pass

    def save_png(self):
        """
        Helper function to save the maze as a PNG
        """
        self.maze.image.save("mazes/" + self.name + "-" + str(self.maze.size) + "x" + str(self.maze.size) + "-" +
                             str(float("%.5f" % self.duration)) + "s.png", "PNG")

    def print_results(self):
        """
        Prints the results of the maze generation to the console
        """
        print("%s: %s x %s" % (self.name, self.maze.size, self.maze.size))
        print("--- %s seconds ---" % self.duration)
        print("History saved to", self.directory)

    def save_history(self, history_log):
        """
        Processes the history_log array to generate a folder of PNGs in order to animate the algorithm
        @param history_log: an array of command tuples in the form (<command_string>, <param1>, <param2>, ...)
        """
        pass

    @abstractmethod
    def maze_generator_factory(self, size: int):
        pass
