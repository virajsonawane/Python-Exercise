import sys
import os
import time

def DirectoryCopyExt(SourceDir, DestDir, Extension):

    try:
        timeStamp = time.ctime()
        Border = "-" * 50

        LogFileName = "Marvellous%s.log" %(timeStamp)
        LogFileName = LogFileName.replace(" ", "_")
        LogFileName = LogFileName.replace(":", "_")

        fobj = open(LogFileName, "w")

        fobj.write(Border + "\n")
        fobj.write("This is log file created by Marvellous Automation\n")
        fobj.write("Directory Copy With Extension Script\n")
        fobj.write(Border + "\n")
        
        if(os.path.exists(SourceDir) == False):
            fobj.write("Source directory not found\n")
            return

        if(os.path.isdir(SourceDir) == False):
            fobj.write("Source path is not a directory\n")
            return
       
        if(os.path.exists(DestDir) == False):
            os.mkdir(DestDir)
            fobj.write("Destination directory created : " + DestDir + "\n")

        CopyCount = 0

        for FolderName, SubFolder, FileName in os.walk(SourceDir):
            for fname in FileName:

                if fname.endswith(Extension):

                    SourcePath = os.path.join(FolderName, fname)
                    DestPath = os.path.join(DestDir, fname)
                    
                    srcfile = open(SourcePath, "rb")
                    destfile = open(DestPath, "wb")

                    data = srcfile.read()
                    destfile.write(data)

                    srcfile.close()
                    destfile.close()

                    CopyCount = CopyCount + 1

                    fobj.write("Copied : " + SourcePath + " -> " + DestPath + "\n")

        fobj.write(Border + "\n")
        fobj.write("Total Files Copied with " + Extension + " extension : " + str(CopyCount) + "\n")
        fobj.write("Log created at : " + timeStamp + "\n")
        fobj.write(Border + "\n")

        fobj.close()

    except Exception as e:
        fobj.write("Error occurred : " + str(e) + "\n")


def main():

    Border = "-" * 50
    print(Border)
    print("----- Marvellous Directory Copy With Extension Automation -----")
    print(Border)

    if (len(sys.argv) != 4):
        print("Invalid Number Of Arguments")
        return

    DirectoryCopyExt(sys.argv[1], sys.argv[2], sys.argv[3])

    print(Border)
    print("---------- Automation Completed ----------")
    print(Border)


if __name__ == "__main__":
    main()
