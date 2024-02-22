ll = [1, 8, 4, 8, 2]
# 正序排列
print(sorted(ll))
# 逆序排列
print(sorted(ll, reverse=True))


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


# 使用 sorted 函数按照名字排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L2 = sorted(L, key=by_name)
# print("=====>L2", L2)
L2 = sorted(L, key=by_score)

# 使用列表的 sort 方法直接进行排序
L.sort(key=by_score)
print("=====>L", L)
print("=====>L2", L2)


# Python 中的闭包相关内容

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print("====>闭包")
# tip 可以发现下面返回的内容一样都是 9，是不是很像 JavaScript 中的闭包呢，原因也一样都是
#   返回函数不会立即执行，三个函数都返回的时候，引用的变量 i 都变成了 3
print(f1())
print(f2())
print(f3())


# 解决上述问题的方式如下
def count1():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        # 因为被立即执行，因此能够避免出现上述的现象
        fs.append(f(i))
    return fs


print('=====>解决闭包带来的问题')
f11, f21, f31 = count1()
print(f11())
print(f21())
print(f31())


# 使用匿名函数对以下函数做改造
def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print("====>匿名函数", L)
