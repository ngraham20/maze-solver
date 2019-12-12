from mazegenerator import MazeGenerator
import time
import random
import pngfunctions
from typing import Tuple

# questions
"""
start at 1,1 in array 
tree starts as n/2 by n/2 nodes
jumping nodes is + 2
give connect both nodes to remove wall --in maze.py
set has const time removal - use for frontier nodes if rand pick
if pick first/last one then use queue/stack
    stacks and queues are both lists 
    append treats like stack
    enqueue or dequeue add front remove back
    append/pop remove from same side
    
    no history
    access nodes by location in matrix until nodes are linked in Tree
heap for smallest/largest
"""


class GeneratePrimms(MazeGenerator):
    def __init__(self, size):
        super().__init__(size)
        self.name = "Primms"
        self.directory = "mazes/" + self.name + "-" + str(self.size) + "x" + str(self.size) + "-" \
                         + hex(random.randint(0, 500))

    def save_history(self, history_log):
        frame = 0
        for action in history_log:
            action: Tuple
            if action[0] == "bridge":
                self.maze.draw.point(action[1], (255, 255, 255))
            if action[0] == "frontier":
                self.maze.draw.point(action[1], (252, 3, 157))
            if action[0] == "visit":
                self.maze.draw.point(action[1], (255, 255, 255))
            pngfunctions.save_frame(self.maze.image, self.directory, frame)
            frame += 1

    def generate(self, history_log=None):

        start_time = time.time()

        the_frontier = {(1, 1)}  # set

        while the_frontier:

            x, y = random.sample(the_frontier, 1)[0]  # pick random frontier node
            the_frontier.remove((x, y))
            self.matrix[x][y].visited = True
            if history_log is not None:
                history_log.append(("visit", (x, y)))

            pool = []

            # check all directions for new frontiers, add to frontier
            if y - 2 > 0:
                if not self.matrix[x][y - 2].visited:  # check north
                    the_frontier.add((x, y - 2))
                    if history_log is not None:
                        history_log.append(("frontier", (x, y - 2)))
                else:
                    pool.append((x, y - 2))
            if y + 2 < len(self.matrix):
                if not self.matrix[x][y + 2].visited:  # check south
                    the_frontier.add((x, y + 2))
                    if history_log is not None:
                        history_log.append(("frontier", (x, y + 2)))
                else:
                    pool.append((x, y + 2))

            if x - 2 > 0:
                if not self.matrix[x - 2][y].visited:  # check east
                    the_frontier.add((x - 2, y))
                    if history_log is not None:
                        history_log.append(("frontier", (x - 2, y)))
                else:
                    pool.append((x - 2, y))

            if x + 2 < len(self.matrix):
                if not self.matrix[x + 2][y].visited:  # check west
                    the_frontier.add((x + 2, y))
                    if history_log is not None:
                        history_log.append(("frontier", (x + 2, y)))
                else:
                    pool.append((x + 2, y))
            
            if len(pool) > 0:
                next_node = random.choice(pool)
                self.maze.connect(self.matrix[x][y], self.matrix[next_node[0]][next_node[1]], history_log)

        self.duration = time.time() - start_time
        if history_log is not None:
            self.save_history(history_log)
        self.save_png()

    def save_png(self):
        self.maze.image.save("mazes/" + self.name + "-" + str(self.size) + "x" + str(self.size) + "-" +
                             str(float("%.5f" % self.duration)) + "s.png", "PNG")

    def print_results(self):
        super().print_results()

    def maze_generator_factory(self, size: int):
        pass
