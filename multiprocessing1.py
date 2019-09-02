from multiprocessing import Pool, Process, Queue
import os, time, random, subprocess


def process(num):
    print('Process:%s' % num)


def main_process():
    for i in range(5):
        p = Process(target=process, args=(i,))
        p.start()


def run_proc(name):
    print('Run child process %s,%s' % (name, os.getpid()))


def main_run_proc():
    print('Parent process %s.' % os.getppid())
    p = Process(target=run_proc, args=('test',))  # to create a child process
    print('Child process will start.')
    p.start()  # to start the child process
    p.join()  # to execute parent process after finishing the child process
    print('Child process end.')


def long_time_task(name):
    print('Run task %s,%s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def main_long_time_task():
    print('Parent process %s.' % os.getpid())
    # p = Pool()
    with Pool() as p:
        for i in range(5):
            p.apply_async(long_time_task, args=(i,))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')


# print('$ nslookup www.python.org')
# r = subprocess.call(['nlookup', 'www.python.org'])
# print('Exit code:', r)
def write(q):
    print('Process to write:%s' % os.getpid())
    for v in list('ABC'):
        print('Put {} to queue...'.format(v))
        q.put(v)
        time.sleep(random.random())


def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        v = q.get(True)
        print('Get {} from queue.'.format(v))


def main_multiprocess_communicate():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


if __name__ == '__main__':
    # main_run_proc()
    # main_long_time_task()
    main_multiprocess_communicate()
    pass
