import hashlib
import sys
import os

def CalculateChecksum(FileName):

    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def main():

    try:
        if (len(sys.argv) != 3):
            print("File names missing. Please enter File Names to compare.")
            return

        File1 = sys.argv[1]
        File2 = sys.argv[2]

        if not os.path.exists(File1):
            print("First file not found")
            return

        if not os.path.exists(File2):
            print("Second file not found")
            return

        Checksum1 = CalculateChecksum(File1)
        Checksum2 = CalculateChecksum(File2)

        if Checksum1 == Checksum2:
            print("Success")
        else:
            print("Failure")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()