import pandas as pd

# Load the initial CSV file
initial_df = pd.read_csv('data/respondents_w2_w3_w4.csv')

# Load the unique PIDs CSV file
unique_pids_df = pd.read_csv('data/unique_pids.csv')

# Filter the initial dataframe to keep only the rows with PIDs in the unique PIDs list
filtered_df = initial_df[initial_df['PID'].isin(unique_pids_df['PID'])]

# Save the filtered dataframe to a new CSV file
filtered_df.to_csv('data/respondents_filtered.csv', index=False)

print("Filtered rows have been saved to 'data/respondents_filtered.csv'.")