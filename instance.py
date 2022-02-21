class Student(object):
    # tip 这是一个类属性，区别于隶属于具体实例的实例属性比如 name，类属性隶属于类，所有实例共享一个属性
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')