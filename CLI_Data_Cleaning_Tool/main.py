import csv
from tkinter.filedialog import askopenfilename

def read_csv(filepath):
    rows = []
    try:
        with open(filepath, mode='r', newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except FileNotFoundError:
        print("The file at the specified path not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
    return rows


def write_csv(filepath, rows):
    try:
        with open(filepath, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f'Data successfully written to {filepath}')
    except Exception as e:
        print(f'An error occurred: {e}')


def remove_duplicates(rows):
    """Removes duplicate rows in data"""
    unique_rows = []
    seen = set()
    for row in rows:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(row)
    return unique_rows


def convert_to_lowercase(rows):
    """Converts all data strings to lowercase"""
    new_rows = []
    for row in rows:
        new_row = [cell.lower() if isinstance(cell, str) else cell for cell in row]
        new_rows.append(new_row)
    return new_rows


def remove_trailing_whitespace(rows):
    """Removes trailing whitespace from all data strings"""
    new_rows = []
    for row in rows:
        new_row = [cell.strip() if isinstance(cell, str) else cell for cell in row]
        new_rows.append(new_row)
    return new_rows


if __name__ == "__main__":
    filepath = askopenfilename()
    data = read_csv(filepath)

    if data:
        print("Cleaning data... ")
        data = remove_trailing_whitespace(data)
        data = convert_to_lowercase(data)
        data = remove_duplicates(data)

    else:
        print("No data to process!")
        
    filepath = askopenfilename()
    write_csv(filepath, data)