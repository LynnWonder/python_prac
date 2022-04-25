import threading
import asyncio


# TIP 异步编程的不同实现方式：
#  我们为什么需要多线程或者多进程：
#  在 IO 操作中，当前线程被挂起，其他需要 CPU 执行的代码就没办法执行了，因此我们使用多线程或者多进程来并发执行代码
# TIP 使用异步 IO 的目的
#  因为系统不能无限的增加线程，切换线程的开销也很大。所以使用多线程或者多进程只是解决 CPU 高速执行能力和 IO 设备的龟速严重不匹配问题的方法之一
#  另一种方法就是使用异步 IO

async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(10)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# TIP asyncio 提供了完善的异步 IO 支持
#  使用 asyncio 结合协程可以让两个任务并发执行
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
