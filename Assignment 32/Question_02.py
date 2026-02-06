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
    

def FindDuplicate(DirectoryName, logObj):

    Ret = os.path.exists(DirectoryName)

    if (Ret == False):
        logObj.write("There is no such directory\n")
        return {}
    
    Ret = os.path.isdir(DirectoryName)

    if (Ret == False):
        logObj.write("It is not a directory\n")
        return {}
    
    Duplicate = {}
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
       
        for fname in FileName:

            fname = os.path.join(FolderName, fname)

            Checksum = CalculateChecksum(fname)

            if(Checksum in Duplicate):
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    return Duplicate
            

def DisplayResult(MyDict, logObj):

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    for value in Result:

        logObj.write("Duplicate File Group :\n")

        for subvalue in value:
            logObj.write(subvalue + "\n")

        logObj.write("-" * 30 + "\n")


def main(): 

    try:
        Border = "-" * 50
        timeStamp = time.ctime()
            
        print(Border)
        print("----- Marvellous Duplicate File Checking Automation -----")
        print(Border)
        
        logObj = open("Log.txt", "w")

        logObj.write(Border + "\n")
        logObj.write("This is log file created by Marvellous Automation\n")
        logObj.write("Directory Duplicate File Script\n")
        logObj.write("Log created at : " + timeStamp + "\n")
        logObj.write(Border + "\n")

        if(len(sys.argv) != 2):
            logObj.write("Invalid Number Of Arguments\n")
            logObj.close()
            return

        DirectoryName = sys.argv[1]

        Ret = FindDuplicate(DirectoryName, logObj)

        DisplayResult(Ret, logObj)

        logObj.write(Border + "\n")
        logObj.write("Duplicate scanning completed\n")
        logObj.write(Border + "\n")

        logObj.close()

        print(Border)
        print("---------- Automation Completed ----------")
        print(Border)

    except Exception as e:
        logObj.write("Error occurred : " + str(e) + "\n")


if __name__ == "__main__":
    main()
