from mazegenerator import MazeGenerator
from disjoint_set import DisjointSet
import time
import random


class GenerateKruskal(MazeGenerator):

    def __init__(self, size):
        super().__init__(size)
        self.name = "Kruskal"
        self.directory = self.directory = "mazes/" + self.name + "-" + str(self.size) + "x" + str(self.size) + "-" + hex(random.randint(0, 500))

    def generate(self):
        start_time = time.time()
        ds = DisjointSet()
        edges = set()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node is not None:
                    node.root = node.location
                    ds.find((i, j))
                    if i + 2 < self.size:
                        edges.add(((i, j), (i + 2, j)))
                    if j + 2 < self.size:
                        edges.add(((i, j), (i, j + 2)))

        while edges:
            edge = random.sample(edges, 1)[0]
            edges.remove(edge)
            ax, ay = edge[0]
            bx, by = edge[1]
            if not ds.connected((ax, ay), (bx, by)):
                ds.union((ax, ay), (bx, by))
                self.maze.connect(self.matrix[ax][ay], self.matrix[bx][by])

        self.duration = time.time() - start_time

    def maze_generator_factory(self, size: int):
        return GenerateKruskal(size)

