from maze import Maze
from typing import List, Tuple
import os

class MazeSolver:

    def __init__(self):
        self.maze = Maze()
        self.matrix = None

        self.duration = 0

        self.solution = None

        self.name = "DEFAULT"

    def import_png(self, png: str):
        self.maze.import_png(png)
        self.matrix = self.maze.matrix

    def solve(self, beginning, end, history_log: List = None):
        pass

    def generate_png(self, image):
        image.save("./solutions/" + self.name + "-" + str(self.maze.size) + "x" + str(self.maze.size) + "-" +
                   str(float("%.5f" % self.duration)) + "s.png", "PNG")

    def save_gif(self, image, frame_number):
        dir_name = "solutions/" + self.name + "-" + str(self.maze.size) + "x" + str(self.maze.size) + "-" + \
                   str(float("%.5f" % self.duration)) + "s"

        try:
            # Create target Directory
            os.mkdir(dir_name)
            print("Directory ", dir_name,  " Created ")
        except FileExistsError:
            print("Directory ", dir_name,  " already exists")

        image.save(dir_name + "/" + str(frame_number) + ".png", "PNG")

    def save_solution(self, solution, history_log=None):
        history_frames = 0
        if history_log:
            history_frames = self.save_history(history_log)

        solution.reverse()
        size = len(solution)
        section = size // 2
        increment = 255 / section
        for index in range(section):  # from red to purple
            self.maze.draw.point(solution[index], (255, 0, int(0 + increment * index)))
            self.save_gif(self.maze.image, index + history_frames)

        for index in range(section + 1):  # from purple to blue
            self.maze.draw.point(solution[section + index], (int(255 - increment * index), 0, 255))
            self.save_gif(self.maze.image, section + index + history_frames)

        self.generate_png(self.maze.image)

    def save_history(self, history_log):
        index = 0
        for action in history_log:
            action: Tuple
            if action[0] == "closed":
                self.maze.draw.point(action[1], (0, 255, 0))
            elif action[0] == "open":
                self.maze.draw.point(action[1], (0, 0, 255))
            self.save_gif(self.maze.image, index)
            index += 1
        return index

