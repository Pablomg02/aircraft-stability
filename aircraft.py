class Aircraft:
    # Add default values for attributes
    def __init__(self, mass, cgX, wing=None, horizontal_stab=None, thrust=None):
        self.wing = wing
        self.horizontal_stab = horizontal_stab
        self.thrust = thrust
        self.mass = mass
        self.cgX = cgX


class Wing:
    # Add default values for attributes
    def __init__(self, posX, area, chord, cl, cd = 0, cm0 = 0):
        self.posX = posX # Distance from 0 to the wing's aerodynamic center
        self.area = area
        self.chord = chord # Chord of wing
        self.cl = cl # Lift coefficient. 
        self.cd = cd # Drag coefficient
        self.cm0 = cm0 # Moment coefficient at 0 AoA in the aerodynamic center
        #posY = 0 since the wing is on the fuselage line


class Horizontal_stab():
    def __init__(self, posX, area, chord, cl, cd = 0, cm0 = 0, posY = 0):
        self.posX = posX # Distance from 0 to the stabilizer's aerodynamic center [m]
        self.posY = posY # Distance from fusselage line to the stabilizer's aerodynamic center [m]
        self.area = area # Area of the stabilizer [m^2]
        self.chord = chord # Chord of the stabilizer [m]
        self.cl = cl # Lift coefficient
        self.cd = cd # Drag coefficient
        self.cm0 = cm0 # Moment coefficient at 0 AoA in the aerodynamic center 

class Thrust():
    def __init__(self, thrust, posY = 0):
        self.posY = posY # Distance from 0 to the engine's thrust center [m]
        self.thrust = thrust # Thrust of the engine [Newtons]