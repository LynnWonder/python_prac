# tip 这一节介绍判断对象类型的几种方式
import types

# tip type 基本上可以判断大部分对象的类型，除了 class 的类型不太方便一般都是用 isinstance
#   因此一般优先使用 isinstance

print(type('abc') == str)


def func():
    pass


print(type(func) == types.FunctionType)


# tip 使用 dir

class MyObject(object):
    def __init__(self):
        self.x = 9


obj = MyObject()
print("是否有属性 x==>", hasattr(obj, 'x'))
print("获取属性 x==>", getattr(obj, 'x'))
print("设置属性 x==>", setattr(obj, 'y', 10))
print("获取属性 y==>", getattr(obj, 'y'))
print("获取属性 z==>", getattr(obj, 'z'))
