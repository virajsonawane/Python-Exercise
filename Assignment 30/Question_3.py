def main():

    try:
        FileName = input("Enter file name: ")

        fobj = open(FileName, "r")

        print("Contents of file line by line:")

        for line in fobj:
            print(line, end="")

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file.")
    except Exception as e:
        print("Error:", e)
    finally:
        print("\nEnd Of Application")


if __name__ == "__main__":
    main()
