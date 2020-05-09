'''Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.

Usage : DirectoryCopy.py “Demo” “Temp”

Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files from Demo to Temp.'''

from sys import *
import os
import shutil


def FileCopy(DirectoryName1, DirectoryName2):
    flag = os.path.isabs(DirectoryName1)
    flag1 = os.path.isabs(DirectoryName2)

    if flag == False:
        DirectoryName1 = os.path.abspath(DirectoryName1)

    if flag1 == False:
        DirectoryName2 = os.path.abspath(DirectoryName2)

    isDir = os.path.isfile(DirectoryName2)

    if isDir == True:
        print("Please Enter File Name :")
        exit()

    isDirexits = os.path.exists(DirectoryName2)

    if isDirexits == False:
        print("Directory is making ")
        os.mkdir(DirectoryName2)

    src_files = os.listdir(DirectoryName1)
    print(src_files)
    for file_name in src_files:
        full_file_name = os.path.join(DirectoryName1, file_name)
        print(full_file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, DirectoryName2)


def main():
    print("This Script Is Used For Copy files From  One Directory to Another")
    if (len(argv) > 3):
        print("Invalid Number Of Arguments ")
        print("Please use -h or -u for help and usage ");
        exit()
    if argv[1].lower() == "-h":
        print("This Script Is Used For Copy files From  One Directory to Another ");
        print("Example :")
        print("python Filename Folder1 Folder2")
        print("python DirectoryCopy.py Demo Demo1")
        exit()
    if argv[1].lower() == "-u":
        print("This Script Is Used For Copy files From  One Directory to Another")
        exit()

    DirectoryName1 = argv[1]
    DirectoryName2 = argv[2]

    try:
        FileCopy(DirectoryName1, DirectoryName2)
    except Exception:
        print("Exception Occurred :", Exception)


if __name__ == "__main__":
    main();
