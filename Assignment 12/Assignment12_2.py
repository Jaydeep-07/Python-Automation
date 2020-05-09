'''2.Design automation script which accept process name and display information of that process if
it is running.
Usage : ProcInfo.py Notepad'''
import psutil
import sys


def ProcessInformation(ProcessName):
    listProcess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            if ProcessName.lower() in pinfo['name'].lower():
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
        print("This Script Is Used for check Whether Process is running  or not ");
        print("To Run The Script use Following Command")
        print("Example :")
        print("python Filename Folder1")
        print("python CheckRunningProcess.py Process ")
        exit()
    if sys.argv[1].lower() == "-u":
        print("This Script Is Used for check Whether Process is running  or not")
        exit()


    listProc = ProcessInformation(sys.argv[1])
    if len(listProc) >=1:
        for element in listProc:
            print(element)
    else:
        print("No Such Procee Is Running ",sys.argv[1])

if __name__ == "__main__":
    main()
