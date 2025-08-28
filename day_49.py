# file handling operations
import os

def read_file(file_path):
    if not os.path.exists(file_path):
        return "File does not exist."
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def file_handling():
    file_path = "data/sampleFile.csv"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(lines)
            for line in lines:
                cols = line.strip().split(',')
                s = [int(c) for c in cols if c.isdigit()]
                print(s)




if __name__ == "__main__":
    file_path = "data/sampleFile.csv"
    file_content = read_file(file_path)
    file_handling()


