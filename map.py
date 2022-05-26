# tip Python 中高阶函数的概念：能接收函数作为参数的的函数
from functools import reduce

# 前面讲列表生成器的时候，我们这样来生成一个列表中每个元素的平方组成的新列表
ll = [1, 2, 3, 4]
# ll_2 = [x*x for x in ll]
# or
# ll_2 = [x * x for x in range(1, 5)]
# or
ll_2 = list((x * x for x in range(1, 5)))
print("使用列表生成式或生成器===>", ll_2)


# tip 使用 map 同样可以一行代码实现上述功能
#   注意结果是一个 Iterator，可以通过 list() 函数将整个序列计算出来并返回一个 list
def f(x):
    return x * x


ll_map = list(map(f, ll))
print("使用 map===>", ll_map)


# 关于 reduce 的用法
def fn(x, y):
    return x * 10 + y


# tip reduce 的概念就是 reduce(f, [x1, x2, x3, x4]) = f(f(f(x1,x2),x3),x4)
#   那么具体到这个例子就是 fn(fn(fn(1,2),3),4)=fn(fn(12,3),4)=fn(123,4)
ll_reduce = reduce(fn, ll)

print("使用 reduce===>", ll_reduce)


# 结合 map reduce  实现一个字符串转数字的函数
# 当然不使用 int() 函数啊
# def str2int(string):
#     # step1 每一个字符转成对应的 int
#     dicts = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#     def char2num(c):
#         return dicts[c]
#
#     # step2 列表转换成数字
#     def list2num(x, y):
#         return x * 10 + y
#
#     return reduce(list2num, list(map(char2num, string)))

# 完全使用匿名函数来完成字符串向整型的转换
def str2int(string: str) -> int:
    dicts = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    # tip reduce 和 map 一样第一个参数是一个函数，第二个参数必须是 iterable，因此直接使用 map 返回的 iterator 是完全可行的
    return reduce(lambda x, y: x * 10 + y, map(lambda x: dicts[x], string))


# 测试题
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：


def normalize(name):
    def lower(c):
        return c.lower()

    return name[0].upper() + ''.join(map(lower, name[1:len(name)]))


def prod(L):
    def multiple(x1, x2):
        return x1 * x2

    return reduce(multiple, L)


# 创建一个函数实现将一个字符串转化成浮点数 比如 '123.456' 替换为 123.456
def str2float(s):
    # 查找 . 的位置
    pos = s.find('.')
    # . 之前的字符转换成整数
    dicts = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    left = reduce(lambda x, y: x * 10 + y, map(lambda z: dicts[z], s[0:pos]))
    right = reduce(lambda x, y: x * 0.1 + y, map(lambda z: dicts[z], reversed(s[pos + 1:])))
    return left + right * 0.1


if __name__ == '__main__':
    print('str2int=====>', str2int('1234'), str2int('300'), isinstance(str2int('300'), int))

    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
    print(str2float('123.456'))

    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')
