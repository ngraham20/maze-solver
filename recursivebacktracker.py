from mazegenerator import MazeGenerator
import time
import random


class RecursiveBacktracker(MazeGenerator):

    def generate(self):
        start_time = time.time()

        the_stack = [(1, 1)]
        self.matrix[1][1].visited = True

        while the_stack:
            x, y = the_stack.pop()
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
                next_node = random.choice(pool)
                self.maze.connect(self.matrix[x][y], self.matrix[next_node[0]][next_node[1]])
                self.matrix[next_node[0]][next_node[1]].visited = True
                the_stack.append(next_node)

        self.duration = time.time() - start_time

    def save_png(self):
        self.maze.image.save("pngs/" + str(self.maze.size) + "x" + str(self.maze.size) + "-RB-" +
                             str(float("%.5f" % self.duration)) + "s.png", "PNG")

    def print_duration(self):
        print("RECURSIVE BACKTRACKER: %s x %s" % (self.maze.size, self.maze.size))
        print("--- %s seconds ---" % self.duration)
