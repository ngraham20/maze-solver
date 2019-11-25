from mazegenerator import MazeGenerator
from mazesolver import MazeSolver
from recursivebacktracker import RecursiveBacktracker
from solveastar import SolveAStar
from solverb import SolveRB
from os import listdir
from os.path import isfile, join


def main():
    cli = CLI()
    cli.main_menu()


class CLI:

    def __init__(self):

        self.decision = ''
        self.operation = ''

    def main_menu(self):  # print main menu

        options = ["Generate a new maze", "Solve an existing maze", "Quit"]

        print("--------------------------------------------------")
        print("                    Maze Machine                  ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        print(" Please select an operation:                      ")
        for index in range(len(options)):
            print(" (%s) %s" % (str(index + 1), options[index]))
        print("--------------------------------------------------")

        self.operation = input(">>")
        if int(self.operation) >= len(options):
            print("Please choose one of the specified options")
        elif options[int(self.operation) - 1] == "Generate a new maze":
            self.generate_maze()
        elif options[int(self.operation) - 1] == "Solve an existing maze":
            self.solve_maze()

    def generate_maze(self):
        options = ["Recursive Backtracking", "Quit"]
        print("--------------------------------------------------")
        print("                  Generate a Maze                 ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        print(" Please select an algorithm:                      ")
        for index in range(len(options)):
            print(" (%s) %s" % (str(index + 1), options[index]))
        print("--------------------------------------------------")

        operation = input(">>")
        if int(operation) >= len(options):
            print("Please choose one of the specified options")
        elif options[int(operation) - 1] == "Recursive Backtracking":
            size = self.generation_settings("Recursive Backtracking")
            rb = RecursiveBacktracker(size)
            rb.generate()
            rb.print_duration()
            rb.save_png()

    @staticmethod
    def generation_settings(title):
        width = 50
        header = " " * ((width - len(title)) // 2) + title + " " * ((width - len(title)) // 2)
        print("--------------------------------------------------")
        print(header)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        print(" Please enter the maze size (N x N):              ")

        response = int(input(">>"))
        if response > 10000:
            print("That's way to big. Exiting.")
            return None
        else:
            return response

    def solve_maze(self):
        options = ["Recursive Backtracking", "A-Star", "Quit"]

        print("--------------------------------------------------")
        print("                    Solve a Maze                  ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        print(" Please select an algorithm:                      ")
        for index in range(len(options)):
            print(" (%s) %s" % (str(index + 1), options[index]))
        print("--------------------------------------------------")

        self.operation = input(">>")
        if int(self.operation) >= len(options):
            print("Please choose one of the specified options")
        elif options[int(self.operation) - 1] == "Recursive Backtracking":
            self.solve_generic("Recursive Backtracking", SolveRB())
        elif options[int(self.operation) - 1] == "A-Star":
            self.solve_generic("A-Star", SolveAStar())

    # @staticmethod
    # def solve_rb():
    #     path = "./mazes/"
    #     options = [f for f in listdir(path) if isfile(join(path, f))]
    #     print("--------------------------------------------------")
    #     print("         Solve with Recursive Backtracking        ")
    #     print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
    #     print(" Please select a PNG to import                    ")
    #     for index in range(len(options)):
    #         print(" (%s) %s" % (str(index + 1), options[index]))
    #     print("--------------------------------------------------")
    #
    #     user_input = input(">>")
    #     rb = SolveRB()
    #     rb.import_png(path + options[int(user_input) - 1])
    #     solution = rb.solve((1, 1), (rb.maze.size - 2, rb.maze.size - 2))
    #     rb.save_solution(solution)

    @staticmethod
    def solve_generic(title, solver):
        path = "./mazes/"
        options = [f for f in listdir(path) if isfile(join(path, f))]
        width = 50
        header = " " * ((width - len(title)) // 2) + title + " " * ((width - len(title)) // 2)
        print("--------------------------------------------------")
        print(header)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        print(" Please select a PNG to import                    ")
        for index in range(len(options)):
            print(" (%s) %s" % (str(index + 1), options[index]))
        print("--------------------------------------------------")

        user_input = input(">>")
        solver.import_png(path + options[int(user_input) - 1])
        solution = solver.solve((1, 1), (solver.maze.size - 2, solver.maze.size - 2))
        solver.save_solution(solution)

    # def solve_astar(self):
    #     path = "./mazes/"
    #     options = [f for f in listdir(path) if isfile(join(path, f))]
    #     print("--------------------------------------------------")
    #     print("                Solve with A-Star                 ")
    #     print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
    #     print(" Please select a PNG to import                    ")
    #     for index in range(len(options)):
    #         print(" (%s) %s" % (str(index + 1), options[index]))
    #     print("--------------------------------------------------")
    #
    #     user_input = input(">>")
    #     star = SolveAStar()
    #     star.import_png(path + options[int(user_input) - 1])
    #     solution = star.solve((1, 1), (star.maze.size - 2, star.maze.size - 2))
    #     star.save_solution(solution)


if __name__ == "__main__":
    main()