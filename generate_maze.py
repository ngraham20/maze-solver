from recursivebacktracker import RecursiveBacktracker


def main():
    rb = RecursiveBacktracker(100)
    rb.generate()
    rb.print_duration()
    rb.save_png()


if __name__ == "__main__":
    main()
