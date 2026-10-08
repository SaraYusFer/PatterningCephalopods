class MotorUnit:

    def __init__(self, motorunit_id: int, x: int, y: int):

        self.id = motorunit_id # identify the motor unit
        self.coordinates = [x,y] # position of the motor unit (necessary to calculate the neighborhood)
        self.action_potential = 0.0 # action potential is the electrical current
        self.chromatophores = [] # cluster of chromatophores controlled by this motor unit, identified by their (x,y) position
        self.neighborhood = [] # Motur units it is connected to
        self.signal = 'contract' # Contract or relax the chromatophores controlled by this MU, simplification of the calcium/potassium pathway

    """ 
    Control of chromatophores
    First model uses simplification; the signal from previous timestep is reversed when current passes
    through the motor unit
    """
    def status_change(self):
        if self.signal == 'relax':
            self.signal == 'contract'

        elif self.signal == 'contract':
            self.signal == 'relax'