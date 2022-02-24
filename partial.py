# tip 本节介绍 python 中的偏函数

import functools

# tip 注意接收对象是 函数对象、*args和**kw这3个参数
in2 = functools.partial(int, base=2)

print(in2('10000'))
