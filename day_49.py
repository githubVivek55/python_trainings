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

# seek and tell function
def file_functions():
    # seek and tell and truncate
    file_path = "data/sampleFile.csv"
    with open(file_path, "r+") as file:
        file.seek(10)
        print(file.read())
        print(file.tell())
        file.truncate(10)
        file.seek(0)
        print(file.read())




if __name__ == "__main__":
    file_path = "data/sampleFile.csv"
    file_content = read_file(file_path)
    file_handling()
    file_functions()


