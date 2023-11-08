import os
import pandas as pd

# Specify the directory containing the fasta files
fasta_directory = '/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/spn39DB_GoldenSet_7548Genomes_2023'

# Get a list of fasta files in the directory
fasta_files = [f for f in os.listdir(fasta_directory) if f.endswith('.fasta')]

# Remove the '.fasta' extension from the file names
file_names = [f[:-6] for f in fasta_files]

# Create a DataFrame with the file names
df = pd.DataFrame({'GoldenSet': file_names})

# Define the output Excel file name
output_excel_file = '/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144ExcelForUpset.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(output_excel_file, index=False)

print(f'Excel file "{output_excel_file}" created with the list of fasta file names.')
