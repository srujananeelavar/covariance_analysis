import pandas as pd

# Given fasta file path and output Excel file path
fasta_file = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144FullAllelesRegrouped.fasta"
output_file = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144AlleleGroups.xlsx"

# Read fasta data from the file and convert it into a dictionary with IDs and sequences
def read_fasta_file(file_path):
    fasta_dict = {}
    with open(file_path, 'r') as file:
        current_id = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_id = int(line.split()[1])
                fasta_dict[current_id] = ""
            else:
                fasta_dict[current_id] += line  # Keep the sequence as it is without any edits
    return fasta_dict

# Given groups data
groups_data = {
    "S1": [3, 9, 4, 7, 1, 10, 8],
    "S2": [6, 5, 2, 11]
}

# Generate the DataFrame for the Excel output
def generate_output_data(groups_data, fasta_dict):
    output_data = []
    for group, ids in groups_data.items():
        for identifier in ids:
            group_id = f"{group}-{identifier}"
            allele = fasta_dict.get(identifier, "")
            output_data.append({"Groups": group_id, "Allele": allele})
    return output_data

# Read fasta data from the file
fasta_dict = read_fasta_file(fasta_file)

# Generate the output data for the Excel file
output_data = generate_output_data(groups_data, fasta_dict)

# Create a pandas DataFrame
df = pd.DataFrame(output_data)

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)

print(f"Output Excel file '{output_file}' generated successfully!")
