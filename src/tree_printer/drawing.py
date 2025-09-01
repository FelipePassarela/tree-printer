import random
from math import ceil, floor


def draw_treetop(
    treetop_height: int,
    tree_width: int,
    canvas: list[str],
    current_center: int,
    true_cols: int,
):
    for i in range(treetop_height):
        current_treetop_width = int(i * tree_width / (2 * treetop_height))
        start = (current_center - 1) - current_treetop_width
        end = (current_center + 1) + current_treetop_width

        for j in range(start, end):
            treetop_char = get_chars()[0]
            canvas[i * true_cols + j] = treetop_char


def draw_trunk(
    trunk_height: int,
    trunk_width: int,
    canvas: list[str],
    current_center: int,
    true_cols: int,
    rows: int,
):
    for i in range(rows - trunk_height, rows):
        start = current_center - floor(trunk_width / 2)
        end = current_center + ceil(trunk_width / 2)

        for j in range(start, end):
            trunk_char = get_chars()[1]
            canvas[i * true_cols + j] = trunk_char


def get_chars() -> tuple[str, str, str]:
    treetop_chars = [
        "\x1b[38;5;34m&\033[0m",
        "\x1b[38;5;28m@\033[0m",
        "\x1b[38;5;106m%\033[0m",
        "\x1b[38;5;22m$\033[0m",
    ]
    trunk_chars = [
        "\x1b[38;5;136m|\033[0m",
        "\x1b[38;5;130m|\033[0m",
        "\x1b[38;5;94m#\033[0m",
        "\x1b[38;5;94m/\033[0m",
    ]

    rand_treetop = random.choice(treetop_chars)
    # Occasionally add a apple to the treetop
    rand_treetop = "\x1b[38;5;9m@\033[0m" if random.random() < 0.02 else rand_treetop
    rand_trunk = random.choice(trunk_chars)
    # Occasionally add a flower to the background
    rand_bg = "*" if random.random() < 0.03 else " "

    return rand_treetop, rand_trunk, rand_bg
