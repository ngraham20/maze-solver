from maze import Maze
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

    def solve(self, beginning, end):
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

    def save_solution(self, solution):
        solution.reverse()
        size = len(solution)
        section = size // 2
        increment = 255 / section
        for index in range(section):  # from red to purple
            self.maze.draw.point(solution[index], (255, 0, int(0 + increment * index)))
            self.save_gif(self.maze.image, index)

        for index in range(section + 1):  # from purple to blue
            self.maze.draw.point(solution[section + index], (int(255 - increment * index), 0, 255))
            self.save_gif(self.maze.image, section + index)

        self.generate_png(self.maze.image)
