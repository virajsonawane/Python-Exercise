def main():

    try:
        SourceFile = input("Enter existing file name: ")
        DestinationFile = input("Enter new file name: ")

        srcfile = open(SourceFile, "r")

        Data = srcfile.read()

        srcfile.close()

        destfile = open(DestinationFile, "w")

        destfile.write(Data)

        destfile.close()

        print("Contents copied from one file to another file successfully.")

    except FileNotFoundError:
        print("Unable to open file as there is no such file.")
    except Exception as e:
        print("Error:", e)
    finally:
        print("End Of Application")


if __name__ == "__main__":
    main()
