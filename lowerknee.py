import math
import pandas as pd

import time

# Constants
gravity = 9.81  # Gravitational constant in m/s^2
angle_offset = 90  # Angle offset due to sensor placement

# Loop to update the angle in real-time
while True:
    # Read the values from the Excel file
    df = pd.read_excel(r'C:\Users\gopal\OneDrive\Desktop\main\code\sensordata.xlsx', sheet_name='sheet1')
    for index, row in df.iterrows():
        accel_x = row['ax']
        accel_y = row['ay']
        accel_z = row['az']
        
        # Calculate the angle
        angle_radians = math.atan2(accel_x, math.sqrt(accel_y**2 + accel_z**2))
        angle_degrees = math.degrees(angle_radians) + angle_offset
        lower_knee_angle = 180 - angle_degrees
    
        # Print the result
        #print("Lower knee angle:", lower_knee_angle)
    
        # Wait for a short period before updating again
        #time.sleep(0.1)

        print(f"Lower knee angle {index+1}: {lower_knee_angle:.4f} degrees", )

        
