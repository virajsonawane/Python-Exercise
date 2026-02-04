def ShowContent(Read1):

    Store = open(Read1,"r")

    Print = Store.read()
    
    print(Print)

def main():

    Input = input("Enter File Name : ")

    ShowContent(Input)

if __name__ == "__main__":
    main()