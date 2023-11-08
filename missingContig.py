# Find the negative dataset without the rios/rgg

import os
import pandas as pd
from Bio import SeqIO

# Read the Excel file and extract the ID column
df = pd.read_excel('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rgg144/rgg144TopHitsNotUnique.xls')
df['ID'] = df['ID'].str.split().str[0]
# print(df['ID'])

# Get the set of IDs from the fasta file names
fasta_folder_path = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rgg144/goldenSet_blast"

# Get a list of the IDs of the fasta files in the folder
fasta_ids = [filename.split(".")[0] for filename in os.listdir(fasta_folder_path)]
# print(fasta_ids)

# Find the missing IDs
missing_ids = set(fasta_ids).difference(set(df['ID']))
# print(missing_ids)

# Create a new Excel file with the missing IDs
new_df = pd.DataFrame(list(missing_ids), columns=['ID'])
new_df.to_excel('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rgg144/rgg144MissingContigs.xlsx', index=False)




# import pandas as pd

# # Read excel sheet#1 and #2
# df1 = pd.read_excel("/Users/srujananeelavar/Documents/Spring2023/Research/covarianceAnalysis/rgg144/rgg144AllHits.xls")
# df2 = pd.read_excel("/Users/srujananeelavar/Documents/Spring2023/Research/covarianceAnalysis/rgg144/rgg144tophits.xls")

# # Extract ID from Contig column in df2
# df2['ID'] = df2['Contig'].str.split(' ').str[0]

# # Use the merge function to join df1 and df2 on ID column
# merged_df = pd.merge(df1, df2['ID'], on='ID', how='outer', indicator=True)

# # Filter out rows that exist in both df1 and df2
# new_df = merged_df[merged_df['_merge'] == 'left_only']

# # Drop the '_merge' column
# new_df = new_df.drop('_merge', axis=1)

# # Write the result to a new Excel sheet
# new_df.to_excel('/Users/srujananeelavar/Documents/Spring2023/Research/covarianceAnalysis/rgg144/rgg144missing_contigs.xlsx', index=False)