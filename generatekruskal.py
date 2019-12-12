from mazegenerator import MazeGenerator
import time
import random


class GenerateKruskal(MazeGenerator):

    def __init__(self, size):
        super().__init__(size)
        self.name = "Kruskal"
        self.directory = self.directory = "mazes/" + self.name + "-" + str(self.size) + "x" + str(self.size) + "-" + hex(random.randint(0, 500))

    def generate(self):
        start_time = time.time()
        set_index = 0
        sets = {}
        edges = set()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node is not None:
                    node.root = node.location
                    sets[set_index] = [(i, j)]
                    node.set_index = set_index
                    set_index += 1

                    if i + 2 < self.size:
                        edges.add(((i, j), (i + 2, j)))
                    if j + 2 < self.size:
                        edges.add(((i, j), (i, j + 2)))

        while edges:
            edge = random.sample(edges, 1)[0]  # returns a set of
            edges.remove(edge)
            ax, ay = edge[0]
            a = self.matrix[ax][ay]
            bx, by = edge[1]
            b = self.matrix[bx][by]
            if a.root != b.root:  # if they're not part of the same tree
                self.maze.draw.point((ax, ay), (255, 255, 255))
                self.maze.draw.point((bx, by), (255, 255, 255))
                self.maze.connect(a, b, update_root=True)

        self.duration = time.time() - start_time

    def save_png(self):
        super().save_png()

    def print_results(self):
        super().print_results()

    def maze_generator_factory(self, size: int):
        return GenerateKruskal(size)


generator = GenerateKruskal(200)
generator.generate()
generator.save_png()

