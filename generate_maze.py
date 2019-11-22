from pnghandler import PngHandler


def main():
    handler = PngHandler(21)
    handler.setup_grid()
    handler.image.save("test.png", "PNG")


if __name__ == "__main__":
    main()
