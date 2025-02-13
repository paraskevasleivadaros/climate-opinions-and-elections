import pandas as pd

# Load the CSV file from the data directory
df = pd.read_csv('data/w1w2w3w4w5_indices_weights_jul12_2022.csv')

# Group by 'ResponseId' and count the number of unique 'WAVE' entries for each 'ResponseId'
response_wave_counts = df.groupby('ResponseId')['WAVE'].nunique()

# Identify 'ResponseId' entries that appear in more than one wave
duplicate_responses = response_wave_counts[response_wave_counts > 1]

# Count the number of such 'ResponseId' entries
duplicate_response_count = duplicate_responses.shape[0]

# Print the result
print(f"Number of unique ResponseId entries that appear in more than one wave: {duplicate_response_count}")

# Save the result to a file
with open('results/duplicate_responses_count.md', 'w') as f:
    f.write("# Duplicate Responses Count\n\n")
    f.write(f"Number of unique ResponseId entries that appear in more than one wave: {duplicate_response_count}\n")

print("Duplicate responses count has been saved to 'results/duplicate_responses_count.md'.")