# file handling operations
import os

def read_file(file_path):
    if not os.path.exists(file_path):
        return "File does not exist."
    with open(file_path, 'r') as file:
        content = file.read()
    return content

if __name__ == "__main__":
    file_path = "data/sampleFile.csv"
    file_content = read_file(file_path)
    print(f"File content:\n{file_content}")


