import aircraft
# Your code here
import simulation

# Create an aircraft object
avion = aircraft.Aircraft(1000, 0.5, 2, 0)
avion.wing = aircraft.Wing(2, 20, 2, 0.1, 5)
avion.horizontal_stab = aircraft.Horizontal_stab(5, 5, 1, 0.1, -1)
avion.thrust = aircraft.Thrust(2000)

# Create a simulation object
sim = simulation.Simulation(avion, 100)

# Print the results
print(f"Total lift: {sim.lift()}")
print(f"Wing lift: {sim.lift_wing()}")
print(f"Stabilizer lift: {sim.lift_stab()}")
print(f"Neutral point: {sim.neutral_point()}")

# :D