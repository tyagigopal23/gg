import math
import pandas as pd
import time
from sklearn.linear_model import LinearRegression

# Constants
gravity = 9.81  # Gravitational constant in m/s^2
angle_offset = 90  # Angle offset due to sensor placement

# Loop to update the angle in real-time
while True:
    # Read the values from the Excel file
    df = pd.read_excel(r'C:\Users\gopal\OneDrive\Desktop\main\code\sensordata.xlsx', sheet_name='sheet1')
    
    # Drop rows with missing values
    # df.dropna(inplace=True)

    # Check if df is empty
    if df.empty:
        print("DataFrame is empty after dropping rows with missing values.")
        time.sleep(1)  # Wait for 1 second before reading the Excel file again
        continue  # Go to the next iteration of the loop

    # Calculate the angle
    df['angle_radians'] = df.apply(lambda row: math.atan2(row['ax'], math.sqrt(row['ay']**2 + row['az']**2)), axis=1)
    df['angle_degrees'] = df['angle_radians'].apply(math.degrees) + angle_offset
    df['lower_knee_angle'] = 180 - df['angle_degrees']
    
    # Split the data into input and output variables
    X = df[['ax', 'ay', 'az']].values
    y = df['lower_knee_angle'].values
    
    # Train a linear regression model
    reg = LinearRegression()
    reg.fit(X, y)
    
    # Print the coefficients and intercept
    print(f"Coefficients: {reg.coef_}")
    print(f"Intercept: {reg.intercept_}")
    
    time.sleep(1)  # Wait for 1 second before reading the Excel file again
