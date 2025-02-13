import pandas as pd

# Load the CSV file
df = pd.read_csv('data/w1w2w3w4w5_indices_weights_jul12_2022.csv')

# Select the specified columns in the desired order
selected_columns = df[['RecordedDate', 'ResponseId', 'WAVE', 'SURVEY']]

# Save the selected columns to a new CSV file
selected_columns.to_csv('data/selected_columns.csv', index=False)

print("Selected columns have been saved to 'data/selected_columns.csv'")