import threading

local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello,%s,(in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Anki',), name=('Thread-A'))
t1.start()
t1.join()