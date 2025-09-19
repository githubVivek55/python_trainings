# write multi threading code here
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1) 


def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)

def print_letters2():
    for letter in ['a','b','c','d','e']:
        print(f"letter: {letter}")
        time.sleep(1)


def executorExample():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(print_numbers)
        future2 = executor.submit(print_letters)
        future3 = executor.submit(print_letters2)


if __name__ == "__main__":
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)
    thread3 = threading.Thread(target=print_letters2)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("Finished both threads")

    print("Thread pool executor")
    executorExample()