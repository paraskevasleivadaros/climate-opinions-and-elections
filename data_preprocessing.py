import pandas as pd
import numpy as np
import os

# Load the CSV file
df = pd.read_csv('data.csv')

# Inspect the first few rows
print(df.head())

# Check basic information about the dataset
print(df.info())