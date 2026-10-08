from Chromatophore import Chromatophore
import matplotlib.pyplot  as plt

def create_grid(size):
    grid = [[Chromatophore(x, y) for x in range(size)] for y in range(size)]

    return grid

def display(grid):
    data = [
        [1 if ch.on else 0 for ch in row]
        for row in grid
    ]

    plt.imshow(data, cmap="gray_r", vmin=0, vmax=1)
    plt.xticks([])
    plt.yticks([])
    plt.show()