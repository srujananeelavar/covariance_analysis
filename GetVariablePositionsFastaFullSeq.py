import pandas as pd
from Bio import SeqIO

# Read the Excel file and create FASTA sequences
df = pd.read_excel('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144Sig1PercentAlleleCounts.xlsx')

# Moving the 6th entry to the end
entry_to_move = df.iloc[5].copy()
df = df.drop(index=5)
df = df.append(entry_to_move, ignore_index=True)

# Renumbering the IDs
fasta_sequences = []
for i, row in df.iterrows():
    allele = row['Alleles']
    frequency = row['Counts']
    sequence = f">{i + 1} ({frequency})\n{allele}"
    fasta_sequences.append(sequence)

# Write the FASTA sequences to a file
fasta_file = '/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144AlleleVarIntermediate.fasta'
with open(fasta_file, 'w') as file:
    file.write('\n'.join(fasta_sequences))