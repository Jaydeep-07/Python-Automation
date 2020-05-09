'''1.Design automation script which display information of running processes as its name, PID,
Username.
Usage : ProcInfo.py'''
import psutil
import sys


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

    print("_______________________Process Information _____________________")
    listProc = ProcessInformation()
    for element in listProc:
        print(element)


if __name__ == "__main__":
    main()
