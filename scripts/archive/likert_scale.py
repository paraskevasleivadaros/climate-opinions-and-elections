import pandas as pd

# Load the CSV file from the data directory
df = pd.read_csv('data/filtered_duplicate_pids.csv')

# Some variables use a five-point Likert scale (1 to 5), while others use a four-point scale (1 to 4). 
# Since some scales are missing a neutral category (like 3), we need to standardize them.
# I chose to rescale the 1-4 scale to match the 1-5 scaleby applying a linear transformation:
# 1 (Not at all)         → 1
# 2 (Only a little)      → 2.33
# 3 (A moderate amount)  → 3.67
# 4 (A great deal)       → 5
mapping = {1: 1, 2: 2.33, 3: 3.67, 4: 5}

# List of variables to be mapped
variables_to_map = ['cc4_world', 'cc4_wealthUS', 'cc4_poorUS', 'cc4_comm', 'cc4_famheal', 'cc4_famecon']

# Apply the mapping to the specified variables
for var in variables_to_map:
    df[var] = df[var].map(mapping)

# Save the cleaned data to a new CSV file
df.to_csv('data/likert_scale.csv', index=False)

print("Data has been standardized and saved to 'data/likert_scale.csv'.")