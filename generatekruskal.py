from mazegenerator import MazeGenerator


class GenerateKruskal(MazeGenerator):

    def __init__(self, size):
        self.name = "Kruskal"
        super().__init__(size)

        self.location_sets = [[set()] * self.size for _ in range(self.size)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] is not None:
                    self.location_sets[i][j].add(self.matrix[i][j].location)

    def generate(self):
        super().generate()

    def save_png(self):
        super().save_png()

    def print_results(self):
        super().print_results()

    def maze_generator_factory(self, size: int):
        return GenerateKruskal(size)


generator = GenerateKruskal(35)
generator.generate()

