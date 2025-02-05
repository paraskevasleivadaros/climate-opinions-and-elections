import pandas as pd

# Load the CSV file from the data directory
df = pd.read_csv('data/w1w2w3w4w5_indices_weights_jul12_2022.csv')

# Define the mapping for the specified variables
mapping = {4: 5, 3: 4, 99: 3}

# List of variables to be mapped
variables_to_map = ['cc4_world', 'cc4_wealthUS', 'cc4_poorUS', 'cc4_comm']

# Apply the mapping to the specified variables
for var in variables_to_map:
    df[var] = df[var].map(mapping)

# Save the cleaned data to a new CSV file
df.to_csv('data/cleaned_data.csv', index=False)

print("Data has been cleaned and saved to 'data/cleaned_data.csv'.")