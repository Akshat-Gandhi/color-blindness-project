import csv
import random

# Define the header of the CSV file
header = ['ImageNumber', 'Red', 'Green', 'Blue', 'ColorBlindnessType']

# Generate the data for 500 values
data = []
for i in range(1, 501):
    # Generate random RGB values for Protanopia
    protanopia_rgb = [random.randint(0, 255) for _ in range(3)]
    data.append([i] + protanopia_rgb + ['Protanopia'])
    
    # Generate random RGB values for Deuteranopia
    deuteranopia_rgb = [random.randint(0, 255) for _ in range(3)]
    data.append([i] + deuteranopia_rgb + ['Deuteranopia'])
    
    # Generate random RGB values for Tritanopia
    tritanopia_rgb = [random.randint(0, 255) for _ in range(3)]
    data.append([i] + tritanopia_rgb + ['Tritanopia'])

# Write the data to a CSV file
with open('color_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(data)

print("CSV file created successfully.")
