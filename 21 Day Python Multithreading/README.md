# Threading in Python

Threading in Python allows you to run multiple threads (smaller units of a process) concurrently within a single process. This can be useful for tasks that can be parallelized or tasks that involve I/O-bound operations where threads can perform other work while waiting for I/O to complete. Python provides a built-in module called `threading` for working with threads. Here's an overview of threading in Python and an example:

**Creating Threads:**

To use threads in Python, you'll typically follow these steps:

1. Import the `threading` module.
2. Define a function that represents the task you want the thread to perform.
3. Create thread objects, specifying the target function.
4. Start the threads.
5. Wait for the threads to finish if necessary.

**Example:**

Here's a simple example of using threads to perform two tasks concurrently:

```python
import threading
import time

# Define two functions to be run in separate threads
def task1():
    for i in range(5):
        print("Task 1 - Iteration", i)
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2 - Iteration", i)
        time.sleep(1)

# Create thread objects
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")
```

In this example:

1. We import the `threading` module.

2. We define two functions, `task1()` and `task2()`, which represent two tasks to be performed concurrently. Each task includes a loop to print messages and a `time.sleep()` to simulate some work.

3. We create two thread objects, `thread1` and `thread2`, specifying the target function for each thread.

4. We start both threads using the `start()` method.

5. We use the `join()` method to wait for both threads to finish executing their tasks. This ensures that the "Both threads have finished." message is printed only after both threads have completed their work.

When you run this code, you'll see that the two threads execute concurrently, and their messages may be interleaved. This demonstrates how threading can be used to perform multiple tasks concurrently within a Python program.

It's important to note that Python's Global Interpreter Lock (GIL) can limit the effectiveness of multithreading for CPU-bound tasks. For CPU-bound operations, you may want to consider using the `multiprocessing` module instead to take full advantage of multiple CPU cores.