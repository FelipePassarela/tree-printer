from math import ceil

from tree_printer.drawing import draw_treetop, draw_trunk, get_chars


def tree_canvas(
    trees: int = 7,
    cols: int = 126,
) -> str:
    if not cols % trees == 0:
        # Ensure n_cols is multiple of n_trees so that there is no leftover at the end
        proper_cols = cols - (cols % trees)
        cols = proper_cols

    true_cols = cols + 1  # To accommodate '\n's
    tree_width = int(cols / trees)
    rows = ceil(tree_width * 9 / 16)

    trunk_height = int(rows * 0.3)
    trunk_width = int(tree_width * 0.15)
    if tree_width % 2 == 0 and trunk_width % 2 == 1:
        trunk_width += 1
    elif tree_width % 2 == 1 and trunk_width % 2 == 0:
        trunk_width += 1

    canvas = []
    for _ in range(rows):
        for _ in range(cols):
            bg_char = get_chars()[2]
            canvas.append(bg_char)
        canvas.append("\n")

    for k in range(trees):
        current_offset = k * tree_width
        current_center = current_offset + int(tree_width / 2)
        treetop_height = rows - trunk_height

        draw_treetop(treetop_height, tree_width, canvas, current_center, true_cols)
        draw_trunk(trunk_height, trunk_width, canvas, current_center, true_cols, rows)

    return "".join(canvas)
