import aircraft
# Your code here
import simulation

# Create an aircraft object
avion = aircraft.Aircraft(250000, 3, 6.65, angle = 0)
avion.wing = aircraft.Wing(4, 383.70, 6.65, 0.2, 5.6, cm0 = -0.15)
avion.horizontal_stab = aircraft.Horizontal_stab(45, 95, 4.77, 0.11, 0)
avion.thrust = aircraft.Thrust(100)

# Create a simulation object
sim = simulation.Simulation(avion, 236.5)

# Print the results
print(f"Total lift: {sim.lift()}")
print(f"Wing lift: {sim.lift_wing()}")
print(f"Stabilizer lift: {sim.lift_stab()}")
print(f"Neutral point: {sim.neutral_point()}")
print(f"Trim: {sim.trim()}")

# :D