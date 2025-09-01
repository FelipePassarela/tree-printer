import argparse

from tree_printer.tree_canvas import tree_canvas


def main():
    parser = argparse.ArgumentParser(description="Prints trees in the terminal.")
    parser.add_argument("--trees", type=int, default=5, help="Number of trees")
    parser.add_argument(
        "--cols", type=int, default=120, help="Number of canvas columns"
    )
    args = parser.parse_args()

    print("Tree Printer!")

    canvas = tree_canvas(trees=args.trees, cols=args.cols)
    print(canvas)


if __name__ == "__main__":
    main()
