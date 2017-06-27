import multiprocessing

# def worker(num):
#     print('Worker:',num)
#
# if __name__=='__name__':
#     jobs = []
#     for i in range(5):
#         p = multiprocessing.Process(target=worker,args=(i,))
#         jobs.append(p)
#         p.start()

def process(num):
    print('Process:%s' % num)

if __name__=='__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()