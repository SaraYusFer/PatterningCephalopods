class Chromatophore:

    def __init__(self, x: int, y: int):
        self.status = 'off' # [on/off], initialized on off (contracted, not visible) 
        self.coordinates = [x,y] # position
        self.mu = [] #list of motor units that control the chromatophore

    def contract(self):
        self.status = 'on'

    def relax(self):
        self.status = 'off'