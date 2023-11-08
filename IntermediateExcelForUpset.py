# import pandas as pd

# # Read input Excel sheets
# input_sheet_1 = pd.read_excel("/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144AlleleGroups.xlsx")

# # Read all sheets from input_sheet_2
# input_sheet_2 = pd.ExcelFile("/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144TranslatedAll.xlsx")

# # Define the output directory
# output_directory = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/ExcelForUpset/"

# # Iterate through all sheets in input_sheet_2
# for sheet_name in input_sheet_2.sheet_names:
#     # Read the current sheet
#     current_sheet = input_sheet_2.parse(sheet_name)
    
#     # Step 1: Extract the IDs from the current sheet and remove "_1" from the end
#     current_sheet['GoldenSet'] = current_sheet['ID'].str.replace(r'_1$', '', regex=True)
    
#     # Step 2: Merge the two dataframes on Allele and Sequence to find matches
#     merged_df = current_sheet.merge(input_sheet_1, left_on='Sequence', right_on='Allele', how='left')
    
#     # Step 3: Drop rows where there is no match (NaN in 'Group' column)
#     merged_df = merged_df.dropna(subset=['Groups'])
    
#     # Step 4: Create a pivot table to get one column for each Group and mark matches as 1, non-matches as 0
#     pivot_table = merged_df.pivot_table(index='GoldenSet', columns='Groups', values='Allele', aggfunc=lambda x: 1, fill_value=0)
    
#     # Step 5: Reset the index to get 'GoldenSet' as a regular column
#     pivot_table.reset_index(inplace=True)
    
#     # Step 6: Write the output to a new Excel sheet
#     output_path = output_directory + "SHP144ExcelForUpset_" + sheet_name + ".xlsx"
#     pivot_table.to_excel(output_path, index=False)

import os
import pandas as pd

# Step 1: Get the list of fasta file names without the ".fasta" extension
fasta_directory = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/spn39DB_GoldenSet_7548Genomes_2023"  # Update with the path to your fasta files directory
fasta_file_names = [os.path.splitext(file)[0] for file in os.listdir(fasta_directory) if file.endswith(".fasta")]

# Define the output directory
output_directory = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/ExcelForUpset/"

# Read input_sheet_1
input_sheet_1 = pd.read_excel("/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144AlleleGroups.xlsx")

# Read all sheets from input_sheet_2
input_sheet_2 = pd.ExcelFile("/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144TranslatedAll.xlsx")

# Iterate through all sheets in input_sheet_2
for sheet_name in input_sheet_2.sheet_names:
    # Read the current sheet
    current_sheet = input_sheet_2.parse(sheet_name)
    
    # Step 1: Extract the IDs from the current sheet and remove "_1" from the end
    current_sheet['GoldenSet'] = current_sheet['ID'].str.replace(r'_1$', '', regex=True)
    
    # Step 2: Merge the two dataframes on Allele and Sequence to find matches
    merged_df = current_sheet.merge(input_sheet_1, left_on='Sequence', right_on='Allele', how='left')
    
    # Step 3: Drop rows where there is no match (NaN in 'Group' column)
    merged_df = merged_df.dropna(subset=['Groups'])
    
    # Step 4: Create a pivot table to get one column for each Group and mark matches as 1, non-matches as 0
    pivot_table = merged_df.pivot_table(index='GoldenSet', columns='Groups', values='Allele', aggfunc=lambda x: 1, fill_value=0)
    
    # Step 5: Reset the index to get 'GoldenSet' as a regular column
    pivot_table.reset_index(inplace=True)
    
    # Step 6: Write the output to a new Excel sheet
    output_path = output_directory + "SHP144ExcelForUpset_" + sheet_name + ".xlsx"
    pivot_table.to_excel(output_path, index=False)
    
    # Step 7: Compare and add missing fasta file names with 0 in corresponding columns
    missing_fasta_names = set(fasta_file_names) - set(pivot_table['GoldenSet'])
    missing_data = pd.DataFrame({'GoldenSet': list(missing_fasta_names)})
    for group in pivot_table.columns[1:]:
        missing_data[group] = 0
    
    pivot_table = pd.concat([pivot_table, missing_data], ignore_index=True)
    
    # Step 8: Write the updated pivot table to the same output Excel sheet
    pivot_table.to_excel(output_path, index=False)