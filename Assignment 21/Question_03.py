import threading

counter = 0
lock = threading.Lock()

def IncreaseCounter(times):
    global counter
    for i in range(times):
        with lock:
            counter += 1
            print(f"{threading.current_thread().name} incremented counter to {counter}")

def main():
    threads = []
    num_threads = int(input("Enter number of threads: "))
    increments_per_thread = int(input("Enter number of increments per thread: "))

    for i in range(num_threads):
        t = threading.Thread(target=IncreaseCounter, args=(increments_per_thread,), name=f"Thread-{i+1}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nFinal value of counter is:", counter)

if __name__ == "__main__":
    main()
