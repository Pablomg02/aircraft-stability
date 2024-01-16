class Aircraft:
    # Add default values for attributes
    def __init__(self, mass, cgX, ref_chord, angle = 0, wing=None, horizontal_stab=None, thrust=None):
        self.wing = wing
        self.horizontal_stab = horizontal_stab
        self.thrust = thrust
        self.mass = mass
        self.cgX = cgX
        self.angle = angle # Angle of attack of the body [degrees]
        self.ref_chord = ref_chord # Reference chord of the body [m] (usually the wing's chord)


class Wing:
    # Add default values for attributes
    def __init__(self, posX, surface, chord, clalpha, iw, cd = 0, cm0 = 0):
        self.posX = posX # Distance from 0 to the wing's aerodynamic center
        self.surface = surface # Surface of the wing
        self.chord = chord # Chord of wing
        self.clalpha = clalpha # Lift coefficient per degree of angle of attack
        self.cd = cd # Drag coefficient. To be defined later
        self.cm0 = cm0 # Moment coefficient at 0 AoA in the aerodynamic center
        self.iw = iw # Angle of the wing's NSL with respect to the fuselage line [degrees]
        #posY = 0 since the wing is on the fuselage line


class Horizontal_stab():
    def __init__(self, posX, surface, chord, clalpha, it, cd = 0, cm0 = 0, posY = 0, efficiency = 1):
        self.posX = posX # Distance from 0 to the stabilizer's aerodynamic center [m]
        self.posY = posY # Distance from fusselage line to the stabilizer's aerodynamic center [m]
        self.surface = surface # Area of the stabilizer [m^2]
        self.chord = chord # Chord of the stabilizer [m]
        self.clalpha = clalpha # Lift coefficient per degree of angle of attack
        self.cd = cd # Drag coefficient
        self.cm0 = cm0 # Moment coefficient at 0 AoA in the aerodynamic center 
        self.efficiency = efficiency # Efficiency of the stabilizer
        self.it = it # Angle of the stabilizer's NSL with respect to the fuselage line [degrees]

class Thrust():
    def __init__(self, thrust, posY = 0):
        self.posY = posY # Distance from 0 to the engine's thrust center [m]
        self.thrust = thrust # Thrust of the engine [Newtons]