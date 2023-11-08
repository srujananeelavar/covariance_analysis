#!/bin/bash

# Check if EMBOSS transeq is installed
command -v transeq >/dev/null 2>&1 || { echo >&2 "EMBOSS transeq is not installed. Please install EMBOSS first. Aborting."; exit 1; }

# Input FASTA file name
input_fasta="/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/WithoutSTARFullNTSeq.fasta"

# Output file name for translated protein sequences
output_protein="/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/WithoutSTARFullSeq_translated.fasta"

# Run transeq to translate the FASTA file
transeq -sequence "$input_fasta" -outseq "$output_protein" 

echo "Translation completed. Protein sequences are stored in $output_protein."