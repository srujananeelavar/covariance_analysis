import pandas as pd

# Read the Excel file
data = pd.read_excel("/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144Sig1PercentAlleleCounts.xlsx") 

# Create and write the FASTA file
with open("/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144Sig1PercentAllele.fasta", "w") as fasta_file:
    for index, row in data.iterrows():
        header = "> {} ({})\n".format(index + 1, row["Counts"])
        sequence = "{}\n".format(row["Alleles"])
        fasta_file.write(header)
        fasta_file.write(sequence)

print("FASTA file has been created successfully.")
