import pandas as pd
from Bio import SeqIO

# Read the positions from the Excel file
positions_file = '/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144LowCons.xlsx'
positions_df = pd.read_excel(positions_file)
positions_list = positions_df['Position'].tolist()
print(positions_list)

# Read the multi-sequence FASTA file
aligned_fasta_file = '/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144AlleleVarIntermediate_aligned.fas'
sequences = SeqIO.parse(aligned_fasta_file, 'fasta')

# Process each sequence and create modified sequences
modified_sequences = []
for sequence in sequences:
    seq_id = sequence.id.split()[0]
    description = sequence.description.split()[1:]
    modified_seq = ''.join([sequence.seq[pos-1] for pos in positions_list if 1 <= pos <= len(sequence.seq)])
    modified_header = f'>{seq_id} {" ".join(description)}'
    modified_sequence = f'{modified_header}\n{modified_seq}\n'
    modified_sequences.append(modified_sequence)

# Write modified sequences to a new FASTA file
output_fasta = '/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144AllelesAtVarPos.fasta'
with open(output_fasta, 'w') as output_file:
    output_file.writelines(modified_sequences)
