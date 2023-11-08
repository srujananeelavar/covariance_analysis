import pandas as pd

# define the path to the input Excel file
input_file = '/Users/srujananeelavar/Documents/Spring2023/Research/covarianceAnalysis/rio122/rio122tophits.xls'

# define the path to the output Excel file
output_file = '/Users/srujananeelavar/Documents/Spring2023/Research/covarianceAnalysis/rio122/alleles/rio17allele.xlsx'

# define the sequence you are looking for
search_sequence = 'MRCELKISSSYVFPNSIPEK'

# read the input Excel file into a pandas DataFrame
data = pd.read_excel(input_file)

# create a new column called 'allele' and populate it with 1 or 0 depending on whether the search sequence is found in the 'Sequence' column
data['allele'] = data['Sequence'].apply(lambda x: 1 if x == search_sequence else 0)

# create a new DataFrame with just the 'Contigs' and 'allele' columns
output_data = data[['Contig', 'allele']]

# write the output DataFrame to the output Excel file
output_data.to_excel(output_file, index=False)
