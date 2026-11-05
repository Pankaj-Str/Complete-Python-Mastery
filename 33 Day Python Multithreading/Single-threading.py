import time

def task1():
    print("Task 1 started.")
    time.sleep(2)  # Simulate some time-consuming operation
    print("Task 1 completed.")

def task2():
    print("Task 2 started.")
    time.sleep(1)  # Simulate another operation
    print("Task 2 completed.")

def main():
    print("Single-threaded program started.")
    task1()
    task2()
    print("Single-threaded program completed.")

if __name__ == "__main__":
    main()
