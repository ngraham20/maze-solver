from mazegenerator import MazeGenerator
import time
import random
import pngfunctions
from typing import Tuple


#questions
"""
why tree? what do? Do need for primms


"""


class GenerateRB(MazeGenerator):

    def __init__(self, size):
        super().__init__(size)
        self.name = "RB"
        self.directory = "mazes/" + self.name + "-" + str(self.size) + "x" + str(self.size) + "-" + hex(random.randint(0, 500))

    def maze_generator_factory(self, size: int):
        return GenerateRB(size)

    def save_history(self, history_log):
        frame = 0
        for action in history_log:
            action: Tuple
            if action[0] == "bridge":
                self.maze.draw.point(action[1], (255, 255, 255))
                if frame + 1 < len(history_log):
                    self.maze.draw.point(history_log[frame + 1][1], (0, 0, 255))
            if action[0] == "pop":
                self.maze.draw.point(action[1], (0, 0, 255))
                if frame - 1 > 0:
                    self.maze.draw.point(history_log[frame - 1][1], (255, 255, 255))
                if frame - 2 >= 0 and history_log[frame - 1][0] == "bridge":
                    self.maze.draw.point(history_log[frame - 2][1], (255, 255, 255))
            pngfunctions.save_frame(self.maze.image, self.directory, frame)
            frame += 1

    def generate(self, history_log=None):
        start_time = time.time()

        the_stack = [(1, 1)]
        self.matrix[1][1].visited = True

        while the_stack:
            x, y = the_stack.pop()
            if history_log is not None:
                history_log.append(("pop", (x, y)))
            pool = []
            if y - 2 > 0 and not self.matrix[x][y - 2].visited:  # check north
                pool.append((x, y - 2))

            if y + 2 < len(self.matrix) and not self.matrix[x][y + 2].visited:  # check south
                pool.append((x, y + 2))

            if x - 2 > 0 and not self.matrix[x - 2][y].visited:  # check east
                pool.append((x - 2, y))

            if x + 2 < len(self.matrix) and not self.matrix[x + 2][y].visited:  # check west
                pool.append((x + 2, y))

            if len(pool) > 0:
                the_stack.append((x, y))
                # if history_log is not None:
                #     history_log.append(("push", (x, y)))
                next_node = random.choice(pool)
                self.maze.connect(self.matrix[x][y], self.matrix[next_node[0]][next_node[1]], history_log)
                self.matrix[next_node[0]][next_node[1]].visited = True
                the_stack.append(next_node)
                # if history_log is not None:
                #     history_log.append(("push", (x, y)))

        self.duration = time.time() - start_time
        if history_log is not None:
            history_log.append(("pop", (1, 1)))
            self.save_history(history_log)

    def save_png(self):
        self.maze.image.save("mazes/RB-" + str(self.maze.size) + "x" + str(self.maze.size) + "-" +
                             str(float("%.5f" % self.duration)) + "s.png", "PNG")

    def print_results(self):
        print("RECURSIVE BACKTRACKER: %s x %s" % (self.maze.size, self.maze.size))
        print("--- %s seconds ---" % self.duration)
        print("History saved to", self.directory)
