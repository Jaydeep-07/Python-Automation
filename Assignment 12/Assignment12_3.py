'''3. Design automation script which accept directory name from user and create log file in that
directory which contains information of running processes as its name, PID, Username.
Usage : ProcInfoLog.py Demo
Demo is name of Directory.import psutil'''
import sys
import os
import datetime
import time

def ProcessInformation():
    listProcess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            listProcess.append(pinfo)
        except Exception:
            pass
    return listProcess


def main():
    if len(sys.argv) != 2:
        print("Invalid Number of Arguments !")
        print("Please use -h Or -u for help and usage")
        exit()
    if sys.argv[1].lower() == "-h":
        print("This Script Is Used for Finding The Running Process And Store in log File ");
        print("To Run The Script use Following Command")
        print("Example :")
        print("python Filename FolderName")
        print("python ProcessInfolog.py Demo")
        exit()
    if sys.argv[1].lower() == "-u":
        print("This Script Is Used for Finding The Running Process And Store in log File")
        exit()


    Directoryname = sys.argv[1]

    isDir = os.path.isfile(Directoryname)
    if isDir == True:
        print("It Is File  Please Enter Directory Name !!!")
        exit()

    DirExits = os.path.exists(Directoryname)

    if DirExits == False:
        os.mkdir(Directoryname)

    flag = os.path.isabs(Directoryname)
    if flag == False:
        Directoryname = os.path.abspath(Directoryname)

    isDir = os.path.isfile(Directoryname)
    if isDir == True:
        print("It Is File  Please Enter Directory Name !!!")
        exit()



    filename = os.path.join(Directoryname, "ProcessLog%s.txt" % datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))
    line = "_" * 60
    fobj = open(filename, "w")

    fobj.write(line + "\n")
    fobj.write("Runnign Process at :")
    fobj.write(time.ctime())
    fobj.write(line + "\n")

    listProc = ProcessInformation()
    for element in listProc:
        fobj.write("%s\n"%element)
    fobj.close()


if __name__ == "__main__":
    main()
