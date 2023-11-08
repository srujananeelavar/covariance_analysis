# get the fasta sequences of missing IDs
import pandas as pd
from Bio import SeqIO

# Read the Excel file containing fasta file names into a DataFrame
df = pd.read_excel('/Users/srujananeelavar/Documents/Spring2023/Research/covarianceAnalysis/rio120/rio120missing_contigs.xlsx')

# Drop rows with empty values
df.dropna(inplace=True)

# Initialize empty list to store extracted sequences and IDs
seqs = []
ids = []

# Define fasta directory and start/end points
fasta_dir = '/Users/srujananeelavar/Documents/Spring2023/Research/covarianceAnalysis/spn39DB_GoldenSet_7548Genomes_2023/'
start = 10
end = 20

# Loop through each row in the DataFrame
for i, row in df.iterrows():
    # Construct the path to the fasta file
    fasta_file = fasta_dir + row['ID'] + '.fasta'

    # Use SeqIO to parse the fasta file and extract the sequence
    for record in SeqIO.parse(fasta_file, 'fasta'):
        seq = str(record.seq)[start:end+1]
        
        # Append the sequence and ID to the respective lists
        seqs.append(seq)
        ids.append(row['ID'])

# Combine the lists into a new DataFrame
new_df = pd.DataFrame({'ID': ids, 'Sequence': seqs})

# Write the new DataFrame to a new Excel file
new_df.to_excel('/Users/srujananeelavar/Documents/Spring2023/Research/covarianceAnalysis/rio120/rio120extracted_missingSeq.xlsx', index=False)