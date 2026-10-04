class Chromatophore:

    def __init__(self, x: float, y: float, motorunits: list):
        self.status = 'off' # [on/off], initialized 
        self.coordinates = [x,y] # position
        self.mu = motorunits #list of motor units that control the chromatophore

    def contract(self):
        self.status = 'on'

    def relax(self):
        self.status = 'off'