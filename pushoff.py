import pandas as pd
import math

# Function to calculate push off angle
def calculatePushOffAngle(ax, ay, az):
    # Convert accelerometer readings to m/s^2
    ax = ax * 9.81
    ay = ay * 9.81
    az = az * 9.81
    
    # Calculate push off angle
    pushOffAngle = math.atan2(ax, math.sqrt(ay**2 + az**2))
    
    # Convert to degrees and return
    return math.degrees(pushOffAngle)

# Read Excel sheet into a pandas dataframe
df = pd.read_excel(r'C:\Users\gopal\OneDrive\Desktop\main\code\sensordata.xlsx', sheet_name='sheet1')

# Loop through each row in the dataframe and calculate push off angle
for index, row in df.iterrows():
    ax = row['ax']
    ay = row['ay']
    az = row['az']
    
    # Calculate push off angle for the row
    pushOffAngle = calculatePushOffAngle(ax, ay, az)
    
    # Print push off angle for the row
    # print(f"Push off angle {index+1}: {pushOffAngle:.2f} degrees")
    if index == 99:
            print(f"Lower knee angle {index+1}: {lower_knee_angle:.4f} degrees")
            break

    #pushOffAngle_rad = math.radians(pushOffAngle)
    #print(f"Push off angle {index+1}: {pushOffAngle_rad:.2f} radians")
