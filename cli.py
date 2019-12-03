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
        while True:
            options = ["Generate a new maze", "Solve an existing maze", "Quit"]

            print("--------------------------------------------------")
            print("                    Maze Machine                  ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print(" Please select an operation:                      ")
            for index in range(len(options)):
                print(" (%s) %s" % (str(index + 1), options[index]))
            print("--------------------------------------------------")

            operation = input(">>")
            if int(operation) == len(options):
                break
            if int(operation) >= len(options):
                print("Please choose one of the specified options")
            elif options[int(operation) - 1] == "Generate a new maze":
                self.generate_maze()
            elif options[int(operation) - 1] == "Solve an existing maze":
                self.solve_maze()

    def generate_maze(self):
        while True:
            options = ["Recursive Backtracking", "Back"]
            print("--------------------------------------------------")
            print("                  Generate a Maze                 ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print(" Please select an algorithm:                      ")
            for index in range(len(options)):
                print(" (%s) %s" % (str(index + 1), options[index]))
            print("--------------------------------------------------")

            operation = input(">>")
            if int(operation) == len(options):
                break
            if int(operation) > len(options):
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
        while True:
            options = ["Recursive Backtracking", "A-Star", "Back"]

            print("--------------------------------------------------")
            print("                    Solve a Maze                  ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print(" Please select an algorithm:                      ")
            for index in range(len(options)):
                print(" (%s) %s" % (str(index + 1), options[index]))
            print("--------------------------------------------------")

            operation = input(">>")
            if int(operation) == len(options):
                break
            if int(operation) >= len(options):
                print("Please choose one of the specified options")
            elif options[int(operation) - 1] == "Recursive Backtracking":
                solve_generic("Recursive Backtracking", SolveRB())
            elif options[int(operation) - 1] == "A-Star":
                solve_generic("A-Star", SolveAStar())


def solve_generic(title, solver):
    while True:
        path = "./mazes/"
        options = [f for f in listdir(path) if isfile(join(path, f))] + ["Back"]
        width = 50
        header = " " * ((width - len(title)) // 2) + title + " " * ((width - len(title)) // 2)
        print("--------------------------------------------------")
        print(header)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        print(" Please select a PNG to import                    ")
        for index in range(len(options)):
            print(" (%s) %s" % (str(index + 1), options[index]))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - ")

        user_input = input(">>")
        if int(user_input) == len(options):
            break
        solver.import_png(path + options[int(user_input) - 1])
        history = []
        solution = solver.solve((1, 1), (solver.maze.size - 2, solver.maze.size - 2), history)
        print("Solution Found.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("Would you like to save the process as well as the solution? (Y/N)")
        answer = None
        while answer is None:
            answer = input(">>")
            if answer.upper() != "Y" and answer.upper() != "N":
                print("Please answer with yes (Y) or no (N)")
                answer = None

        if answer.upper() == "Y":
            print("Saving solution and history.")
            solver.save_solution(solution, history)
            # print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
            # print("Would you like to compile a gif of the history? (Y/N)")
            # gif_answer = None
            # while gif_answer is None:
            #     gif_answer = input(">>")
            #     if gif_answer.upper() != "Y" and gif_answer.upper() != "N":
            #         print("Please answer with yes (Y) or no (N)")
            #         gif_answer = None
            #
            # if gif_answer.upper() == "Y":
            #     print("Compiling gif.")
            #     solver.compile_gif()

        else:
            print("Saving solution.")
            solver.save_solution(solution)

        print("To compile a gif of the solution, use")
        print("gifski --fps 60 -o 60.gif *.png")
        
            # gif_answer = None
            # while gif_answer is None:
            #     gif_answer = input(">>")
            #     if gif_answer.upper() != "Y" and gif_answer.upper() != "N":
            #         print("Please answer with yes (Y) or no (N)")
            #         gif_answer = None
            #
            # if gif_answer.upper() == "Y":
            #     print("Compiling gif.")
                # solver.compile_gif()


if __name__ == "__main__":
    main()
