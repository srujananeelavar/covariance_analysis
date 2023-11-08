# import os
# import pandas as pd

# # set the directory where your fasta files are located
# fasta_dir = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/spn39DB_GoldenSet_7548Genomes_2023/"

# # get a list of all the fasta file names (without the .fasta extension)
# fasta_files = [os.path.splitext(f)[0] for f in os.listdir(fasta_dir) if f.endswith(".fasta")]

# # create a pandas dataframe with a column for all sequences
# df = pd.DataFrame({"allSequences": fasta_files})

# # specify the full paths to your 5 Excel files
# excel_files = ["/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rgg144/rgg144TopHitsNotUnique.xls", "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rio120/rio120TopHitsNotUnique.xls", "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rio121/rio121TopHitsNotUnique.xls", "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rio122/rio122TopHitsNotUnique.xls", "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rio17/rio17TopHitsNotUnique.xls", "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144AllHits.xls"]

# # loop through each Excel file and extract the fasta file names from the Contig column
# for i, excel_file in enumerate(excel_files):
#     # read the Excel file into a pandas dataframe
#     excel_df = pd.read_excel(excel_file)
    
#     # extract the fasta file names from the Contig column
#     fasta_names = excel_df["Contig"].str.split().str[0].unique()
    
#     # add a column to the dataframe for this Excel file
#     df[os.path.basename(excel_file).split(".")[0]] = df["allSequences"].isin(fasta_names).astype(int)

# # create a new sheet in the same Excel file with the allSequences column
# with pd.ExcelWriter("/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/presenceAbsenceRioSHPRgg.xlsx") as writer:
#     df.to_excel(writer, sheet_name="Sheet1", index=False)

# print("Done!")

import os
import pandas as pd

# Set the directory where your FASTA files are located
fasta_dir = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/spn39DB_GoldenSet_7548Genomes_2023/"

# Get a list of all the FASTA file names (without the .fasta extension)
fasta_files = [os.path.splitext(f)[0] for f in os.listdir(fasta_dir) if f.endswith(".fasta")]

# Create a pandas DataFrame with a column for all sequences
df = pd.DataFrame({"allSequences": fasta_files})

# Specify the full paths to your 6 Excel files
excel_files = [
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rgg144/rgg144TopHitsNotUnique.xls",
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rio120/rio120TopHitsNotUnique.xls",
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rio121/rio121TopHitsNotUnique.xls",
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rio122/rio122TopHitsNotUnique.xls",
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rio17/rio17TopHitsNotUnique.xls",
    "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144TopHitsNotUnique.xls"
]

# Loop through each Excel file and extract the FASTA file names
for i, excel_file in enumerate(excel_files):
    # Read the Excel file into a pandas DataFrame
    excel_df = pd.read_excel(excel_file)
    
    # Extract the FASTA file names based on the file type
    if "rgg144" in excel_file:
        # Extract from the "ID" column for the "rgg144" file
        fasta_names = excel_df["ID"].str.split().str[0].unique()
    else:
        # Extract from the "Contig" column for other files
        fasta_names = excel_df["Contig"].str.split().str[0].unique()
    
    # Add a column to the DataFrame for this Excel file
    df[os.path.basename(excel_file).split(".")[0]] = df["allSequences"].isin(fasta_names).astype(int)

# Create a new sheet in the same Excel file with the allSequences column
with pd.ExcelWriter("/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/presenceAbsenceRioSHPRgg.xlsx") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)

print("Done!")

