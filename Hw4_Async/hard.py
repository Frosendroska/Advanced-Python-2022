import codecs
from datetime import datetime
import multiprocessing
import queue
import time


def process_A(input_queue: multiprocessing.Queue,
              output_queue: multiprocessing.Queue):
    while True:
        try:
            msg = input_queue.get_nowait()
            # Apply .lower() and sent to B
            output_queue.put(msg.lower())
        except queue.Empty:
            pass
        time.sleep(5)


def process_B(input_queue: multiprocessing.Queue,
              output_queue: multiprocessing.Queue):
    while True:
        try:
            msg = input_queue.get_nowait()
            # Sent to MAIN
            output_queue.put(codecs.encode(msg, "rot_13"))
        except queue.Empty:
            pass
        time.sleep(5)


def hard_task():
    main_A = multiprocessing.Queue()
    A_B = multiprocessing.Queue()
    B_main = multiprocessing.Queue()

    multiprocessing.Process(target=process_A, args=(main_A, A_B), daemon=True).start()
    multiprocessing.Process(target=process_B, args=(A_B, B_main), daemon=True).start()

    while True:
        main_A.put(input(datetime.now().strftime("%H:%M:%S") + "> "))
        res = B_main.get()
        print(datetime.now().strftime("%H:%M:%S") + ">", res)
