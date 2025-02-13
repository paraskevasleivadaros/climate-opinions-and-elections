import pandas as pd

# Load the CSV file from the data directory
df = pd.read_csv('data/selected_columns.csv')

# Convert the 'RecordedDate' column to datetime format
df['RecordedDate'] = pd.to_datetime(df['RecordedDate'])

# Sort the dataframe by 'RecordedDate' in ascending order
df_sorted = df.sort_values(by='RecordedDate')

# Save the sorted dataframe to a new CSV file in the data directory
df_sorted.to_csv('data/sorted_selected_columns.csv', index=False)

print("Data has been sorted by 'RecordedDate' and saved to 'data/sorted_selected_columns.csv'")