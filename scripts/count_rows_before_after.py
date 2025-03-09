import pandas as pd

# Load the CSV file from the data directory
df = pd.read_csv('data/cleaned_data.csv')

# Convert the 'RecordedDate' column to datetime format
df['RecordedDate'] = pd.to_datetime(df['RecordedDate'])

# Define the cutoff date
cutoff_date = pd.to_datetime('2020-11-07')

# Count the number of rows before and after the cutoff date
rows_before = df[df['RecordedDate'] < cutoff_date].shape[0]
rows_after = df[df['RecordedDate'] >= cutoff_date].shape[0]

# Print the results
print(f"Number of rows before {cutoff_date}: {rows_before}")
print(f"Number of rows on or after {cutoff_date}: {rows_after}")

# Save the results to a file
with open('data/rows_count_before_after.md', 'w') as f:
    f.write("# Rows Count Before and After 2020-11-07\n\n")
    f.write(f"Number of rows before {cutoff_date}: {rows_before}\n")
    f.write(f"Number of rows on or after {cutoff_date}: {rows_after}\n")

print("Counts have been saved to 'data/rows_count_before_after.md'.")