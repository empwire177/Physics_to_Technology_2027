
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
rpm_fl = (front_left / pulses_per_revolution) * (60 / time_seconds)   # TODO
rpm_fr = (front_right / pulses_per_revolution) * (60 / time_seconds)  # TODO
rpm_rl = (rear_left / pulses_per_revolution) * (60 / time_seconds)    # TODO
rpm_rr = (rear_right / pulses_per_revolution) * (60 / time_seconds)   # TODO

# Task 2: Calculate average RPM
average_rpm = (rpm_fl + rpm_fr + rpm_rl + rpm_rr) / 4     # TODO

# Task 3: Display the results
print("Front Left RPM:", rpm_fl)
print("Front Right RPM:", rpm_fr)
print("Rear Left RPM:", rpm_rl)
print("Rear Right RPM:", rpm_rr)
print("Average RPM:", average_rpm)



fastest_rpm = max(rpm_fl, rpm_fr, rpm_rl, rpm_rr )
slowest_rpm = min(rpm_fl, rpm_fr, rpm_rl, rpm_rr )
rpm_difference = fastest_rpm - slowest_rpm 

print("Fastest RPM:", fastest_rpm)
print("Slowest RPM:", slowest_rpm)
print("RPM Difference:", rpm_difference)


if rpm_difference > 5:
    print("Warning: wheel speed imbalance detected!")
else: 
    print("Wheel speeds are within the exercise tolerance" )
    