# A* search algorithm for solving the maze
from mazesolver import MazeSolver
import time


class SolveAStar(MazeSolver):

    def __init__(self):
        super().__init__()
        self.name = "solutionAStar"

    def solve(self, beginning, end, history_log=None):
        super().solve(beginning, end)
        start_time = time.time()

        the_open = {}
        the_closed = set()

        # start at beginning
        # add beginning to open set
        the_open[beginning] = Node(beginning)

        while the_open:
            node = min(the_open.values())
            the_open.pop(node.location, None)
            the_closed.add(node.location)
            history_log.append(("closed", node.location))
            x, y = node.location

            if (x, y) == end:
                self.duration = time.time() - start_time
                return Node.calculate_ancestry(node)

            successors = []

            # generate children nodes and add to open set (N,S,E,W)
            # check north
            if y - 1 > 0 and self.maze.image.getpixel((x, y-1)) == (255, 255, 255):
                successors.append(Node((x, y - 1), node))

            # check south
            if y + 1 < self.maze.size and self.maze.image.getpixel((x, y+1)) == (255, 255, 255):
                successors.append(Node((x, y + 1), node))

            # check east
            if x - 1 > 0 and self.maze.image.getpixel((x - 1, y)) == (255, 255, 255):
                successors.append(Node((x - 1, y), node))

            # check west
            if x + 1 < self.maze.size and self.maze.image.getpixel((x + 1, y)) == (255, 255, 255):
                successors.append(Node((x + 1, y), node))

            for child in successors:
                if child.location not in the_closed:
                    if child.parent:
                        child.g = node.g + 1  # distance to start through ancestry. 0 if beginning
                    else:
                        child.g = 0

                    child.h = abs(child.location[0] - end[0]) + abs(child.location[1] - end[1])  # manhattan distance to finish
                    child.f = int((child.g + child.h))  # (g + h)
                    if child not in the_open:
                        the_open[child.location] = child
                        history_log.append(("open", child.location))
                    else:
                        open_neighbor = the_open[child.location]
                        if child.g < open_neighbor.g:
                            open_neighbor.g = child.g
                            open_neighbor.parent = child.parent

            the_closed.add(node.location)
            history_log.append(("closed", node.location))


class Node:

    def __init__(self, location, parent=None):
        self.parent = parent
        self.location = location

        self.g = 0
        self.h = 0
        self.f = 0

    @staticmethod
    def calculate_ancestry(node):
        the_stack = [node.location]
        parent = node.parent
        while parent is not None:
            the_stack.append(parent.location)
            parent = parent.parent
        return the_stack

    def __eq__(self, other):
        return self.location == other.location

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __hash__(self):
        return hash(self.location)
