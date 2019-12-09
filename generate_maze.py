from generaterb import GenerateRB


def main():
    rb = GenerateRB(100)
    rb.generate()
    rb.print_results()
    rb.save_png()


if __name__ == "__main__":
    main()
