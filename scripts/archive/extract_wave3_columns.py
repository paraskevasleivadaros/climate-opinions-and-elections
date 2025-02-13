import pandas as pd

# Load the CSV file
df = pd.read_csv('data/w1w2w3w4w5_indices_weights_jul12_2022.csv')

# Filter the dataframe to include only rows where WAVE is 3
wave3_df = df[df['WAVE'] == 3]

# Select the specified columns in the desired order
selected_columns_wave3 = wave3_df[['RecordedDate', 'ResponseId', 'WAVE', 'SURVEY']]

# Save the selected columns to a new CSV file
selected_columns_wave3.to_csv('data/selected_columns_wave3.csv', index=False)

print("Selected columns for wave 3 have been saved to 'data/selected_columns_wave3.csv'")