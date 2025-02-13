import pandas as pd

# Load the initial CSV file
initial_df = pd.read_csv('data/respondents_w2_w3_w4.csv', low_memory=False)

# Load the unique PIDs CSV file
unique_pids_df = pd.read_csv('data/unique_pids.csv')

# Filter the initial dataframe to keep only the rows with PIDs in the unique PIDs list
filtered_df = initial_df[initial_df['PID'].isin(unique_pids_df['PID'])]

# Convert the 'WAVE' column to strings
filtered_df['WAVE'] = filtered_df['WAVE'].astype(str)

# Filter the dataframe to include only rows with Wave 3
wave3_df = filtered_df[filtered_df['WAVE'].str.contains('3', na=False)]

# Save the filtered dataframe to a new CSV file
wave3_df.to_csv('data/respondents_wave3.csv', index=False)

print("Filtered respondents who participated in Wave 3 have been saved to 'data/respondents_wave3.csv'.")