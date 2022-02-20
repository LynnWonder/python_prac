# tip 函数调用越多，就会导致栈溢出
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 使用尾递归做优化，循环就是一种特殊的尾递归函数，函数返回的时候调用自身本身，并且不包含表达式
# 这样编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次都只占用一个栈帧，不会溢出
# 实际上 Python 标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题
def opt_fact(n, res):
    if n == 1:
        return res
    return opt_fact(n - 1, n * res)


# tip 汉诺塔问题是经典的递归问题，最终可以总结成三个步骤
# 具体问题和分析方法可以参考我的博客 https://blog.csdn.net/lynnwonder6/article/details/104007317
# 将 n-1 个盘子借助 C 从 A 移动到 B 上
# 将最后一个盘子从 A 移动到 C 上
# 将 n-1 个盘子借助 A, 从 B 移动到 C 上
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


# print(fact(5))
# 栈溢出
# print(fact(1000))
# print(opt_fact(100, 1))
move(3, 'A', 'B', 'C')
