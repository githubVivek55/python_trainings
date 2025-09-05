#  file operations
import os
def read_file(file_path):
    """Read the content of a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)


if __name__ == "__main__":
    file_path = "data/sampleFile.csv"
    try:
        content = read_file(file_path)
        print("File content:")
        print(content)
        new_content = "New content added to the file."
        write_file(file_path, new_content)
        print("File updated successfully.")
        content = read_file(file_path)
        print("File content:")
        print(content)
    except FileNotFoundError as e:
        print(e)
