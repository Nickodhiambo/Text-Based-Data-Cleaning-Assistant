# Text-based Data Cleaning Assistant

A **command-line tool** written in Python to clean and validate data stored in various file formats, such as CSV, Excel, text, and log files. This tool provide funtionality to clean data, including the command line tools to remove trailing whitespaces and duplicates, and converting to lowercase. In addition, the tool offers flexible and user-friendly functionality to validate email addresses, standardize phone numbers, format dates, check for missing values, and ensure correct data types in specified columns. It is designed for handling data across different formats, and is particularly useful for quick, efficient data preprocessing.

## Features

- **Email Validation**: Parse through a column and validate email addresses. Identifies and labels invalid emails.
- **Phone Number Standardization**: Standardizes phone numbers in the correct format based on the specified rules.
- **Date Formatting**: Formats dates into a specified format.
- **Convert to Lowercase**: Converts all text in a specified column to lowercase.
- **Data Type Validation**: Validates if the data in a column conforms to a specified data type (e.g., `int`, `float`, `date`).
- **Check for Missing Values**: Detects and reports any missing or null values in the specified column.
- **Supports Multiple File Types**: Works with CSV, Excel, text, and log files.
- **Remove duplicate entries**: Removes duplicate entries from data.
- **Trim whitespaces**: Removes whitespaces from data entries.

## How It Works

The tool allows you to pass specific flags from the command line to invoke various cleaning and validation functionalities. For instance, you can choose to validate email addresses or standardize phone numbers by simply specifying the correct command.

### Command-Line Arguments

| Argument                      | Description                                                     |
|-------------------------------------------------------------------------------------------------|
| `--validate_email`                     | Validates email addresses in a specified column          |
| `--standardize_phone`                  | Standardizes phone numbers in a specified column         |
| `--format_dates`                       | Format dates in a specified column to a standard format  |
| `--lowercase`                          | Converts all text data to lowercase                      |
| `--validate_type`                      | Validates data type in a specified column                |
| `--check_missing`                      | Checks for and mark missing values in a specified column |
| `--trim_whitespace`                    | Removes whitespaces in data rows                         |
| `--remove_duplicates`                  | Removes duplicate entries in data                        |

## Installation

To use this tool, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/Nickodhiambo/Text-Based-Data-Cleaning-Assistant.git
   ```

2. Create a Python virtual environment
    ```bash
    python -m venv venv
    <!-- For windows -->
    venv\Scripts\activate

    <!-- For linux -->
    source venv/bin/activate
    ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Change into project directory
   ```bash
   cd CLI_Data_Cleaning_Tool
   ```

## Usage

Run the tool using the command line by specifying the flag corresponding to the function you want to execute.

### Examples:

1. **Validate Emails**:
   ```bash
   python main.py --validate_email "Email"
   ```
   This will validate email addresses in the column named "Email" of your data file.

2. **Standardize Phone Numbers**:
   ```bash
   python main.py --standardize_phone "Phone Number"
   ```
   Standardizes the phone numbers in the column named "Phone Number".

3. **Format Dates**:
   ```bash
   python main.py --format_date "Date of Birth"
   ```
   Formats the dates in the column named "Date of Birth" to a standard format (e.g., `YYYY-MM-DD`).

4. **Convert to Lowercase**:
   ```bash
   python main.py --lowercase 
   ```
   Converts all text data to lowercase.

5. **Check for Missing Values**:
   ```bash
   python main.py --check_missing "Age"
   ```
   Identifies any missing values in the "Age" column.

6. **Validate Data Type**:
   ```bash
   python main.py --validate_type "Price" float
   ```
   Ensures that the data in the "Price" column is of the type `float`.

7. **Trim White Space**
    ```bash
    python main.py --trim_whitespace
    ```
    Removes leading and trailing whitespaces from data rows

8. **Remove Duplicate Data**
    ```bash
    python main.py --remove_duplicates
    ```
    Removes duplicate data entries from data file

## File Formats Supported

The tool supports the following file formats:
- CSV files (`.csv`)
- Excel files (`.xlsx`)
- Text files (`.txt`)
- Log files (`.log`)

### How to Specify File Input and Output:
The tool automatically detects the file type based on the file extension. To process a file, just run
`python main.py [--flag_option]` and a GUI will open prompting for a file input. Once your file is
processed, the tool will prompt you to provide a destination file for the cleaned data.

## Example Files

Here’s an example of a simple Excel file (`data.xlsx`) you could use with this tool:

| Name   | Email                  | Phone        | Date of Birth |
|--------|------------------------|--------------|---------------|
| John   | john.doe@gmail.com      | 555-1234     | 1990-01-15    |
| Jane   | invalid.email@wrong     | 555-5678     | 12/31/1995    |
| David  | david.smith@example.com | (555) 876-1234 | 1992-07-20  |
| Maria  | maria@gmail             | +1 555 2345 | 01/15/1985     |

You can test the functionality by running commands to clean and validate this data.

## Testing

You can create various test files (CSV, Excel, text, and log) and run the tool to verify the different functionalities. For example:
```bash
python main.py --validate_email Email --check_missing Email
```

## Future Enhancements

- **Performance Optimization**: Consider implementing batch processing for large files.
- **Additional File Formats**: Adding support for other data formats like JSON or XML.
- **GUI Version**: Expanding the command-line tool into a GUI-based application for non-technical users.

## Contributing

If you'd like to contribute, please fork the repository and submit a pull request. Feel free to suggest new features or report bugs through the issue tracker.

## Acknowledgments

Special thanks to all the developers and open-source projects that made this tool possible.

---