# Physics to Technology - Lesson 2 
# Python Functions for Engineering 
# Define a function 
def calculate_rpm(pulses, time_seconds):
    rpm = (pulses / 20) * (60 / time_seconds) 
    return rpm 

# Call the function for four motors 

front_left_rpm = calculate_rpm(75, 5)
front_right_rpm = calculate_rpm(65, 5)
rear_left_rpm = calculate_rpm(70, 5)
rear_right_rpm = calculate_rpm(60, 5)       

# Display the function for motors 
print("EmpwireBoot Motors RPM")
print("------------------------")
print("Front Left Motor RPM:", front_left_rpm)
print("Front Right Motor RPM:", front_right_rpm)
print("Rear Left Motor RPM:", rear_left_rpm)
print("Rear Right Motor RPM:", rear_right_rpm)  
