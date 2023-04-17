import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def calculatePushOffAngle(ax, ay, az):
    # Convert accelerometer readings to m/s^2
    ax = ax * 9.81
    ay = ay * 9.81
    az = az * 9.81
    
    # Calculate push off angle
    pushOffAngle = math.atan2(ax, math.sqrt(ay**2 + az**2))
    
    # Convert to degrees and return
    return math.degrees(pushOffAngle)

# Read Excel sheets into pandas dataframes
pushoff_df = pd.read_excel(r'C:\Users\gopal\OneDrive\Desktop\finalproj-main\cleaned_pushoff1.xlsx',sheet_name='Sheet1')

pushOffAngles = []
for index, row in pushoff_df.iterrows():
    ax = row['ax']
    ay = row['ay']
    az = row['az']

    # Calculate push off angle for the row
    pushOffAngle = calculatePushOffAngle(ax, ay, az)
    pushOffAngles.append(pushOffAngle)

# Create evenly spaced x-axis values for a time period of 3 seconds
x = np.linspace(0, 6, len(pushOffAngles))

# Create y-axis values from pushOffAngles list
y = pushOffAngles

# Plot the graph
plt.plot(x, y)

# Set the title and axis labels
plt.title('Push Off Angles ')
plt.xlabel('Time (seconds)')
plt.ylabel('Push Off Angle (degrees)')

# Show the plot
plt.show()
