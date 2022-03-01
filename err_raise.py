# error reraise
import logging


# tip
#  高级语言都内置了 try...except...finally... 的错误处理机制，Python 也不例外
#  当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
#  如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
#  执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    # 可以使用 except 来处理不同类型的错误
    except ValueError as e:
        print('there is a ValueError')
        # raise
        # logging 模块可以很清晰的记录错误信息
        logging.exception(e)
    finally:
        print('finally')


# bar()


# 练习题 https://www.liaoxuefeng.com/wiki/1016959663602400/1017598873256736

from functools import reduce


def str2num(s):
    # tip 这就是 python 中三目运算符的用法
    # return int(s) if s.find('.') == -1 else float(s)
    # 或者直接改成用 float(s)
    return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
