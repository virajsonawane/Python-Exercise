def main():

    try:
        FileName = input("Enter file name: ")
        SearchString = input("Enter string to search: ")

        fobj = open(FileName, "r")

        Data = fobj.read()

        fobj.close()

        Count = Data.count(SearchString)

        print("Frequency of string is:", Count)

    except FileNotFoundError:
        print("Unable to open file as there is no such file.") 
    except Exception as e:
        print("Error:", e)
    finally:
        print("End Of Application")

if __name__ == "__main__":
    main()