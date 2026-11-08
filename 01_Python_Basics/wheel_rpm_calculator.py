# Physics to Technology - Lesson 1, Part 3
# EmpwireBot Wheel RPM Calculator 

import math
print("EmpwireBot Wheel Analysis")
print("--------------------------------------------------")

# Robot parameters 
wheel_diameter = 0.0676 # meters
pulse_per_revolution = 20 # pulses per revolution

# User inputs
total_pulses = int(input("Enter total encoder pulses: "))
time_seconds = float(input("Enter measurement time in seconds: "))

#Check measurement time 
if time_seconds <= 0: 
    print("Error: Measurement time must be greater than zero.")
else:
    # Engineering Calculations
    revolutions = total_pulses / pulse_per_revolution
    rpm = (revolutions / time_seconds) * 60

    circumference = math.pi * wheel_diameter
    velocity = (rpm * circumference) / 60

# Display results
print("\nResults:")
print("--------------------------------------------------")

print("Wheel Revolutions:", revolutions)
print("Motor RPM:", round(rpm, 2))
 
print("Linear Velocity:" , round(velocity, 4), "m/s") 
