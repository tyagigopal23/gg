import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


def calculateTrunkAngle(ax, ay, az):
    roll = math.atan2(ay, az)
    pitch = math.atan2(-ax, math.sqrt(ay * ay + az * az))
    trunk_angle = math.sqrt(roll * roll + pitch * pitch)
    return math.degrees(trunk_angle)

# Read Excel sheets into pandas dataframes
trunk_df = pd.read_excel(r"C:\Users\gopal\OneDrive\Desktop\finalproj-main\cleaned_trunk.xlsx",sheet_name='Sheet1')
trunk_angle = []
for index, row in trunk_df.iterrows():
    ax = row['ax']
    ay = row['ay']
    az = row['az']

    # Calculate push off angle for the row
    angle = calculateTrunkAngle(ax, ay, az)
    trunk_angle.append(angle)

# Create evenly spaced x-axis values for a time period of 3 seconds
x = np.linspace(0, 6, len(trunk_angle))

# Create y-axis values from pushOffAngles list
y = trunk_angle

# Plot the graph
plt.plot(x, y)

# Set the title and axis labels
plt.title('Trunk Angle (Actual)')
plt.xlabel('Time (seconds)')
plt.ylabel('Push Off Angle (degrees)')

# Show the plot
plt.show()

