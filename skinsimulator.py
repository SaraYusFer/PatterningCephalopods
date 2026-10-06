from Chromatophore import Chromatophore
import matplotlib.pyplot  as plt

def create_grid():

    grid = [[Chromatophore(x, y) for x in range(24)] for y in range(24)]

    return grid

def display(grid):
    data = [
        [1 if obj.on else 0 for obj in row]
        for row in grid
    ]

    plt.imshow(data, cmap="gray_r", vmin=0, vmax=1)
    plt.xticks([])
    plt.yticks([])
    plt.show()