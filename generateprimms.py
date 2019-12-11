from mazegenerator import MazeGenerator
import time
import random
import pngfunctions
from typing import Tuple


#questions
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
        self.directory = "mazes/" + self.name + "-" + str(self.size) + "x" + str(self.size) + "-" + hex(random.randint(0, 500))

    def generate(self, history_log=None):

        start_time = time.time()

        the_frontier = {(1, 1)}  # set
        self.matrix[1][1].visited = True

        while the_frontier:
            x, y = the_frontier.pop()
            # check all directions for new frontiers, add to frontier
            if y - 2 > 0 and not self.matrix[x][y - 2].visited:  # check north
                the_frontier.append((x, y - 2))

            if y + 2 < len(self.matrix) and not self.matrix[x][y + 2].visited:  # check south
                the_frontier.append((x, y + 2))

            if x - 2 > 0 and not self.matrix[x - 2][y].visited:  # check east
                the_frontier.append((x - 2, y))

            if x + 2 < len(self.matrix) and not self.matrix[x + 2][y].visited:  # check west
                the_frontier.append((x + 2, y))

            if len(the_frontier) > 0:
                next_node = random.choice(the_frontier)  # pick next node
                self.maze.connect(self.matrix[x][y], self.matrix[next_node[0]][next_node[1]], history_log)  # Nath what do for history here?
                self.matrix[next_node[0]][next_node[1]].visited = True
                the_frontier.append(next_node)

        self.duration = time.time() - start_time

    def save_png(self):
        self.maze.image.save("mazes/" + self.name + "-" + str(self.size) + "x" + str(self.size) + "-" +
                             str(float("%.5f" % self.duration)) + "s.png", "PNG")

    def print_results(self):
        super().print_results()

    def maze_generator_factory(self, size: int):
        pass



generator = GeneratePrimms(11)
generator.generate()
generator.save_png()

#to run right click file and run file