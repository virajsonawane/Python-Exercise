import sys
import os
import time

def DirectoryRename(DirName, OldExt, NewExt):

    try:
        timeStamp = time.ctime()
        Border = "-" * 50

        LogFileName = "Marvellous%s.log" %(timeStamp)
        LogFileName = LogFileName.replace(" ", "_")
        LogFileName = LogFileName.replace(":", "_")

        fobj = open(LogFileName, "w")

        fobj.write(Border + "\n")
        fobj.write("This is log file created by Marvellous Automation\n")
        fobj.write("Directory Rename Script\n")
        fobj.write(Border + "\n")
        
        if(os.path.exists(DirName) == False):
            fobj.write("Directory not found\n")
            return

        if(os.path.isdir(DirName) == False):
            fobj.write("Given path is not a directory\n")
            return

        RenameCount = 0

        for FolderName, SubFolder, FileName in os.walk(DirName):
            for fname in FileName:

                if fname.endswith(OldExt):

                    OldPath = os.path.join(FolderName, fname)

                    NewFileName = fname.replace(OldExt, NewExt)
                    NewPath = os.path.join(FolderName, NewFileName)

                    os.rename(OldPath, NewPath)

                    RenameCount = RenameCount + 1

                    fobj.write("Renamed : " + OldPath + " -> " + NewPath + "\n")

        fobj.write(Border + "\n")
        fobj.write("Total Files Renamed : " + str(RenameCount) + "\n")
        fobj.write("Log created at : " + timeStamp + "\n")
        fobj.write(Border + "\n")

        fobj.close()

    except Exception as e:
        fobj.write("Error occurred : " + str(e) + "\n")


def main():

    Border = "-" * 50
    print(Border)
    print("----- Marvellous Directory Rename Automation -----")
    print(Border)

    if (len(sys.argv) != 4):
        print("Invalid Number Of Arguments")        
        return

    DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

    print(Border)
    print("---------- Automation Completed ----------")
    print(Border)


if __name__ == "__main__":
    main()
