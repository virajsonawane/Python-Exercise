import os

def FileCheck(F1):

    if os.path.isfile(F1):
        print("File Is Exist")

    else:
        print("File Does Not Exist")

def main():

    Input = input("Enter File Name : ")

    FileCheck(Input)

if __name__ == "__main__":
    main()