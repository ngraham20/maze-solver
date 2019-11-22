from maze import Maze
import time
import random


def main():
    size = 2000
    maze = Maze(size)
    maze.setup_grid()

    matrix = maze.matrix

    start_time = time.time()

    the_stack = [(1, 1)]
    matrix[1][1].visited = True

    while the_stack:
        x, y = the_stack.pop()
        pool = []
        if y - 2 > 0 and not matrix[x][y - 2].visited:  # check north
            pool.append((x, y - 2))

        if y + 2 < len(matrix) and not matrix[x][y + 2].visited:  # check south
            pool.append((x, y + 2))

        if x - 2 > 0 and not matrix[x - 2][y].visited:  # check east
            pool.append((x - 2, y))

        if x + 2 < len(matrix) and not matrix[x + 2][y].visited:  # check west
            pool.append((x + 2, y))

        if len(pool) > 0:
            the_stack.append((x, y))
            next_node = random.choice(pool)
            maze.connect(matrix[x][y], matrix[next_node[0]][next_node[1]])
            matrix[next_node[0]][next_node[1]].visited = True
            the_stack.append(next_node)

    duration = time.time() - start_time
    print("RECURSIVE BACKTRACKER: %s x %s" % (maze.size, maze.size))
    print("--- %s seconds ---" % duration)
    
    maze.image.save("pngs/test.png", "PNG")


if __name__ == "__main__":
    main()
