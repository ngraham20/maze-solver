from mazesolver import MazeSolver
import time
import random


class SolveRB(MazeSolver):

    def __init__(self):
        super().__init__()
        self.name = "solutionRB"

    def solve(self, beginning, end, history_log=None):
        start_time = time.time()
        the_visited = set()
        the_visited.add(beginning)

        the_stack = [beginning]
        if history_log is not None:
            history_log.append(("push", beginning))

        while end not in the_stack:  # while the stack is not empty
            x, y = the_stack.pop()
            if history_log is not None:
                history_log.append(("pop", (x, y)))

            # check all of this nodes neighbors and add them to a pool
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

            if len(pool) > 0:  # pick a random neighbor and travel to that one next
                the_stack.append((x, y))
                if history_log is not None:
                    history_log.append(("push", (x, y)))
                next_node = random.choice(pool)
                the_visited.add(next_node)
                the_stack.append(next_node)
                if history_log is not None:
                    history_log.append(("push", next_node))

        self.duration = time.time() - start_time

        return the_stack


