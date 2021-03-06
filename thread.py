import time,threading

def loop():
    print('Thread 01 %s is running.' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s <<< %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread 02 %s ended.' % threading.current_thread().name)

if __name__ == '__main__':
    print('Thread %s is running.' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='loopThread')
    t.start()
    t.join()
    print('Thread %s end.' % threading.current_thread().name)


