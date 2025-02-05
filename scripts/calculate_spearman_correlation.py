import pandas as pd

# Load the cleaned CSV file from the data directory
df = pd.read_csv('data/cleaned_data.csv')

# Select the specified columns
variables = ['ccComp0', 'ccSolve0', 'cc_pol_tax', 'cc_pol_car', 'cc4_world', 'cc4_wealthUS', 'cc4_poorUS', 'cc4_comm']
df_selected = df[variables]

# Calculate the Spearman correlation matrix
correlation_matrix = df_selected.corr(method='spearman')

# Save the correlation matrix to a CSV file
correlation_matrix.to_csv('results/spearman_correlation_matrix.csv')

print("Spearman correlation matrix has been calculated and saved to 'results/spearman_correlation_matrix.csv'.")