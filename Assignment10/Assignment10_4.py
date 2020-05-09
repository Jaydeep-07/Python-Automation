'''Design automation script which accept two directory names and one file extension. Copy all
files with the specified extension from first directory into second directory. Second directory
should be created at run time. 

Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”

Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files with extension .exe from Demo to Temp.'''

from sys import *
import os
import shutil


def FileCopyExtension(DirectoryName1, DirectoryName2,Extension):
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
    print("___________________________________________________")
    for file_name in src_files:
        full_file_name = os.path.join(DirectoryName1, file_name)
        print(full_file_name)

        if os.path.isfile(full_file_name):
            if full_file_name.endswith(Extension):
                shutil.copy(full_file_name, DirectoryName2)


def main():
    print("This Script Is Used For Copy files From  One Directory to Another Directory With Specified Extension ")
    if (len(argv) > 4):
        print("Invalid Number Of Arguments ")
        print("Please use -h or -u for help and usage ");
        exit()
    if argv[1].lower() == "-h":
        print("This Script Is Used For Copy files From  One Directory to Another Directory With Specified Extension ");
        print("Example :")
        print("python Filename Folder1 Folder2 Extension")
        print("python DirectoryCopy.py Demo Demo1 .py")
        exit()
    if argv[1].lower() == "-u":
        print("This Script Is Used For Copy files From  One Directory to Another Directory With Specified Extension ")
        exit()

    DirectoryName1 = argv[1]
    DirectoryName2 = argv[2]
    Extension = argv[3]
    try:
        FileCopyExtension(DirectoryName1, DirectoryName2 , Extension)
    except Exception:
        print("Exception Occurred :", Exception)


if __name__ == "__main__":
    main();
