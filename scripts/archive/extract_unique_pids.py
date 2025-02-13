import pandas as pd

# Load the filtered CSV file from the data directory
df = pd.read_csv('data/respondents_w2_w3_w4.csv')

# Get the unique values from the 'PID' column
unique_pids = df['PID'].unique()

# Save the unique values to a new CSV file
unique_pids_df = pd.DataFrame(unique_pids, columns=['PID'])
unique_pids_df.to_csv('data/unique_pids.csv', index=False)

print("Unique PID values have been saved to 'data/unique_pids.csv'.")