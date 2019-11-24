from mazesolver import MazeSolver
import time
import random


class SolveRB(MazeSolver):

    def solve(self, beginning, end):
        start_time = time.time()
        the_visited = set()
        the_visited.add(beginning)

        the_stack = [beginning]

        while end not in the_stack:
            x, y = the_stack.pop()
            pool = []

            # check north
            if y - 1 > 0 and self.maze.image.getpixel((x, y - 1)) == (255, 255, 255) and not (x, y - 1) in the_visited:
                pool.append((x, y - 1))

            # check south
            if y + 1 < self.maze.size and self.maze.image.getpixel((x, y + 1)) == (255, 255, 255) and not (x, y + 1) in the_visited:
                pool.append((x, y + 1))

            # check east
            if x + 1 < self.maze.size and self.maze.image.getpixel((x + 1, y)) == (255, 255, 255) and not (x + 1, y) in the_visited:
                pool.append((x + 1, y))

            # check west
            if x - 1 > 0 and self.maze.image.getpixel((x - 1, y)) == (255, 255, 255) and not (x - 1, y) in the_visited:
                pool.append((x - 1, y))

            if len(pool) > 0:
                the_stack.append((x, y))
                next_node = random.choice(pool)
                the_visited.add(next_node)
                the_stack.append(next_node)

        self.duration = time.time() - start_time

        return the_stack

    def save_png(self, image):
        image.save("pngs/" + str(self.maze.size) + "x" + str(self.maze.size) + "-solutionRB-" +
                             str(float("%.5f" % self.duration)) + "s.png", "PNG")
