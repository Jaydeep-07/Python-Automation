'''Design automation script which accept directory name and write names of duplicate files from
that directory into log file named as Log.txt. Log.txt file should be created into current
directory.

Usage : DirectoryDusplicate.py “Demo”
Demo is name of directory.'''

import os
from sys import *;
import hashlib

def hashFile(path , blocksize =1024 ):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf)>0 :
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def PrintResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print("Duplicates Found ");
        print("Following Are the Duplicate ")
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
    else:
        print("No Duplicates Found")



def DuplicateFiles(Directoryname):
    flag = os.path.isabs(Directoryname)

    if flag == False:
        Directoryname = os.path.abspath(Directoryname)

    isDir = os.path.isfile(Directoryname)
    if isDir == True:
        print("It Is File  Please Enter Directory Name !!!")
        exit()

    DirExits = os.path.exists(Directoryname)
    if DirExits == False:
        print("Directory ", Directoryname, "Does Not Exits  ")
        exit()

    dups = {}
    fobj = open("Log.txt", "w")
    for Folder,SubFolders,Files in os.walk(Directoryname):
        print(Folder)
        for file in Files:
            path = os.path.join(Folder,file)
            File_hash = hashFile(path)
            if File_hash in dups :
                dups[File_hash].append(path)
                fobj.write(file)

            else:
                dups[File_hash]= [path]
    fobj.close()
    return dups

def main():
    print("This Script Is Used For Find The Duplicates File from The Directory ")
    if (len(argv) > 2):
        print("Invalid Number Of Arguments ")
        print("Please use -h or -u for help and usage ");
        exit()
    if argv[1].lower() == "-h":
        print("This Script Is Used For Find The Duplicates File from The Directory");
        print("Example :")
        print("python Filename Folder1")
        print("python DirectoryDuplicate.py Demo ")
        print("DirectoryDuplicate.py : Name Of The file")
        print("Demo : Name of the Folder ")
        exit()
    if argv[1].lower() == "-u":
        print("This Script Is Used For Find The Duplicates File from The Directory")
        exit()

    Directoryname = argv[1];
    try:
        arr = {}
        arr = DuplicateFiles(Directoryname)
        PrintResults(arr)

    except Exception:
        print("Exception Occurred :",Exception)


if __name__ == "__main__":
    main();