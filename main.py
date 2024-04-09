"""
Hazar Michael 1201838
Mona Dweikat 1200277
Abdalrahim Thiab  1202102
"""


from ThreadManager import ThreadManager
from MyThread import my_thread_function
from MySemaphore import Semaphore


def main():
    thread_manager = ThreadManager()
    semaphore = Semaphore(1)

    while True:
        print("1. Create Thread")
        print("2. Terminate Thread")
        print("3. Run Threads")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter thread name: ")

            while True:
                try:  # Invalid entry point function handling
                    entry_point = input("Enter the entry point function: ")
                    target = globals().get(entry_point)
                    if target is None or not callable(target):
                        raise ValueError("Invalid entry point function!")
                    break
                except ValueError as ve:
                    print(ve)

            try:  # Error creating thread handling
                thread_manager.create_thread(name, target, args=(semaphore,))
            except Exception as e:
                print(f"Error creating thread: {str(e)}")

        elif choice == "2":
            thread_name = input("Enter thread name to terminate: ")
            try:  # Error terminating thread handling

                thread_manager.terminate_thread(thread_name)
            except Exception as e:
                print(f"Error terminating thread: {str(e)}")

        elif choice == "3":
            try:  # Error running threads handling
                thread_manager.simulate_execution()
            except Exception as e:
                print(f"Error running threads: {str(e)}")

        elif choice == "4":
            break

        print()

    print("Exiting...")


if __name__ == "__main__":
    main()
