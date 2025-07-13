import os

def get_file_path(filename):
    """
    Returns the absolute path of the given filename in the current directory.
    """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, filename)

def main():
    filename = "day_36.py"
    file_path = get_file_path(filename)
    print(f"The absolute path of '{filename}' is: {file_path}")

def mkdir_if_not_exists(directory):
    """
    creates directory if not exists
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_folder_structure(folder_name):
    mkdir_if_not_exists(folder_name)

    for i in range(1, 6):
        subfolder = os.path.join(folder_name, f"subfolder_{i}")
        mkdir_if_not_exists(subfolder)
    


if __name__ == "__main__":
    create_folder_structure("example_folder")