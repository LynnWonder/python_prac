# 解决多线程数据共享导致的变量修改混乱的问题

import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(2000000):
        # TIP 当多个线程同时执行 lock.acquire() 时，
        #  只有一个线程能成功地获取锁，然后继续执行代码，
        #  其他线程就继续等待直到获得锁为止
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
