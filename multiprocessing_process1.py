from multiprocessing import Process
import os

#print('Process %s start' % os.getppid())

#Only works on Unix/Mac/Linux/:
#pid=os.fork()
#if pid==0:
#    print('child process:%s,parent process:%s'%(os.getpid(),os.getppid()))
#else:
#    print('.......'%(os.getpid(),pid))

def run_proc(name):
    print('Run child process %s,%s' % (name, os.getpid()))

if __name__ == '__main__':
    #run_proc()
    print('Parent process %s.' % os.getppid())
    p = Process(target=run_proc, args=('test',))  # to create a child process
    print('Child process will start.')
    p.start()      #to start the child process
    p.join()       #to execute parent process after finishing the child process
    print('Child process end.')
