from solverb import SolveRB


def main():
     rb = SolveRB()
     rb.import_png("pngs/101x101-RB-0.01905s.png")
     the_stack = rb.solve((1, 1), (99, 99))

     print(str(the_stack))

     rb.save_solution(the_stack)


if __name__ == "__main__":
    main()
