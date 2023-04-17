import math
import pandas as pd

# Function to calculate trunk angle
def calculateTrunkAngle(ax, ay, az):
  roll = math.atan2(ay, az)
  pitch = math.atan2(-ax, math.sqrt(ay * ay + az * az))
  angle = math.sqrt(roll * roll + pitch * pitch)
  return angle

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('cleaned_trunk.xlsx')  # Replace with the actual filename and sheet name

# Extract the ax, ay, and az values
ax = df['ax'].values  # Replace with the actual column name
ay = df['ay'].values
az = df['az'].values

# Iterate over the arrays and call the calculateTrunkAngle() function for each set of values
for i in range(len(ax)):
  angle = calculateTrunkAngle(ax[i], ay[i], az[i])
  #print(f"Trunk angle {i+1}: {angle} radians")

  angle_degrees = math.degrees(angle)
  print(f"Trunk angle {i+1}: {angle_degrees} degrees")





