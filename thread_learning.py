# TIP 多任务可以由多进程完成，也可以由一个进程内的多线程完成
#  一个进程至少有一个线程，线程是操作系统直接支持的执行单元
#  多进程中同一个变量各自拷贝一份存在每个进程中互不影响
#  多线程中所有变量都由所有线程共享
#  同时需要注意：python 不能利用多线程实现多核任务，但是可以通过多进程实现多核任务。
#          多个 python 进程有各自独立的 GIL 锁，互不影响

import time, threading


# 新线程执行的代码
def loop():
    print('新 thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

# 任何进程默认启动一个线程，即主线程
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
# TIP t.join() 会阻塞线程 t 直到 t 终结，有点类似于 await 的含义
t.join()
#  TIP 没有 t.join() 的时候会一开始就执行下面这段代码
print('thread %s finished...' % threading.current_thread().name)
