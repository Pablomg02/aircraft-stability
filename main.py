import aircraft
# Your code here
import simulation

# Create an aircraft object
avion = aircraft.Aircraft(250000, 4, 6.65, angle = 0)
avion.wing = aircraft.Wing(5.65, 383.70, 6.65, 0.0886, 7.26, cm0 = -0.076)
avion.horizontal_stab = aircraft.Horizontal_stab(46.9, 95, 4.77, 0.034, 0)
avion.thrust = aircraft.Thrust(100)

# Create a simulation object
sim = simulation.Simulation(avion, 236.5)


# Print the results
print(f"Neutral point: {sim.neutral_point()}")
print(f"Trim: {sim.trim()}")

