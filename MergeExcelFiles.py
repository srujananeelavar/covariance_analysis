import pandas as pd
from openpyxl import Workbook
import os

# List of input Excel file names
input_files = ["/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/D39/SHP144TopHits_D39.xls", "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/TIGR4/SHP144TopHits_TIGR4.xls", "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/BS72/SHP144TopHits_BS72.xls", "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/108700/SHP144TopHits_108700.xls", "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/4595/SHP144TopHits_4595.xls"]

# Name of the output merged Excel file
output_file = "/Users/srujananeelavar/Documents/Summer2023/Research/Rgg144RiosSHP/SHP144/SHP144NT/SHP144TopHits_all.xlsx"

# Create a new Excel workbook
workbook = Workbook()


# Loop through the input files and add each sheet to the workbook
for input_file in input_files:
    xls = pd.ExcelFile(input_file)
    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        
        # Extract the name for the new worksheet from the original filename
        new_sheet_name = os.path.splitext(os.path.basename(input_file))[0].split("_")[-1]
        
        # Create a new worksheet in the workbook
        worksheet = workbook.create_sheet(title=new_sheet_name)
        
        # Write the header to the worksheet
        header = df.columns.tolist()
        worksheet.append(header)
        
        # Convert the DataFrame data (excluding header) to a list of lists
        data = df.values.tolist()
        
        # Write data to the worksheet
        for row in data:
            worksheet.append(row)

# Remove the default first sheet created by openpyxl
workbook.remove(workbook.active)

# Save the workbook to the output file
workbook.save(output_file)

print(f"Merged sheets from {len(input_files)} files into {output_file}")