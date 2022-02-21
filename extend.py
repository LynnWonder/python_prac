class Animal(object):
    def __init__(self, name):
        self.__name = name
        pass

    def run(self):
        print("Animal is running")
        return


class Dog(Animal):
    def run(self):
        print("Dog is running")
        return


class Cat(Animal):
    def run(self):
        print("Cat is running")
        return


def run_twice(animal):
    animal.run()


huskey = Dog('huskey')
# huskey.run()
# tip 可以发现只要我们传入一个 Animal 类型，run_twice 都会调用 run() 方法，
#  也就是说，调用方只管调用，不管细节，新增一种 Animal 子类时，只要确保 run() 方法编写正确，不用管原来的代码是如何调用的
#  开闭原则： 对扩展开放，允许新增 Animal 子类
#  对修改关闭：不需要修改依赖 Animal 类型的 run_twice 等函数
run_twice(huskey)
black = Cat('black')
# black.run()
run_twice(black)
# 可以用 isinstance 来判断类型
print(isinstance(huskey, Animal))
print(isinstance(huskey, Dog))

# tip Python 是动态语言，因此拥有动态语言的'鸭子类型'， 也就是不要求严格的继承体系，一个对象只要看起来像鸭子那就是鸭子
#  "file-like object" 就是一种鸭子类型，只要有 read() 方法或者说给函数传入的对象是一个实现了 read() 方法的对象
#  那么就能使用，动态语言的鸭子类型特点决定了继承并不像静态语言那么必须。

