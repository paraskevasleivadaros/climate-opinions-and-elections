import pandas as pd

# Load the CSV file from the data directory
df = pd.read_csv('data/w1w2w3w4w5_indices_weights_jul12_2022.csv')

# Sort the dataframe by the 'SURVEY' column
df_sorted = df.sort_values(by='SURVEY')

# Save the sorted dataframe to a new CSV file
df_sorted.to_csv('data/sorted_by_survey.csv', index=False)

print("Data has been sorted by 'SURVEY' and saved to 'data/sorted_by_survey.csv'.")