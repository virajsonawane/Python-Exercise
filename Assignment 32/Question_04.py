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
    

def DeleteDuplicate(DirectoryName):

    try:
        StartTime = time.time()

        Border = "-" * 50
        timeStamp = time.ctime()
        
        logObj = open("Log.txt", "w")

        logObj.write(Border + "\n")
        logObj.write("This is log file created by Marvellous Automation\n")
        logObj.write("Directory Duplicate File Deletion With TimeStamp Script\n")
        logObj.write(Border + "\n")
        
        Ret = os.path.exists(DirectoryName)

        if (Ret == False):
            logObj.write("There is no such directory\n")
            return
        
        Ret = os.path.isdir(DirectoryName)

        if (Ret == False):
            logObj.write("It is not a directory\n")
            return
        
        Duplicate = {}
        
        for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
           
            for fname in FileName:

                fname = os.path.join(FolderName, fname)

                Checksum = CalculateChecksum(fname)

                if(Checksum in Duplicate):
                    Duplicate[Checksum].append(fname)
                else:
                    Duplicate[Checksum] = [fname]

        DeletedCount = 0
        
        for value in Duplicate.values():

            count = 0

            for subvalue in value:

                count = count + 1
                
                if(count > 1):

                    os.remove(subvalue)

                    logObj.write("Deleted File : " + subvalue + "\n")

                    DeletedCount = DeletedCount + 1

        EndTime = time.time()   

        ExecutionTime = EndTime - StartTime

        logObj.write(Border + "\n")
        logObj.write("Total Deleted Files : " + str(DeletedCount) + "\n")
        logObj.write("Execution Time Required : " + str(ExecutionTime) + " seconds\n")        
        logObj.write("Duplicate removal completed\n")
        logObj.write("Log created at : " + timeStamp + "\n")
        logObj.write(Border + "\n")

        logObj.close()

    except Exception as e:
        logObj.write("Error occurred : " + str(e) + "\n")


def main(): 

    Border = "-" * 50
            
    print(Border)
    print("----- Marvellous Duplicate File Checking and Deletion With TimeStamp Automation -----")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number Of Arguments")
        return

    DeleteDuplicate(sys.argv[1])


if __name__ == "__main__":
    main()
