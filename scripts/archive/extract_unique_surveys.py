import pandas as pd

# Load the CSV file from the data directory
df = pd.read_csv('data/w1w2w3w4w5_indices_weights_jul12_2022.csv')

# Get the unique values from the 'SURVEY' column
unique_surveys = df['SURVEY'].unique()

# Save the unique values to a new CSV file
unique_surveys_df = pd.DataFrame(unique_surveys, columns=['SURVEY'])
unique_surveys_df.to_csv('data/unique_surveys.csv', index=False)

print("Unique survey values have been saved to 'data/unique_surveys.csv'.")