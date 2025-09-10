# rename all file in folder to meaningful name 
# input file type
import os


def renameFiles(dir,type):
    if os.path.isdir(dir):
        list = os.listdir(dir)
        print(list)
        if len(list) > 0:
            for index, file in enumerate(list):
                fileType = os.path.splitext(file)[1]
                print(fileType)
                if fileType == type:
                    newName = f"{dir}/{index}{fileType}"
                    oldName = f"{dir}/{file}"
                    print(newName)
                    os.rename(oldName, newName)


if __name__ == "__main__":
    dir = input("Please provide dir path: ")
    type = input("Please enter file type: ")

    renameFiles(dir, type)