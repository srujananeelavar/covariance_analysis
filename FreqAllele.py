# import pandas as pd

# # Load the Excel file into a pandas DataFrame
# df = pd.read_excel("/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144TopHits_translated_BS72.xlsx")

# # Get the counts of each sequence in the 'sequence' column
# counts = df['Sequence'].value_counts().reset_index()

# # Rename the columns to 'Alleles' and 'Counts'
# counts = counts.rename(columns={'index': 'Alleles', 'Sequence': 'Counts'})

# # Save the counts to a new Excel file
# counts.to_excel("/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144AlleleCounts_BS72.xlsx", index=False)
import pandas as pd
from openpyxl import Workbook

# Define the path to your input Excel file
input_excel_file = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144TranslatedAll.xlsx"

# Load the Excel file
xls = pd.ExcelFile(input_excel_file)

# Create a new workbook to save all sheets into a single Excel file
workbook = Workbook()

# Loop through all sheets in the Excel file
for sheet_name in xls.sheet_names:
    # Load the sheet into a pandas DataFrame
    df = xls.parse(sheet_name)

    # Get the counts of each sequence in the 'Sequence' column
    counts = df['Sequence'].value_counts().reset_index()

    # Rename the columns to 'Alleles' and 'Counts'
    counts = counts.rename(columns={'index': 'Alleles', 'Sequence': 'Counts'})

    # Create a new sheet with the same data
    sheet = workbook.create_sheet(title=sheet_name)
    
    # Convert the pandas DataFrame to a list of lists for openpyxl
    data = counts.values.tolist()

    # Write the data to the new sheet
    for row in data:
        sheet.append(row)

# Remove the default sheet created and save the Excel file
workbook.remove(workbook.active)
output_excel_file = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144AlleleCountsTranslatedAll.xlsx"
workbook.save(output_excel_file)