from threading import Thread, current_thread, Lock
import time

shared_data = []  # Shared data among threads
shared_data_lock = Lock()  #


class MyThread(Thread):
    def __init__(self, name, target, args=()):
        super().__init__(name=name)
        self.target = target
        self.args = args
        self.is_terminated = False  # Flag indicating if the thread is terminated
        self.has_executed = False  # Flag indicating if the thread has executed

    def run(self):
        self.target(*self.args)
        if self.is_terminated:  # If the thread is terminated, remove its name from shared_data

            with shared_data_lock:
                shared_data.remove(current_thread().name)


def my_thread_function(semaphore):  # The entry point function
    thread_name = current_thread().name
    print(f"Thread {thread_name} is trying to acquire the semaphore.")
    semaphore.acquire()
    print(f"Thread {thread_name} has acquired the semaphore.")
    with shared_data_lock:
        shared_data.append(thread_name)
        print(f"Thread {thread_name} adds its name to the shared data:")
        print(shared_data)
    time.sleep(2)
    print(f"Thread {thread_name} is releasing the semaphore.")
    semaphore.release()
    print(f"Thread {thread_name} is done.\n")
