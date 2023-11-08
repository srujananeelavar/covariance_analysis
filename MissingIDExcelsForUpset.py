import os
import pandas as pd

# Directory path for fasta files
fasta_directory = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/spn39DB_GoldenSet_7548Genomes_2023"

# List all the file names without the .fasta extension in the directory
file_list = [os.path.splitext(file)[0] for file in os.listdir(fasta_directory) if file.endswith(".fasta")]

# Replace these with the actual paths to your Excel files
excel_files = [
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHp144/SHP144NT/BS72/SHP144ExcelForUpset_BS72.xlsx",
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHp144/SHP144NT/108700/SHP144ExcelForUpset_108700.xlsx",
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHp144/SHP144NT/D39/SHP144ExcelForUpset_D39.xlsx",
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHp144/SHP144NT/TIGR4/SHP144ExcelForUpset_TIGR4.xlsx",
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHp144/SHP144NT/4595/SHP144ExcelForUpset_4595.xlsx",
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/Rgg144_D39/Rgg144NT/Rgg144ExcelForUpset.xlsx"
]

# Loop through each Excel file
for excel_file in excel_files:
    df = pd.read_excel(excel_file)
    golden_set_column = "GoldenSet"
    
    # Replace NaN values in the GoldenSet column with an empty string
    df[golden_set_column].fillna('', inplace=True)
    
    # Create a set of all entries in the GoldenSet column to make the comparison faster
    existing_entries = set(df[golden_set_column].dropna())
    
    # Filter out the entries from the file_list that don't appear in the GoldenSet column
    missing_entries = [entry for entry in file_list if entry not in existing_entries]
    
    # Append the missing entries to the end of the GoldenSet column
    missing_entries_data = pd.DataFrame({golden_set_column: missing_entries})
    df = df.append(missing_entries_data, ignore_index=True)
    
    # Replace empty strings in the GoldenSet column with 0
    df[golden_set_column].replace('', 0, inplace=True)
    
    # Save the modified DataFrame back to the Excel file
    df.to_excel(excel_file, index=False)
