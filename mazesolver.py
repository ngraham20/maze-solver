from maze import Maze
from typing import List, Tuple
import pngfunctions


class MazeSolver:

    def __init__(self):
        self.maze = Maze()
        self.matrix = None

        self.duration = 0

        self.solution = None

        self.name = "DEFAULT"

    def import_png(self, png: str):
        """
        Import a png to solve
        @param png: the PNG file string to import
        @return:
        """
        self.maze.import_png(png)
        self.matrix = self.maze.matrix

    def solve(self, beginning, end, history_log: List = None):
        """
        Solve the imported Maze PNG
        @param beginning: the start location
        @param end: the target location
        @param history_log: an array of command tuples in the form (<command_string>, <param1>, <param2>, ...)
        @return:
        """
        pass

    def generate_png(self, image):
        """
        Generate and save the PNG solution
        @param image: the image object containing the PNG data
        @return:
        """
        dir_name = "./solutions/" + self.name + "-" + str(self.maze.size) + "x" + str(self.maze.size) + "-" + \
                   str(float("%.5f" % self.duration)) + "s.png"
        image.save(dir_name, "PNG")

        print("Solution saved to", dir_name)

    def save_solution(self, solution, history_log=None):
        """
        Helper function to generate a solution, displayed as a gradient from blue (start) to red (finish)
        @param solution: the list containing the solution (x, y) coordinates
        @param history_log: an array of command tuples in the form (<command_string>, <param1>, <param2>, ...)
        @return:
        """
        dir_name = "solutions/" + self.name + "-" + str(self.maze.size) + "x" + str(self.maze.size) + "-" \
                   + str(float("%.5f" % self.duration)) + "s"

        history_frames = 0
        if history_log:
            history_frames = self.save_history(history_log)

        size = len(solution)
        section = size // 2
        increment = 255 / section
        for index in range(section):  # from red to purple
            self.maze.draw.point(solution[index], (255, 0, int(0 + increment * index)))
            pngfunctions.save_frame(self.maze.image, dir_name, index + history_frames)

        for index in range(section + 1):  # from purple to blue
            self.maze.draw.point(solution[section + index], (int(255 - increment * index), 0, 255))

            pngfunctions.save_frame(self.maze.image, dir_name, section + index + history_frames)

    def save_history(self, history_log):
        """
        Save the algorithmic process as well as the solution
        @param history_log: an array of command tuples in the form (<command_string>, <param1>, <param2>, ...)
        @return:
        """
        dir_name = "solutions/" + self.name + "-" + str(self.maze.size) + "x" + str(self.maze.size) + "-" \
                   + str(float("%.5f" % self.duration)) + "s"
        index = 0
        for action in history_log:
            action: Tuple
            if action[0] == "closed":
                self.maze.draw.point(action[1], (0, 255, 0))
            elif action[0] == "open":
                self.maze.draw.point(action[1], (0, 0, 255))
            elif action[0] == "push":
                self.maze.draw.point(action[1], (0, 255, 0))
            elif action[0] == "pop":
                self.maze.draw.point(action[1], (35, 192, 209))
            pngfunctions.save_frame(self.maze.image, dir_name, index)
            index += 1
        return index
