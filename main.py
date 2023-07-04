# Python File 1:
#
# Goal: {010222: [(8*60)/2,33,61,103], ...}
#
# Python File 2:
#
# Match by key --> csv file by rows

import pandas as pd
import os


def csv_to_excel():
    # Specify the directory path
    directory = "/Users/zihaowang/PycharmProjects/Takachar/Takachar-GPT/logs_v6"

    # Iterate through each file in the directory
    counter = 0
    for filename in os.listdir(directory):
        # Check if the item is a file
        if os.path.isfile(os.path.join(directory, filename)):
            # Get the full path of the file
            file_path = os.path.join(directory, filename)
            csv_data = pd.read_csv(file_path)
            excel_filename = filename[:6]
            output_directory = "/Users/zihaowang/PycharmProjects/Takachar/Takachar-GPT/logs_v6_excels"
            output_file = os.path.join(output_directory, f'{excel_filename}.xlsx')
            csv_data.to_excel(output_file, index=False)
        counter += 1
        print(counter)


def add_state_column():
    directory = "/Users/zihaowang/PycharmProjects/Takachar/Takachar-GPT/logs_v6_excels"

    # Iterate through each file in the directory
    counter = 0
    for filename in os.listdir(directory):
        # Check if the item is a file
        try:
            if os.path.isfile(os.path.join(directory, filename)):
                # Get the full path of the file
                file_path = os.path.join(directory, filename)
                excel_data = pd.read_excel(file_path)

                # Set the column header name
                new_column_header = 'State'

                # Add the new column header to the DataFrame
                excel_data[new_column_header] = None

                # Save the modified DataFrame to a new Excel file
                excel_data.to_excel(file_path, index=False)
            print(filename)
        except:
            print(f"failed: {filename}")

# Corrupt Files: [180722.xlsx, 250422.xlsx, 220621.xlsx]
