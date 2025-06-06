
# script to read all files under a directory after a given date
import os
from datetime import datetime
def read_files_after_date(directory, date_str):
    """
    Reads all files in the specified directory that were modified after the given date.

    :param directory: The directory to search for files.
    :param date_str: The date string in 'YYYY-MM-DD' format.
    :return: A list of file paths modified after the specified date.
    """
    date = datetime.strptime(date_str, '%Y-%m-%d')
    files_after_date = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getmtime(file_path) > date.timestamp():
                files_after_date.append(file_path)

    return files_after_date

# Example usage
if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    date_str = input("Enter the date (YYYY-MM-DD): ")
    files = read_files_after_date(directory, date_str)
    
    if files:
        print("Files modified after", date_str, ":")
        for file in files:
            print(file)
    else:
        print("No files modified after", date_str)