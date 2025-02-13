import pandas as pd

# Load the unique surveys CSV file from the data directory
df = pd.read_csv('data/unique_surveys.csv')

# Sort the dataframe by the 'SURVEY' column
df_sorted = df.sort_values(by='SURVEY')

# Save the sorted dataframe to a new CSV file
df_sorted.to_csv('data/sorted_unique_surveys.csv', index=False)

print("Unique survey values have been sorted and saved to 'data/sorted_unique_surveys.csv'.")