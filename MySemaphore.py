from threading import current_thread, Condition


class Semaphore:
    def __init__(self, value=1):
        self.value = value
        self.waiting_threads = []
        self.condition = Condition()

    def acquire(self):
        with self.condition:
            self.value -= 1
            if self.value < 0:
                # If the semaphore value is negative, block the thread
                current_thread().semaphore = self
                self.waiting_threads.append(current_thread())
                self.condition.wait()

    def release(self):
        with self.condition:
            self.value += 1
            if self.value <= 0:
                # If there are threads waiting, wake up one of them
                thread = self.waiting_threads.pop(0)
                self.condition.notify()
