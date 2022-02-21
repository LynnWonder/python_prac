# 任何模块代码的第一个字符串都被是否为模块的文档注释：
""" a test module to myself """

import sys


# tip 关于 python 作用域的问题：
# - 正常的函数和变量名是公开的 public,可以直接被引用，比如 abc
# __xx__ 为特殊变量，有特殊用途，一般写代码不这么定义变量，比如 __doc__  __name__
# - 注意这是一种编程习惯（可以说是一种标识）：类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如 _abc __abc
def test():
    # sys.argv 变量 它用 list 存了命令行的所有参数，其至少有一个元素，就是该 .py 文件的名称
    args = sys.argv
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print('Hello, %s~' % args[1])
    else:
        print('Too many arguments~ please try again')


# tip 当我们在命令行运行 hello 模块文件的时候， Python 解释器将一个特殊变量 __name__ 置为 __main__,
# 这段代码经常用于运行测试，导入其他模块的时候就会失败了
if __name__ == '__main__':
    test()
