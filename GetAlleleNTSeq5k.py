import pandas as pd
from Bio import SeqIO

def remove_trailing_number(id_str):
    # Function to remove the trailing '_1' from the ID
    return id_str.rsplit('_', 1)[0]

def main():
    # Step 1: Read the Excel file
    excel_file = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/TIGR4/SHP144TopHits_translated_TIGR4.xlsx"
    search_sequence = "MKKQVLTLLTIVAEIIIILPFLTNR*"

    df = pd.read_excel(excel_file)
    
    # Filter IDs based on the search sequence
    matched_ids = df[df["Sequence"] == search_sequence]["ID"].tolist()

    # Step 2: Remove the trailing "_1" from the IDs
    cleaned_ids = [remove_trailing_number(id_str) for id_str in matched_ids]

    # Step 3: Read the multi-sequence FASTA file
    
    fasta_file = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/peg_130/peg130_5kDS.fasta"
    output_fasta_file = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/peg_130/SHP144Allele7_8NT5kDS.fasta"
    
    with open(output_fasta_file, "w") as output_handle:
        for record in SeqIO.parse(fasta_file, "fasta"):
            header = record.id

            # Step 4: Search for matching IDs in the headers
            for cleaned_id in cleaned_ids:
                if cleaned_id in header:
                    # Write matching headers and sequences to the output FASTA file
                    SeqIO.write(record, output_handle, "fasta")
                    break

if __name__ == "__main__":
    main()