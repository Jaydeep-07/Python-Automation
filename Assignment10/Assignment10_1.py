'''1.Design automation script which accept directory name and file extension from user. Display all
files with that extension.

Usage : DirectoryFileSearch.py “Demo” “.txt”

Demo is name of directory and .txt is the extension that we want to search.'''
from sys import *
import os


def Directoryfile(DirectoryName, Extension):
    flag = os.path.isdir(DirectoryName)
    if flag == False:
        print("It IS Not Directory  ")
        exit()
    count = 0
    for folder, subFolder, Files in os.walk(DirectoryName):
        print("Current Directory is ",folder)
        for file in Files:
            if file.endswith(Extension):
                count = count + 1
                print(file);

    if count == 0 :
        print("No Such File With Extension",Extension)

def main():
    print("This Script Is Used For Directory File Search With Specific FileExtension")
    if (len(argv)!=3):
        print("Invalid Number Of Arguments ")
        print("Please use -h or -u for help and usage ");
        exit()
    if argv[1].lower() == "-h":
        print("This Script is Used For For Directory Search File");
        print("Example :")
        print("python Filename DirectoryName Extension")
        print("python DirectoryFileSearch.py Demo .txt")
        exit()
    if argv[1].lower() == "-u":
        print("This Script is used for file Search in Directory")
        exit()

    DirectoryName = argv[1]
    Extension = argv[2];
    try:
        Directoryfile(DirectoryName, Extension)
    except Exception:
        print("Exception Occurred ", Exception)


if __name__ == "__main__":
    main();
