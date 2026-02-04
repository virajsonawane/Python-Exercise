def main():

    try:
        FileName = input("Enter file name: ")
        SearchWord = input("Enter word to search: ")

        fobj = open(FileName, "r")

        Data = fobj.read()

        fobj.close()

        if SearchWord in Data:
            print("The word " + SearchWord + " is found in the file.")
        else:
            print("The word " + SearchWord + " is not found in the file.")


    except FileNotFoundError:
        print("Unable to open file as there is no such file.")
    except Exception as e:
        print("Error:", e)
    finally:
        print("End Of Application")


if __name__ == "__main__":
    main()
