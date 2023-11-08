def reorder_fasta(input_fasta, order_list, output_fasta):
    # Read the input FASTA file and store sequences and headers in a dictionary
    sequences = {}
    current_header = None
    with open(input_fasta, 'r') as infile:
        for line in infile:
            if line.startswith('>'):
                current_header = line.strip()[1:]  # Remove '>'
                sequences[current_header] = ''
            else:
                sequences[current_header] += line.strip()

    # Create a new list to store the reordered sequences
    reordered_sequences = []

    # Reorder the sequences based on the provided list of numbers
    for number in order_list:
        header_to_find = f"{number} ("
        for header, sequence in sequences.items():
            if header.startswith(header_to_find):
                reordered_sequences.append(f">{header}\n{sequence}")
                break  # Move to the next number in the order_list

    # Write the reordered sequences to the output FASTA file
    with open(output_fasta, 'w') as outfile:
        outfile.write('\n'.join(reordered_sequences))


# Example usage
input_fasta_file = '/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144AllelesAtVarPos_aligned.fas'
output_fasta_file = '/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144AllelesVarPosGrouped.fasta'
order_list = [3, 7, 2, 5, 4, 6, 1, 8, 9]

reorder_fasta(input_fasta_file, order_list, output_fasta_file)