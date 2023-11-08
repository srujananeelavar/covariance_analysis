import pandas as pd
from Bio import SeqIO
import matplotlib.pyplot as plt
import logomaker as lm

# Step 1: Read the original Excel sheet
df = pd.read_excel('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144ConservationAnalysis.xlsx')

# Filter positions with conservation score >= 0.90
filtered_df = df[df['Conservation Score'] >= 0.90]

# Step 2: Write the selected positions to a new Excel sheet
filtered_df.to_excel('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144HighCons.xlsx', index=False)

# Step 3: Read the new Excel sheet
selected_df = pd.read_excel('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144HighCons.xlsx')

# Extract the selected positions
selected_positions = selected_df['Position'].tolist()

# Step 4: Read the multi-sequence aligned FASTA file
sequences = []
for record in SeqIO.parse('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144FullAllelesRegrouped_aligned.fas', 'fasta'):
    sequence = str(record.seq)
    sequences.append(sequence)

# Extract the amino acids at the selected positions for each sequence
selected_amino_acids = []
for sequence in sequences:
    selected_amino_acids.append(''.join([sequence[pos - 1] for pos in selected_positions]))

# Calculate the number of motif logos to display
num_positions = len(selected_positions)
num_positions_per_row = 10
num_rows = num_positions // num_positions_per_row + 1

# Group the rows
grouped_rows = []
num_groups = num_rows // 5
remaining_rows = num_rows % 5

for group in range(num_groups):
    start_row = group * 5
    end_row = (group + 1) * 5
    grouped_rows.append((start_row, end_row))

if remaining_rows > 0:
    start_row = num_groups * 5
    end_row = start_row + remaining_rows
    grouped_rows.append((start_row, end_row))

# Create subplots for each group
for i, (start_row, end_row) in enumerate(grouped_rows):
    num_group_rows = end_row - start_row

    fig, axs = plt.subplots(num_group_rows, 1, figsize=(10, num_group_rows * 2), squeeze=False)

    for j in range(num_group_rows):
        ax = axs[j, 0]

        start = (start_row + j) * num_positions_per_row
        end = (start_row + j + 1) * num_positions_per_row

        row_positions = selected_positions[start:end]
        row_amino_acids = [acid[start:end] for acid in selected_amino_acids]

        pfm = lm.alignment_to_matrix(row_amino_acids)
        logo = lm.Logo(pfm, color_scheme='charge', ax=ax, vsep=0.2)

        for k, position in enumerate(row_positions):
            logo.ax.text(k, -0.5, str(position), fontsize=20, ha='center', color= 'black')
            

    plt.tight_layout()
    plt.savefig(f'/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/MotifLogos/SHP144MotifHighCons{i+1}.png')
    plt.close(fig)

# Display the motif logos
plt.show()