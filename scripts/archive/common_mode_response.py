import pandas as pd

# Load your dataset (update the file path as needed)
df = pd.read_csv("../data/cleaned_data.csv")

# Select relevant columns
ccSolve_columns = ["ccSolve100", "ccSolve50", "ccSolve10", "ccSolve1", "ccSolve0"]

# Compute mode for each ccSolve column
mode_values = {col: df[col].mode()[0] if not df[col].dropna().empty else None for col in ccSolve_columns}

# Print the mode values
print("Most common (mode) response for each ccSolve column:")
for col, mode in mode_values.items():
    print(f"{col}: {mode}")