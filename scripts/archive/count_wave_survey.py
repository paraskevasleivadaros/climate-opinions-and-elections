import pandas as pd

# Load the CSV file
df = pd.read_csv('data/w1w2w3w4w5_indices_weights_jul12_2022.csv', low_memory=False)

# Count the number of rows for each WAVE
wave_counts = df['WAVE'].value_counts().reset_index()
wave_counts.columns = ['WAVE', 'COUNT']

# Count the number of rows for each SURVEY
survey_counts = df['SURVEY'].value_counts().reset_index()
survey_counts.columns = ['SURVEY', 'COUNT']

# Save the results to CSV files
wave_counts.to_csv('data/wave_counts.csv', index=False)
survey_counts.to_csv('data/survey_counts.csv', index=False)

print("Counts have been saved to 'data/wave_counts.csv' and 'data/survey_counts.csv'.")