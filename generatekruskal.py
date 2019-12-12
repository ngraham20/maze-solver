from mazegenerator import MazeGenerator
from disjoint_set import DisjointSet
from typing import Tuple
import pngfunctions
import time
import random


class GenerateKruskal(MazeGenerator):

    def __init__(self, size):
        super().__init__(size)
        self.name = "Kruskal"
        self.directory = self.directory = "mazes/" + self.name + "-" + str(self.size) + "x" + str(self.size) + "-" + hex(random.randint(0, 500))

    def save_history(self, history_log):
        frame = 0
        for action in history_log:
            action: Tuple
            if action[0] == "set_color":  # initialize a grid of random color pixels
                self.maze.draw.point(action[1], (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
            if action[0] == "bridge":  # (ax, ay) with (bx, by)
                self.maze.draw.point(action[1], (255, 255, 255))
            if action[0] == "merge":  # merge the colored pixels into a white bar
                self.maze.draw.point(action[1], (255, 255, 255))
                self.maze.draw.point(action[2], (255, 255, 255))

            pngfunctions.save_frame(self.maze.image, self.directory, frame)
            frame += 1

    def generate(self, history_log=None, save_png=True):
        start_time = time.time()
        ds = DisjointSet()
        edges = set()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] is not None:  # apply the following to the grid nodes
                    ds.find((i, j))  # add location (i, j) to the disjoint-set
                    if history_log is not None:
                        history_log.append(("set_color", (i, j), (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))))
                    if i + 2 < self.size:
                        edges.add(((i, j), (i + 2, j)))  # create an edge between (i, j) and its East neighbor
                    if j + 2 < self.size:
                        edges.add(((i, j), (i, j + 2)))  # create an edge between (i, j) and its South neighbor

        while edges:  # while there are edges left
            edge = random.sample(edges, 1)[0]
            edges.remove(edge)
            ax, ay = edge[0]
            bx, by = edge[1]
            if not ds.connected((ax, ay), (bx, by)):  # determine if the edge connects disjoint sets
                ds.union((ax, ay), (bx, by))  # connect the sets by the selected edge
                self.maze.connect(self.matrix[ax][ay], self.matrix[bx][by], history_log)
                if history_log is not None:
                    history_log.append(("merge", (ax, ay), (bx, by)))

        self.duration = time.time() - start_time
        if history_log is not None:
            self.save_history(history_log)
        if save_png:
            self.save_png()

    def maze_generator_factory(self, size: int):
        return GenerateKruskal(size)

