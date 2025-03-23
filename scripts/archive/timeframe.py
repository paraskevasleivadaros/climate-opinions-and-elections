import pandas as pd
import os

# Define the absolute path to the CSV file
file_path = os.path.join(os.path.dirname(__file__), '../data/cleaned_data.csv')

# Load the CSV file
data = pd.read_csv(file_path)

# Convert the 'RecordedDate' column to datetime
data['RecordedDate'] = pd.to_datetime(data['RecordedDate'])

# Calculate the earliest and latest recorded dates
earliest_date = data['RecordedDate'].min()
latest_date = data['RecordedDate'].max()

# Save the result in a new file
result = pd.DataFrame({
    'Earliest Recorded Date': [earliest_date],
    'Latest Recorded Date': [latest_date]
})

# Define the absolute path to the result file
result_file_path = os.path.join(os.path.dirname(__file__), '../data/timeframe.md')
result.to_csv(result_file_path, index=False)

print(f"Results saved to {result_file_path}")