class Simulation:
    def __init__(self, aircraft, velocity, density = 1.225):
        self.aircraft = aircraft
        self.density = density
        self.velocity = velocity
        self.q = 0.5 * self.density * self.velocity**2

    def lift_wing(self): #lift of the wing
        cl = self.aircraft.wing.clalpha * (self.aircraft.angle + self.aircraft.wing.iw)
        result = self.q * self.aircraft.wing.surface * cl
        return result
    
    def lift_stab(self): #lift of the horizontal stabilizer
        cl = self.aircraft.horizontal_stab.clalpha * (self.aircraft.angle + self.aircraft.horizontal_stab.it)
        # it is not considering epsilon, the downwash angle
        result = self.q * self.aircraft.horizontal_stab.surface * cl * self.aircraft.horizontal_stab.efficiency
        return result #it will be negative if cl < 0
    
    def lift(self): #total lift
        result = self.lift_wing() + self.lift_stab()
        return result

    def neutral_point(self):
        a = (self.aircraft.horizontal_stab.surface / self.aircraft.wing.surface) * self.aircraft.horizontal_stab.efficiency * self.aircraft.horizontal_stab.efficiency
        xw_unit = self.aircraft.wing.posX / self.aircraft.wing.chord
        xh_unit = self.aircraft.horizontal_stab.posX / self.aircraft.horizontal_stab.chord
        No_unit = (self.aircraft.wing.clalpha*xw_unit + a*xh_unit) / (self.aircraft.wing.clalpha + a)
        return No_unit * self.aircraft.wing.chord
