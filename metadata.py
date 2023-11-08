import pandas as pd

# Load the first Excel file with column 'ID'
file1 = pd.read_excel('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/VpoD/vp1TopHits.xls')

# Load the second Excel file with column 'sample', 'GPSC', 'MLST', and 'serotype'
file2 = pd.read_excel('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/VpoD/differenceset_serotype.xlsx')

# Merge the two dataframes based on the 'sample' column
merged_data = pd.merge(file1, file2, left_on='ID', right_on='sample', how='inner')

# Select only the required columns in the final output
final_output = merged_data[['sample', 'GPSC', 'MLST', 'serotype']]

# Save the final output to a new Excel file
final_output.to_excel('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/VpoD/x.xlsx', index=False)
