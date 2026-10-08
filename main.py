import skinsimulator
import networksimulator


# Global values: simulation parameters can be changed here
SKIN_GRID_SIZE = 20
NETWORK_SIZE = 20
INPUT = {}
TMAX = 100

def initialize_simulation():
    skin_grid = skinsimulator.create_grid(SKIN_GRID_SIZE)
    network = networksimulator.create_network(NETWORK_SIZE)

    networksimulator.innervate_chromatophores(skin_grid, network)

    skinsimulator.display(skin_grid)

    return skin_grid, network

# Create experimental conditions and run experiment
def experiment(network):
    networksimulator.propagate_signal(INPUT, network, TMAX)

def main():
    skin, network = initialize_simulation()
    experiment(network)