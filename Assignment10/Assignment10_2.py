'''Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extenntion.

Usage : DirectoryRename.py “Demo” “.txt” “.doc”

Demo is	name of directory and .txt is the extension that we want to search and rename
with .doc.

After execution this script each .txt file gets renamed as .doc.'''

from sys import *
import os


def FileRename(DirectoryName, Extension1, Extension2):
    flag = os.path.isabs(DirectoryName)
    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)
    flag = os.path.isdir(DirectoryName)
    if flag == False:
        print("It IS Not Directory  ")
        exit()
    count = 0

    print(DirectoryName)
    print("_________________________________________________________________")
    for Folder,SubFolder,files in os.walk(DirectoryName):
        print("_________________________________________________________________")
        print("Folder Name is")
        print(Folder)
        print("_________________________________________________________________")
        for filename in files:
            print(filename)
            base_file , ext = os.path.splitext(filename)
            print(base_file)
            print("_________________________________________________________________")
            print(os.path.abspath(filename))
            print("_________________________________________________________________")
            full_file_name = os.path.join(Folder, filename)
            print("Full File name is !!!!",full_file_name)
            if ext == Extension1:
                count = count + 1
                os.rename(full_file_name,base_file+Extension2)

    if count == 0:
        print("There Is No file With ",Extension1)

def main():
    print("This Script Is Used For Directory File Search With Specific FileExtension")
    if (len(argv) != 4):
        print("Invalid Number Of Arguments ")
        print("Please use -h or -u for help and usage ");
        exit()
    if argv[1].lower() == "-h":
        print("This Script is Used For Changing the file Extension from directory ");
        print("Example :")
        print("python Filename Extension1 Extension2")
        print("python DirectoryRename.py .txt .doc")
        exit()
    if argv[1].lower() == "-u":
        print("This Script is Used For Changing the file Extension from directory")
        exit()

    DirectoryName = argv[1]
    Extension1 = argv[2]
    Extension2 = argv[3];
    FileRename(DirectoryName, Extension1, Extension2)


if __name__ == "__main__":
    main();
