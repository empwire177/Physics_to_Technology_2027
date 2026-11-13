# Physics to Technology - Lesson 2 
# Python Functions parameters and Return Values  
# Define a function 
def calculate_rpm(pulses, time_seconds, ppr):
    rpm = (pulses / ppr) * (60 / time_seconds) 
    return rpm 

# expeeriment 1 
rpm_1 = calculate_rpm(80, 4, 20)

# expeeriment 2 
rpm_2 = calculate_rpm(80, 4, 40)

# expeeriment 3
rpm_3 = calculate_rpm(120, 6, 20)

# Display the results
print("Experiment 1 RPM:", rpm_1)
print("Experiment 2 RPM:", rpm_2)
print("Experiment 3 RPM:", rpm_3) 

