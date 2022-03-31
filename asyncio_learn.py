import threading
import asyncio


async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# TIP asyncio 提供了完善的异步 IO 支持
#  使用 asyncio 结合协程可以让两个任务并发执行
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
