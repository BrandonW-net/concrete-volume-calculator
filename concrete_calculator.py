# This script calculates the concrete volume for a single wall

# Step:1 Define wall dimensions
# Using hard coded values for test purposes
# Dimensions are in feet, wall thickness measured in feet
wallLenghtFT = 40
wallHeightFt = 8
wallThicknessInches = 10

# Step 2: Convert all measured units to feet
# 12 inches are in 1 foot, divide wall thickness by 12
wallThicknessFt = wallThicknessInches / 12

# Step 3: Calculate the volume in cubic feet
# The formula is; Volume = Lenght * Height * Thickness
volumeCubicFeet = wallLenghtFT * wallHeightFt * wallThicknessFt

# Step 4: Convert the volume to cubic yards 
# There are 27 cubic feet in 1 cubic yard
volumeCubicYard = volumeCubicFeet / 27

# Step 5: Print the results to the console
print(f"Your wall measurements are: {wallLenghtFT}ft x {wallHeightFt}ft x {wallThicknessInches}in")
print(f"The volume of concrete is: {volumeCubicFeet:.2f} cubic feet")
print(f"You will need to order: {volumeCubicYard:.2f} cubic yards of concrete")
