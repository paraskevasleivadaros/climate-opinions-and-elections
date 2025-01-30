import pandas as pd

# Load the CSV file from the data directory
df = pd.read_csv('data/sorted_selected_columns.csv')

# Convert the 'RecordedDate' column to datetime format
df['RecordedDate'] = pd.to_datetime(df['RecordedDate'])

# Group by 'WAVE' and calculate the min and max 'RecordedDate' for each group
wave_date_ranges = df.groupby('WAVE')['RecordedDate'].agg(['min', 'max'])

# Write the date ranges to a Markdown file
with open('results/wave_date_ranges.md', 'w') as f:
    f.write("# Date Ranges for Each Wave\n\n")
    for wave, row in wave_date_ranges.iterrows():
        f.write(f"## Wave {wave}\n")
        f.write(f"- **Oldest recording:** {row['min']}\n")
        f.write(f"- **Latest recording:** {row['max']}\n")
        f.write("\n")

print("Date ranges for each wave have been calculated and written to 'results/wave_date_ranges.md'.")