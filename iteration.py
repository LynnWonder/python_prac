# tip Python 中只要是一个可迭代对象，那么 for 循环就可以使用, list/tuple/dict/set/str 都是可迭代对象
# tip 可以被 next() 函数调用不断返回下一个值的对象都是迭代器 iterator
# tip 判断一个对象是不是可迭代对象
# 可以发现字符串、数组都是可迭代对象
from collections.abc import Iterable
from collections.abc import Iterator
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
print("迭代器判断", (x for x in range(10)), isinstance((x for x in range(10)), Iterator))

d = {'a': 1, 'b': 2, 'c': 3}


# for key in d:
# print('key is ===>', key)

# for x, y in [(1, 1), (2, 4), (3, 9)]:
# print('测试两个变量的输出', x, y)


def findMinAndMax(L):
    # 先使用最简单的遍历方式实现最大值和最小值查找
    if len(L) == 0:
        return None, None
    else:
        min_one = L[0]
        max_one = L[0]
        for val in L:
            if min_one > val:
                min_one = val
            if max_one < val:
                max_one = val
        return min_one, max_one


print(findMinAndMax([7]))
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
