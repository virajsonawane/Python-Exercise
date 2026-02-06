import sys
import hashlib
import os
import time

def CalculateChecksum(FileName):        

    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()
    

def DirectoryWatcher(DirectoryName):

    try:
        timeStamp = time.ctime()
        Border = "-" * 50

        LogFileName = "Marvellous%s.log" %(timeStamp)
        LogFileName = LogFileName.replace(" ", "_")
        LogFileName = LogFileName.replace(":", "_")

        fobj = open(LogFileName, "w")

        fobj.write(Border + "\n")
        fobj.write("This is log file created by Marvellous Automation\n")
        fobj.write("Directory Checksum Script\n")
        fobj.write(Border + "\n")

        Ret = os.path.exists(DirectoryName)

        if (Ret == False):
            fobj.write("There is no such directory\n")
            return
        
        Ret = os.path.isdir(DirectoryName)

        if (Ret == False):
            fobj.write("It is not a directory\n")
            return
        
        FileCount = 0

        for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
           
            for fname in FileName:

                FileCount = FileCount + 1

                fname = os.path.join(FolderName, fname)

                Checksum = CalculateChecksum(fname)

                fobj.write("File Name : " + fname + "\n")
                fobj.write("Checksum  : " + Checksum + "\n")
                fobj.write("-" * 30 + "\n")

        fobj.write(Border + "\n")
        fobj.write("Total Files Scanned : " + str(FileCount) + "\n")
        fobj.write("Log created at : " + timeStamp + "\n")
        fobj.write(Border + "\n")

        fobj.close()

    except Exception as e:
        fobj.write("Error occurred : " + str(e) + "\n")


def main():  

    Border = "-" * 50
    print(Border)
    print("----- Marvellous Directory Files checksum Calculation Automation -----")
    print(Border)

    if (len(sys.argv) != 2):
        print("Invalid Number Of Arguments")
        return
    
    DirectoryWatcher(sys.argv[1])

    print(Border)
    print("---------- Automation Completed ----------")
    print(Border)

if __name__ == "__main__":
    main()
