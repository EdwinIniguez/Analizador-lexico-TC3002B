import pandas as pd
from pathlib import Path

def convert_all_xlsx_to_csv():
    # Get the current working directory
    current_dir = Path.cwd()
    
    # Iterate over all .xlsx files in the current directory
    xlsx_files = list(current_dir.glob("*.xlsx"))
    
    if not xlsx_files:
        print("No .xlsx files found in the current directory.")
        return

    for excel_file in xlsx_files:
        # Skip temporary files created by Excel when a file is open
        if excel_file.name.startswith("~$"):
            continue
            
        try:
            print(f"Converting '{excel_file.name}'...")
            
            # Read the Excel file using the second row (index 1) as headers
            df = pd.read_excel(excel_file, header=1)
            
            # Drop any empty columns that Pandas defaults to 'Unnamed' (like 'Unnamed: 0')
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            
            # Change the file extension from .xlsx to .csv
            csv_file_path = excel_file.with_suffix('.csv')
            
            # Save the dataframe to CSV, ignoring the pandas index
            df.to_csv(csv_file_path, index=False)
            
            print(f"Successfully saved as '{csv_file_path.name}'\n")
            
        except Exception as e:
            print(f"Error converting '{excel_file.name}': {e}\n")

if __name__ == "__main__":
    convert_all_xlsx_to_csv()
