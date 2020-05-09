'''Design automation script which accept directory name and display checksum of all files.
Usage : DirectoryChecksum.py “Demo”

Demo is name of directory.'''

from sys import *
import os
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

def  FileChecksum(Directoryname):
    flag = os.path.isabs(Directoryname)

    if flag == False:
        Directoryname = os.path.abspath(Directoryname)

    isDir = os.path.isfile(Directoryname)
    if isDir == True:
        print("It Is File  Please Enter Directory Name !!!")
        exit()

    DirExits = os.path.exists(Directoryname)
    if DirExits == False:
        print("Directory ",Directoryname,"Does Not Exits  ")
        exit()

    for Folder,SubFolders,Files in os.walk(Directoryname):
        print(Folder)
        for file in Files:
            path = os.path.join(Folder,file)
            FileChecksum = hashFile(path)
            print("The Checksum of ",file ," Is   :",FileChecksum)


def main():
    print("This Script Is Used For Finding CheckSum Of File")
    if (len(argv) > 2):
        print("Invalid Number Of Arguments ")
        print("Please use -h or -u for help and usage ");
        exit()
    if argv[1].lower() == "-h":
        print("This Script Is Used For Finding CheckSum Of File ");
        print("Example :")
        print("python Filename Folder1")
        print("python DirectoryChecksum.py Demo ")
        print("DirectoryChecksum.py : Name Of The file")
        print("Demo : Name of the Folder ")
        exit()
    if argv[1].lower() == "-u":
        print("This Script Is Used For Finding CheckSum Of File ")
        exit()

    Directoryname = argv[1];
    try:

        FileChecksum(Directoryname)

    except Exception:
        print("Exception Occurred :",Exception)


if __name__ == "__main__":
    main();