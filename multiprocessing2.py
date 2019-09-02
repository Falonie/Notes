from multiprocessing import Pool, Process, Queue
import os, time, random, subprocess


def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item)
    print("Consumer done.")


def producer(sequence, q):
    for item in sequence:
        q.put(item)


def multiprocess_communicate():
    q = Queue()
    cons_p = Process(target=consumer, args=(q,))
    cons_p.start()
    sequence = list(range(5))
    producer(sequence, q)
    q.put(None)
    cons_p.join()

multiprocess_communicate()