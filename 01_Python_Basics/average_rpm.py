# Physics to Technology - Lesson 1, Part 3, exercise 1 
# EmpwireBot Wheel average RPM Calculator

import math 
print("EmpwireBot Wheel Average RPM Analysis")

print("--------------------------------------------------")

# robot parameters
wheel_diameter = 0.0676 # meters
pulse_per_revolution = 20 # pulses per revolution

#user inputs 
total_pulses_FR = int(input("Enter total encoder pulses for front right wheel: "))
total_pulses_FL = int(input("Enter total encoder pulses for front left wheel: "))
total_pulses_RR = int(input("Enter total encoder pulses for rear right wheel: "))
total_pulses_RL = int(input("Enter total encoder pulses for rear left wheel: "))


time_seconds = float(input("Enter measurement time in seconds: "))

#Check measurement time
if time_seconds <= 0:
    print("Error: Measurement time must be greater than zero.")
else: 
    # Engineering Calculations
    revolutions_FR = total_pulses_FR / pulse_per_revolution
    revolutions_FL = total_pulses_FL / pulse_per_revolution
    revolutions_RR = total_pulses_RR / pulse_per_revolution
    revolutions_RL = total_pulses_RL / pulse_per_revolution

    rpm_FR = (revolutions_FR / time_seconds) * 60
    rpm_FL = (revolutions_FL / time_seconds) * 60
    rpm_RR = (revolutions_RR / time_seconds) * 60
    rpm_RL = (revolutions_RL / time_seconds) * 60

    circumference = math.pi * wheel_diameter
    velocity_FR = (rpm_FR * circumference) / 60
    velocity_FL = (rpm_FL * circumference) / 60
    velocity_RR = (rpm_RR * circumference) / 60
    velocity_RL = (rpm_RL * circumference) / 60

    # Display Results
    print("--------------------------------------------------")
    print("Analysis Results:")
    print(f"Total Revolutions for Front Right Wheel: {revolutions_FR:.2f}")
    print(f"Total Revolutions for Front Left Wheel: {revolutions_FL:.2f}")
    print(f"Total Revolutions for Rear Right Wheel: {revolutions_RR:.2f}")
    print(f"Total Revolutions for Rear Left Wheel: {revolutions_RL:.2f}")
    print(f" RPM for Front Right Wheel: {rpm_FR:.2f}")
    print(f" RPM for Front Left Wheel: {rpm_FL:.2f}")
    print(f" RPM for Rear Right Wheel: {rpm_RR:.2f}")
    print(f" RPM for Rear Left Wheel: {rpm_RL:.2f}")
    print(f"Wheel Velocity for Front Right Wheel: {velocity_FR:.2f} m/s")
    print(f"Wheel Velocity for Front Left Wheel: {velocity_FL:.2f} m/s")
    print(f"Wheel Velocity for Rear Right Wheel: {velocity_RR:.2f} m/s")
    print(f"Wheel Velocity for Rear Left Wheel: {velocity_RL:.2f} m/s") 

    print(" Average RPM for all wheels: {:.2f}".format((rpm_FR + rpm_FL + rpm_RR + rpm_RL) / 4))`=[]\[AQ"?
# Physics to Technology - Lesson 1, Part 4
# Independent Four-Wheel RPM Challenge

print("EmpwireBot Four-Wheel RPM Analysis")
print("----------------------------------")

# Experimental data
pulses_per_revolution = 20
time_seconds = 5

front_left = 75
front_right = 65
rear_left = 70
rear_right = 60

# Task 1: Calculate RPM for each wheel
rpm_fl = 0  # TODO
rpm_fr = 0  # TODO
rpm_rl = 0  # TODO
rpm_rr = 0  # TODO

# Task 2: Calculate average RPM
average_rpm = 0  # TODO

# Task 3: Display the results
print("Front Left RPM:", rpm_fl)
print("Front Right RPM:", rpm_fr)
print("Rear Left RPM:", rpm_rl)
print("Rear Right RPM:", rpm_rr)
print("Average RPM:", average_rpm)
]`