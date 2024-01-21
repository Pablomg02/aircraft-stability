class Simulation:
    def __init__(self, aircraft, velocity, density = 1.225):
        self.aircraft = aircraft
        self.density = density
        self.velocity = velocity
        # Calculate the rest of the variables
        self.q = 0.5 * self.density * self.velocity**2
        self.volume_tail = self.aircraft.horizontal_stab.surface * (self.aircraft.horizontal_stab.posX - self.aircraft.wing.posX) / (self.aircraft.ref_chord * self.aircraft.wing.surface)
        self.xw_unit = self.aircraft.wing.posX / self.aircraft.ref_chord
        self.xh_unit = self.aircraft.horizontal_stab.posX / self.aircraft.ref_chord
        self.xcg_unit = self.aircraft.cgX / self.aircraft.ref_chord
        self.cm0 = self.aircraft.wing.cm0 - self.aircraft.horizontal_stab.clalpha * self.volume_tail * self.aircraft.horizontal_stab.efficiency * (self.aircraft.horizontal_stab.it - self.aircraft.wing.iw)
        self.cmalpha = self.aircraft.wing.clalpha * (self.xcg_unit - self.xw_unit) - (self.aircraft.horizontal_stab.clalpha * self.volume_tail * self.aircraft.horizontal_stab.efficiency)
        self.cmdelta = - self.aircraft.horizontal_stab.clalpha * self.aircraft.horizontal_stab.efficiency * self.aircraft.horizontal_stab.control_surface * self.volume_tail
        


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
        # downwash angle is not considered. It has to be added in the future
        No_unit = self.xw_unit + (self.aircraft.horizontal_stab.clalpha / self.aircraft.wing.clalpha) * self.volume_tail * self.aircraft.horizontal_stab.efficiency
        return No_unit * self.aircraft.ref_chord


    def trim(self):
        # downwash angle is not considered. It has to be added in the future
        # Trim needed to fly straight and level at angle self.aircaft.angle 
        trim = - (self.cm0/self.cmdelta) - ((self.cmalpha/self.cmdelta) * (self.aircraft.angle + self.aircraft.wing.iw))
        return trim
