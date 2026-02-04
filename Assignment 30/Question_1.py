def main():

    try:
        FileName = input("Enter file name: ")

        fobj = open(FileName, "r")

        Count = 0

        for line in fobj:
            Count = Count + 1

        fobj.close()

        print("Total number of lines in file:", Count)

    except FileNotFoundError:
        print("Unable to open file as there is no such file.")
    except Exception as e:
        print("Error:", e)
    finally:
        print("End Of Application")


if __name__ == "__main__":
    main()
