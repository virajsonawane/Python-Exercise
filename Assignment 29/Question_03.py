import sys

def main():

    try:
        if (len(sys.argv) != 2):
            print("Source file name missing. Please enter Source File Name.")
            return

        SourceFile = sys.argv[1]

        srcfile = open(SourceFile, "r")
        print("Source file opened successfully.")

        Data = srcfile.read()

        destfile = open("Demo.txt", "w")
        destfile.write(Data)

        print("Contents copied into Demo.txt successfully.")

        srcfile.close()
        destfile.close()

    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print("Error:", e)
    finally:
        print("End Of Application")


if __name__ == "__main__":
    main()
