# 首先通过函数实现一个菲波那切数列 1 1 2 3 5 8...
def fib(param):
    # 定义三个值
    n, first, current = 0, 0, 1
    res = []
    while n < param:
        res.append(current)
        # tmp = first
        # first = current
        # current = tmp + current
        # 上面写的一坨代码可以直接转换成如下 tip python 的元素交换太好用了
        first, current = current, first + current
        n = n + 1
    return res


# 下面我们将 fib 改造成一个 generator
def fib0(param):
    n, first, current = 0, 0, 1
    while n < param:
        yield current
        first, current = current, first + current
        n = n + 1
    return 'done'


print(fib(6))

for n in fib0(6):
    print(n)
# 我想使用 fib0 直接生成一个列表
print("使用 fib0 得到的数据：", [x for x in fib0(6)])

# 如何拿到 generator 的 return 语句的返回值
# 一定要将 generator 赋予到另一个对象后再使用 next, 否则每次都会新建一个 generator
g = fib0(6)
while True:
    try:
        x = next(g)
    except StopIteration as e:
        print('Generator return value', e.value)
        break
