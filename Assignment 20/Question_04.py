import threading

def Small(Str):
    Count = 0
    for ch in Str:
        if ch.islower():
            Count = Count + 1

    print(f"Thread ID   : {threading.get_ident()}")
    print(f"Thread Name : {threading.current_thread().name}")
    print("Number of lowercase characters :", Count)


def Capital(Str):
    Count = 0
    for ch in Str:
        if ch.isupper():
            Count = Count + 1

    print(f"Thread ID   : {threading.get_ident()}")
    print(f"Thread Name : {threading.current_thread().name}")
    print("Number of uppercase characters :", Count)


def Digits(Str):
    Count = 0
    for ch in Str:
        if ch.isdigit():
            Count = Count + 1

    print(f"Thread ID   : {threading.get_ident()}")
    print(f"Thread Name : {threading.current_thread().name}")
    print("Number of numeric digits :", Count)


def main():
    InputStr = input("Enter a string : ")

    t1 = threading.Thread(target=Small, args=(InputStr,), name="Small")
    t2 = threading.Thread(target=Capital, args=(InputStr,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(InputStr,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
