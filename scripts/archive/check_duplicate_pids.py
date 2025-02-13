import pandas as pd

# Load the CSV file
df = pd.read_csv('data/w1w2w3w4w5_indices_weights_jul12_2022.csv', low_memory=False)

# Check for duplicate PIDs
duplicate_pids = df[df.duplicated('PID', keep=False)]

if not duplicate_pids.empty:
    print("There are duplicate PIDs in the dataset.")
    duplicate_pids.to_csv('data/duplicate_pids.csv', index=False)
    print("Duplicate PIDs have been saved to 'data/duplicate_pids.csv'.")
else:
    print("All PIDs are unique.")