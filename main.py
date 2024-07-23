data_file = "data.txt"

# Read the data file
try:
    with open(data_file, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error: The file '{data_file}' was not found.")
    exit()

# Parse the header
header = lines[0].strip().split(',')

# Initialize data list
data = []
for line in lines[1:]:
    values = line.strip().split(',')
    data.append({
        'Red': int(values[0]),
        'Yellow': int(values[1]),
        'Green': int(values[2]),
        'TimeActive': int(values[3]),
        'Time': values[4]
    })

# Task 1: Count occurrences of each light
red_count = sum(1 for entry in data if entry['Red'])
yellow_count = sum(1 for entry in data if entry['Yellow'])
green_count = sum(1 for entry in data if entry['Green'])

print(f"Red: {red_count}, Yellow: {yellow_count}, Green: {green_count}")

# Task 2: Calculate total time each light was active
red_time = sum(entry['TimeActive'] for entry in data if entry['Red'])
yellow_time = sum(entry['TimeActive'] for entry in data if entry['Yellow'])
green_time = sum(entry['TimeActive'] for entry in data if entry['Green'])

print(f"Red: {red_time} seconds, Yellow: {yellow_time} seconds, Green: {green_time} seconds")

# Task 3: Find all times when Green was active
green_times = [entry['Time'] for entry in data if entry['Green']]
print(f"Times when Green was active: {green_times}")

# Task 4: Find number of complete cycles Red-Yellow-Green-Yellow-Red
complete_cycles = 0
i = 0
n = len(data)

while i < n - 4:
    if data[i]['Red'] and data[i+1]['Yellow'] and data[i+2]['Green'] and data[i+3]['Yellow'] and data[i+4]['Red']:
        complete_cycles += 1
        i += 5
    else:
        i += 1

print(f"Number of complete cycles: {complete_cycles}")

# Task 5: Find number of lines with mistakes
mistakes = 0

for entry in data:
    active_lights = entry['Red'] + entry['Yellow'] + entry['Green']
    if active_lights != 1:
        mistakes += 1

print(f"Number of lines with mistakes: {mistakes}")