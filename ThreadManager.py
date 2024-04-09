from MyThread import MyThread


class ThreadManager:
    def __init__(self):
        self.threads = []  # List to store the created threads

    def create_thread(self, name, target, args=()):
        thread = MyThread(name, target=target, args=args)
        self.threads.append(thread)

    def terminate_thread(self, thread_name):  # Terminate a thread by setting its termination flag.

        for thread in self.threads:
            if thread.name == thread_name:
                thread.is_terminated = True
                break

    def run_threads(self):  # run the threads that are not terminated and haven't been executed yet.
        for thread in self.threads:
            if not thread.is_terminated and not thread.is_alive() and not thread.has_executed:
                thread.start()
                thread.has_executed = True

        for thread in self.threads:
            if not thread.is_terminated:
                thread.join()

    def simulate_execution(self):
        print("The running threads: ")
        self.run_threads()
