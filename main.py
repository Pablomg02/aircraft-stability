import aircraft
# Your code here
import simulation

# Create an aircraft object
avion = aircraft.Aircraft(1000, 0.5, 3, angle = 0)
avion.wing = aircraft.Wing(3, 30, 3, 0.1, 5)
avion.horizontal_stab = aircraft.Horizontal_stab(9, 5, 1, 0.1, -2)
avion.thrust = aircraft.Thrust(100)

# Create a simulation object
sim = simulation.Simulation(avion, 100)

# Print the results
print(f"Total lift: {sim.lift()}")
print(f"Wing lift: {sim.lift_wing()}")
print(f"Stabilizer lift: {sim.lift_stab()}")
print(f"Neutral point: {sim.neutral_point()}")

# :D