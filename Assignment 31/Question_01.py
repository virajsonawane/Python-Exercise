import sys
import os
import time

def DirectoryScanner(DirName, Extension):

    try:
        timeStamp = time.ctime()
        Border = "-" * 50

        LogFileName = "Marvellous%s.log" %(timeStamp)
        LogFileName = LogFileName.replace(" ", "_")
        LogFileName = LogFileName.replace(":", "_")

        fobj = open(LogFileName, "w")

        fobj.write(Border + "\n")
        fobj.write("This is log file created by Marvellous Automation\n")
        fobj.write("Directory File Search Script\n")
        fobj.write(Border + "\n")
        
        if(os.path.exists(DirName) == False):
            fobj.write("Directory does not exist\n")
            return

        if(os.path.isdir(DirName) == False):
            fobj.write("Given path is not a directory\n")
            return

        FileCount = 0

        for FolderName, SubFolder, FileName in os.walk(DirName):
            for fname in FileName:

                if fname.endswith(Extension):

                    FileCount = FileCount + 1
                    FullPath = os.path.join(FolderName, fname)
                    fobj.write("File Found : " + FullPath + "\n")

        fobj.write(Border + "\n")
        fobj.write("Total Files with " + Extension + " extension : " + str(FileCount) + "\n")
        fobj.write("Log created at : " + timeStamp + "\n")
        fobj.write(Border + "\n")

        fobj.close()

    except Exception as e:
        fobj.write("Error occurred : " + str(e) + "\n")


def main():

    Border = "-" * 50
    print(Border)
    print("----- Marvellous Directory File Search Automation -----")
    print(Border)

    if (len(sys.argv) != 3):
        print("Invalid Number Of Arguments")
        return

    DirectoryScanner(sys.argv[1], sys.argv[2])

    print(Border)
    print("---------- Automation Completed ----------")
    print(Border)


if __name__ == "__main__":
    main()
