import pandas as pd

# Load the CSV file from the data directory
df = pd.read_csv('data/w1w2w3w4w5_indices_weights_jul12_2022.csv')

# Get the column names
columns = df.columns

# Print the column names to a file
with open('data/column_names.md', 'w') as f:
    f.write("# Column Names\n\n")
    for column in columns:
        f.write(f"- {column}\n")

print("Column names have been saved to 'data/column_names.md'.")