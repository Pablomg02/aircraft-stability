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
        # downwash angle is not considered. It has to be added in the future
        xw_unit = self.aircraft.wing.posX / self.aircraft.ref_chord
        xh_unit = self.aircraft.horizontal_stab.posX / self.aircraft.ref_chord
 
        volume_tail = self.aircraft.horizontal_stab.surface * (self.aircraft.horizontal_stab.posX - self.aircraft.wing.posX) / (self.aircraft.ref_chord * self.aircraft.wing.surface)
        No_unit = xw_unit + (self.aircraft.horizontal_stab.clalpha / self.aircraft.wing.clalpha) * volume_tail * self.aircraft.horizontal_stab.efficiency
        return No_unit * self.aircraft.ref_chord



    """def neutral_point(self):
        # downwash angle is not considered. It has to be added in the future
        a = (self.aircraft.horizontal_stab.surface / self.aircraft.wing.surface) * self.aircraft.horizontal_stab.efficiency * self.aircraft.horizontal_stab.clalpha
        xw_unit = self.aircraft.wing.posX / self.aircraft.wing.chord
        xh_unit = self.aircraft.horizontal_stab.posX / self.aircraft.horizontal_stab.chord
        No_unit = xw_unit + (xh_unit - xw_unit) *(a / (self.aircraft.wing.clalpha + a))
        return No_unit * self.aircraft.wing.chord"""
    
    def trim(self):
        # downwash angle is not considered. It has to be added in the future
        # Trim needed to fly straight and level at angle self.aircaft.angle 

        xw_unit = self.aircraft.wing.posX / self.aircraft.ref_chord
        xh_unit = self.aircraft.horizontal_stab.posX / self.aircraft.ref_chord
        xcg_unit = self.aircraft.cgX / self.aircraft.ref_chord

        #Cm0 Cmacwb - at * performance tail * volume tail * (it - iwb - epsilon0(=0))
        volume_tail = self.aircraft.horizontal_stab.surface * (self.aircraft.horizontal_stab.posX - self.aircraft.wing.posX) / (self.aircraft.ref_chord * self.aircraft.wing.surface)
        cm0 = self.aircraft.wing.cm0 - self.aircraft.horizontal_stab.clalpha * volume_tail * self.aircraft.horizontal_stab.efficiency * (self.aircraft.horizontal_stab.it - self.aircraft.wing.iw)

        cmalpha = self.aircraft.wing.clalpha * (xcg_unit - xw_unit) - (self.aircraft.horizontal_stab.clalpha * volume_tail * self.aircraft.horizontal_stab.efficiency)
        cmdelta = - self.aircraft.horizontal_stab.clalpha * self.aircraft.horizontal_stab.efficiency * self.aircraft.horizontal_stab.control_surface * volume_tail
        trim = - (cm0/cmdelta) - ((cmalpha/cmdelta) * (self.aircraft.angle + self.aircraft.wing.iw))
        return cm0, cmalpha, cmdelta, trim
        #return(- (cm0/cmdelta) - (cmalpha/cmdelta) * self.aircraft.angle)