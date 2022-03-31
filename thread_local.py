import threading
# TIP 为了解决线程数据共用的问题我们可以使用锁，不然就使用局部变量，但局部变量在数据传递时并不方便
#   因此 ThreadLocal 应运而生，它可以理解为一个全局 dict，每个线程只能读写当前线程自己的独立副本（自己的 key 对应的 value）
#   解决了参数在一个线程中各个函数之间互相传递的问题
# 创建全局ThreadLocal对象:
local_school = threading.local()


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
