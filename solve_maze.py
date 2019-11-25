from solverb import SolveRB
from solveastar import SolveAStar


def main():
     # rb = SolveRB()
     # rb.import_png("pngs/501x501-RB-0.22689s.png")
     # the_stack = rb.solve((1, 1), (499, 499))
     #
     # #print(str(the_stack))
     #
     # rb.save_solution(the_stack)

     star = SolveAStar()
     star.import_png("pngs/1001x1001-RB-1.12744s.png")
     solution = star.solve((1, 1), (999, 999))

     solution.reverse()
     star.save_solution(solution)


if __name__ == "__main__":
    main()
