from Bio import SeqIO
import pandas as pd

def truncate_sequence(sequence, length):
    return sequence[:length]

def fasta_to_excel(input_file, output_file, sequence_length=289):
    records = SeqIO.parse(input_file, "fasta")

    data = {
        "ID": [],
        "Sequence": []
    }

    for record in records:
        sequence_id = record.id
        sequence = str(record.seq)
        truncated_sequence = truncate_sequence(sequence, sequence_length)
        data["ID"].append(sequence_id)
        data["Sequence"].append(truncated_sequence)

    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    input_fasta_file = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/peg_130/SHP144Allele7_8NT5kDS_translated.fasta"  
    output_excel_file = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/peg_130/SHP144Allele7_8NT5kDS_translated.xlsx"  

    fasta_to_excel(input_fasta_file, output_excel_file)
