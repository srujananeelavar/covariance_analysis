# Open the input and output fasta files
with open('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rgg144/rgg144TopHits_aligned.fas', 'r') as infile, open('/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/rgg144/rgg144alleles.fasta', 'w') as outfile:
    # Initialize dictionaries to store sequences and alleles
    sequences = {}
    alleles = {}
    
    # Read the input fasta file and store sequences in the dictionary
    sequence_id = ''
    sequence = ''
    for line in infile:
        if line.startswith('>'):
            if sequence_id:
                sequences[sequence_id] = sequence
                sequence = ''
            sequence_id = line.strip()[1:]
        else:
            sequence += line.strip()
    sequences[sequence_id] = sequence
    
    # Identify alleles and store in a separate dictionary
    for sequence_id, sequence in sequences.items():
        allele = sequence[0:13] # replace with appropriate markers or pattern
        if allele not in alleles.values():
            allele_id = f'{sequence_id}_{allele}' # generate unique allele identifier
            alleles[allele_id] = allele
    
    # Write unique alleles to output fasta file
    for allele_id, allele_seq in alleles.items():
        outfile.write(f'>{allele_id}\n{allele_seq}\n')
