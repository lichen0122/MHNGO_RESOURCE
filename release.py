import pickle
import json
import os
from datetime import datetime
import random

# Generate today's date in the format year-month-day
today_date = datetime.now().strftime("%Y-%m-%d")

# Generate a random serial number
serial_number = random.randint(1000, 9999)

# Create the dictionary with 'version' as key and date plus serial number as value
version_info = {"version": f"{today_date}-{serial_number}"}

# Define file paths
pickle_file_path = 'MHNGO/MHNGO_RUNTIME.dll'  # Path for pickle file in MHNGO directory
json_file_path = 'MHNGO_VERSION.json'         # Path for json file in the current directory

# Create MHNGO directory if it doesn't exist
mhngo_dir = '/mnt/data/MHNGO'
os.makedirs(mhngo_dir, exist_ok=True)

# Save the dictionary as a pickle file
with open(pickle_file_path, 'wb') as pickle_file:
    pickle.dump(version_info, pickle_file)

# Save the dictionary as a json file
with open(json_file_path, 'w') as json_file:
    json.dump(version_info, json_file)
