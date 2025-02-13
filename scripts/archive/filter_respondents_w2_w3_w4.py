import pandas as pd

# Load the CSV file from the data directory
df = pd.read_csv('data/w1w2w3w4w5_indices_weights_jul12_2022.csv')

# Define the survey values that include waves 2, 3, and 4
survey_values = ['W4REPw3w2', 'W4REPw3w2w1', 'W5REPw4w3w2', 'W5REPw4w3w2w1']

# Filter the dataframe based on the survey values
filtered_df = df[df['SURVEY'].isin(survey_values)]

# Save the filtered data to a new CSV file
filtered_df.to_csv('data/respondents_w2_w3_w4.csv', index=False)

print("Filtered respondents who participated in waves 2, 3, and 4 have been saved to 'data/respondents_w2_w3_w4.csv'.")