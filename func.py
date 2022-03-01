import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("not suggested type")
    if x < 0:
        return -x
    else:
        return x


# tip 看起来像是返回多个值了, 其实返回的只是一个 tuple 值
# tip 定义默认参数的方式其实和 JavaScript 一样
# tip 默认参数必须指向不变对象，否则将会出现非预期的现象
def move(x, y, step=0, angle=0):
    return x * y, x / y


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


def quadratic(a, b, c):
    # 没有进行参数类型检查
    for v in (a, b, c):
        if not isinstance(v, (int, float)):
            raise TypeError
    # 说明开平方根为 0 的情况
    if math.pow(b, 2) - 4 * a * c < 0:
        raise ValueError("无实数解")
    res_temp1: float = -b + math.sqrt(math.pow(b, 2) - 4 * a * c)
    res_temp2: float = -b - math.sqrt(math.pow(b, 2) - 4 * a * c)
    return res_temp1 / (2 * a), res_temp2 / (2 * a)


# tip * 标识后面这个值是一个可变参数
def calc(*numbers):
    sum_res = 0
    for n in numbers:
        sum_res = sum_res + n
    return sum_res


# tip ** 标识关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other 关键字参数', kw)


# tip: 命名关键字，* 后的参数被视为命名关键字参数（* 为特殊分隔符，必须有，否则将会被视为位置参数）
# tip 命名关键字参数在调用时必须传入参数名，否则将会报错
def person_name(name, age, *, city, job):
    print('命名关键字===>', name, age, city, job)


# tip 混合参数组合：必选参数-默认参数-可选参数-命名关键字参数-关键字参数 必须是这样的顺序
def f1(a, b=0, *args, **kw):
    print("混合参数组合：必选参数-默认参数-可选参数-命名关键字参数-关键字参数", a, b, args, kw)


def f2(a, b=0, *, d, **kw):
    print("混合参数a=", a, "b=", b, "d=", d, "kw=", kw)


# 测试多个数的乘积

def mul(*kw):
    if len(kw) < 1:
        raise TypeError
    res = 1
    for v in kw:
        res = res * v
    return res


# print(my_abs(100))
# print(isinstance(10, int))
# print(move(10, 12))

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

tuple_var = [1, 2, 3]
print("可变参数函数测试===>", calc(1, 2, 3))
# tip python 允许在 list 或 tuple 前面加一个 * 号，让其变成可变参数传进去
print(calc(*tuple_var))
# 创造参数错误和无解的情况
# print(quadratic("test", 1, 1))
# print(quadratic(1, 1, 1))

print(add_end())
print(add_end())

extra = {'city': 'Beijing', 'job': 'cat'}
# **extra 标识下，kw 将获得一个 dict,
# tip 注意 kw 获得的 dict 是 extra 的一份拷贝，对 kw 的拷贝不会影响到函数外的 extra
person('Tom', 2, **extra)
# 这也是使用关键字参数的一种方式
person('Jerry', 1, city='Beijing', job='mouse')
person_name('Jerry', 1, city='Beijing', job='mouse')
# 这是不被允许的
# person_name('Jerry', 1, city='Beijing')

f2(1, 2, d=99, ext=None)
# 没有传入 b，则默认为 0
f2(1, d=99, ext=None)
# print('mul(0) =', mul())
print('mul(5) =', mul(5))


# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))


def zzz(x, y):
    print("输出一个值====>", x)
    return x / y


# tip 通过这里可以发现即便是没有标明命名参数
zzz(y=1, x=10)
