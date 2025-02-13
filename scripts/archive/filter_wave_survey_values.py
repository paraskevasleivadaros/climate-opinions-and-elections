import pandas as pd

# Load the CSV file
df = pd.read_csv("data/duplicate_pids.csv")

# Identify valid sequences (rolling window approach)
df['valid_seq'] = df['WAVE'].rolling(3).apply(lambda x: list(x) == [2,3,4], raw=True)

# Flag rows belonging to valid sequences
df['keep'] = df['valid_seq'].shift(-2).fillna(0).astype(bool) | df['valid_seq'].shift(-1).fillna(0).astype(bool) | df['valid_seq'].fillna(0).astype(bool)

# Filter the rows
filtered_df = df[df['keep']].drop(columns=['valid_seq', 'keep'])

# Save to a new CSV file
filtered_df.to_csv("data/filtered_duplicate_pids.csv", index=False)

print("Filtered data saved to filtered_duplicate_pids.csv")