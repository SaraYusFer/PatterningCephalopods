from MotorUnit import MotorUnit

"""
Instantiate motor units and connect them
Connectivity based on neighborhood type: Moore, Von Neumann
"""
def create_network(size, neighborhood):
    pass

"""
Connect motor units to chromatophores and viceversa
"""
def innervate_chromatophores(grid, network):
    # Do I need the definition of a cluster here? where do I specify how many chromatophores
    # a motor unit controls? and how to select them?
    pass

"""
Signal propagation dynamics
Input is motor units (ids) that are excited in t=0
tmax is the number of steps to run the dynamics
""" 
def propagate_signal(input, network, tmax): 
    pass