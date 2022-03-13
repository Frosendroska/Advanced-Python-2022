import time
from multiprocessing import Process
from threading import Thread
import os
from fib import first_n_fib

RECURSION_LEN = 100
TESTS_NUMBER = 10


def small_test(N):
    start = time.time()
    for _ in range(TESTS_NUMBER):
        first_n_fib(N)
    sync_time = time.time() - start

    start = time.time()
    threads = [Thread(target=first_n_fib, args=(TESTS_NUMBER,)) for _ in range(TESTS_NUMBER)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    threads_time = time.time() - start

    start = time.time()
    threads = [Process(target=first_n_fib, args=(TESTS_NUMBER,)) for _ in range(TESTS_NUMBER)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    process_time = time.time() - start
    return [sync_time, threads_time, process_time]


def write_to_file(results, file):
    file.write("Synchronous time:\t" + str(results[0]) + '\n')
    file.write("Threads time:\t\t" + str(results[1]) + '\n')
    file.write("Process time:\t\t" + str(results[2]) + '\n')
    file.write(">\n")
    file.write("The fastest:\t\t" + str(min(results[0], results[1], results[2])) + '\n')
    file.write("The slowest:\t\t" + str(max(results[0], results[1], results[2])) + '\n')
    file.write("\n------------------------------------------\n\n")


def easy_task():
    print("Comparing time...")
    small = small_test(RECURSION_LEN)
    medium = small_test(RECURSION_LEN * 100)
    big = small_test(RECURSION_LEN * 1000)

    if not os.path.exists("artifacts"):
        os.mkdir("artifacts")

    with open("artifacts/easy.txt", "w") as file:
        print("\tSmall...")
        write_to_file(small, file)
        print("\tMedium...")
        write_to_file(medium, file)
        print("\tBig...")
        write_to_file(big, file)
    print("------ DONE ------")