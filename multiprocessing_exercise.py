# from multiprocessing import Process
import multiprocessing

def process(num):
    print('Process:%s' % num)

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()