from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def write(q):
    print('写数据进程： %s' % os.getpid())
    for v in ['A', 'B', 'C']:
        print('put %s to queue...' % v)
        q.put(v)
        time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    print('读数据进程：%s' % os.getpid())
    while True:
        v = q.get(True)
        print('get %s from queue.' % v)


# 子进程要执行的代码
def run_proc(name):
    print('正在运行子进程 %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    # TIP 这里是使用 multiprocessing 能够跨平台使用（即使是 windows）
    # print('正在运行父进程 %s.' % os.getpid())
    # p = Process(target=run_proc, args=('test',))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')

    # 进程间通信学习
    # TIP python 进程间通信是通过 Queue Pipes 等实现的
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程 pw 写入
    pw.start()
    # 启动子进程 pr 读取
    pr.start()
    # 等待 pw 结束
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()
