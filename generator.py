# tip 本节主要介绍生成器
# 一边循环一边计算的机制即生成器 generator，实现方式是将列表生成器的 [] 换成是 ()
# tip generator 是可迭代对象，其保存的是算法

g = (x * x for x in range(10))
# print(g)
# print(next(g))
# tip 可以发现我们在遍历 g 之前已经调用过 next，它是从上次 next 之后的结果往后 next 的
# print(next(g))
# print(next(g))
# for n in g:
#     print('关于 g 中的每一个值', n)


# 利用 generator 实现了 Python 对协程的支持
# TIP 协程：coroutine
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # 启动 generator
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
