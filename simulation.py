class Simulation:
    def __init__(self, aircraft, velocity, density = 1.225):
        self.aircraft = aircraft
        self.density = density
        self.velocity = velocity

    def lift_wing(self): #lift of the wing
        result = 0.5 * self.density * self.velocity**2 * self.aircraft.wing.area * self.aircraft.wing.cl
        return result
    
    def lift_stab(self): #lift of the horizontal stabilizer
        result = 0.5 * self.density * self.velocity**2 * self.aircraft.horizontal_stab.area * self.aircraft.horizontal_stab.cl
        return result #it will be negative if cl < 0
    
    def lift(self): #total lift
        result = self.lift_wing() + self.lift_stab()
        return result

    def neutral_point(self):
        print("Chillout dude, I'm working on it :)")
