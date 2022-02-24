# 在 Python 中装饰器亦是一个高阶函数
import time, functools


def log(func):
    # 添加这步，防止被装饰的函数失去原名字
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():', func.__name__)
        return func(*args, **kw)

    return wrapper


# 相当于执行了 now = log(now) = wrapper()
@log
def now():
    return 'test'


now()
# 我们发现 now 函数的名字变成了 wrapper，此时添加一句 @functools.wraps(func) 防止丢失正确的名字
print(now.__name__)


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        res = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return res
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
print('====>', f, s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
