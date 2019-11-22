from maze import Maze


def main():
    maze = maze(21)
    maze.setup_grid()

    matrix = maze.matrix

    # maze.connect(matrix[1][1], matrix[1][3])
    # maze.connect(matrix[3][5], matrix[3][7])
    # maze.connect(matrix[5][5], matrix[7][5])
    # maze.connect(matrix[1][9], matrix[3][9])



    maze.image.save("pngs/test.png", "PNG")


if __name__ == "__main__":
    main()
