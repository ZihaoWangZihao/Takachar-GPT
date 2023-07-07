import pandas as pd
from openpyxl.reader.excel import load_workbook

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('/Users/zihaowang/PycharmProjects/Takachar/Takachar-GPT/Hot_Tests_original.xlsx')

# Define the column index (e.g., 2 for the third column)
column_index = 2

# Get the column at the specified index
column = df.iloc[:, column_index]

allowed_values = ["0", "1"]
workbook = load_workbook('/Users/zihaowang/PycharmProjects/Takachar/Takachar-GPT/Hot_Tests_original.xlsx')
worksheet = workbook['Sheet1']
# Iterate through the rows of the column
for index, value in column.items():
    # Access each value in the column
    new_value = ""
    for i in str(value):
        if i in allowed_values:
            new_value = str(i)
        else:
            new_value = "N/A"
    cell = f"K{index + 2}"
    worksheet[cell] = new_value

# Save the modified DataFrame to the original Excel file
workbook.save('/Users/zihaowang/PycharmProjects/Takachar/Takachar-GPT/Hot_Tests_original.xlsx')
