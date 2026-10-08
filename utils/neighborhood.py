"""
Returns the neighborhood of an element (chromatophore or motor unit) given its coordinates
Included: Moore, Von Neumann
Expansion: Radial neighborhood (based on retinal models)
"""

def calculate_neighborhood(x: int, y: int, nb: str):
    # TO DO: handle boundaries
    neighborhood = {}
    if nb == 'Moore':
        neighborhood = {[x-1, y], [x+1, y], [x, y+1], [x, y-1], [x-1, y-1], [x+1, y+1], [x-1, y+1], [x+1, y-1]}

    elif nb == 'Von Neumann':
        neighborhood = {[x-1, y], [x+1, y], [x, y+1], [x, y-1]}

    return neighborhood