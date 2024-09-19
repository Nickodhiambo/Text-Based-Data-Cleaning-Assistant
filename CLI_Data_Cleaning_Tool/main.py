import csv
from tkinter.filedialog import askopenfilename

def read_csv(filepath):
    rows = []
    try:
        with open(filepath, mode='r') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except FileNotFoundError:
        print("The file at the specified path not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
    return rows


def write_csv(filepath, rows):
    try:
        with open(filepath, mode='w') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f'Data successfully written to {filepath}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    filepath = askopenfilename()
    data = read_csv(filepath)

    if data:
        print("Original data: ")
        for row in data:
            print(row)
        
    filepath = askopenfilename()
    write_csv(filepath, data)