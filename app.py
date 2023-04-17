from flask import Flask, render_template
import pandas as pd
import math
import matplotlib
app = Flask(__name__)

# # Function to calculate push off angle
def calculatePushOffAngle(ax, ay, az):
    # Convert accelerometer readings to m/s^2
    ax = ax * 9.81
    ay = ay * 9.81
    az = az * 9.81
    
    # Calculate push off angle
    pushOffAngle = math.atan2(ax, math.sqrt(ay**2 + az**2))
    
    # Convert to degrees and return
    return math.degrees(-pushOffAngle)

def calculateTrunkAngle(ax, ay, az):
  
  roll = math.atan2(ay, az)
  pitch = math.atan2(-ax, math.sqrt(ay * ay + az * az))
  trunkAngles = math.sqrt(roll * roll + pitch * pitch)
  return math.degrees(trunkAngles)

# Home page
@app.route('/')
def home():
    # Read Excel sheets into pandas dataframes
    pushoff_df = pd.read_excel(r'C:\Users\gopal\OneDrive\Desktop\finalproj-main\cleaned_pushoff1.xlsx',sheet_name='Sheet1')
    lowerknee_df = pd.read_excel(r'C:\Users\gopal\OneDrive\Desktop\finalproj-main\cleaned_pushoff.xlsx',sheet_name='Sheet1')
    upperknee_df = pd.read_excel(r'C:\Users\gopal\OneDrive\Desktop\finalproj-main\cleaned_pushoff.xlsx',sheet_name='Sheet1')
    trunk_df = pd.read_excel(r'C:\Users\gopal\OneDrive\Desktop\finalproj-main\cleaned_trunk.xlsx',sheet_name='Sheet1')

    pushOffAngles = []
    lowerKneeAngles = []
    upperKneeAngles = []
    trunkAngles = []

    # Loop through each row in the dataframes and calculate angles
    for index, row in pushoff_df.iterrows():
        ax = row['ax']
        ay = row['ay']
        az = row['az']

        # Calculate push off angle for the row
        pushOffAngle = calculatePushOffAngle(ax, ay, az)
        pushOffAngles.append(f"Push off angle {index+1}: {pushOffAngle:.4f} degrees")

    for index, row in lowerknee_df.iterrows():
        ax = row['ax']
        ay = row['ay']
        az = row['az']

        # Calculate lower knee angle for the row
        angle_radians = math.atan2(ax, math.sqrt(ay**2 + az**2))
        angle_degrees = math.degrees(angle_radians) + 90
        lower_knee_angle = 180 - angle_degrees
        lowerKneeAngles.append(f"Lower knee angle {index+1}: {lower_knee_angle:.4f} degrees")

    for index, row in upperknee_df.iterrows():
        ax = row['ax']
        ay = row['ay']
        az = row['az']

        # Calculate upper knee angle for the row
        angle_offset = 90 
        angle_radians = math.atan2(ax, math.sqrt(ay**2 + az**2))
        angle_degrees = math.degrees(angle_radians) + angle_offset
        upperKneeAngles.append(f"Upper knee angle {index+1}: {angle_degrees:.4f} degrees")

    for index, row in trunk_df.iterrows():
        ax = row['ax']
        ay = row['ay']
        az = row['az']

        # Calculate trunk angle for the row
        trunk_angle = calculateTrunkAngle(ax, ay, az)
        trunkAngles.append(f"Trunk angle {index+1}: {trunk_angle:.4f} degrees")

    return render_template('index.html', pushOffAngles=pushOffAngles, lowerKneeAngles=lowerKneeAngles, upperKneeAngles=upperKneeAngles, trunkAngles=trunkAngles)

if __name__ == '__main__':
    app.run(debug=True)
