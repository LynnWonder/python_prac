# tip 这一节是关于 Python 的类，Python允许对实例变量绑定任何数据，
#  也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
# (object)表示继承于 object
# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def get_grade(self):
#         if self.__score >= 90:
#             return 'excellent'
#         # Python 简直不像编程语言
#         elif 80 < self.__score < 90:
#             return 'good'
#         else:
#             return 'nice'
#
#     def set_score(self, score):
#         self.__score = score
#         print('修改后的 score', self.__score)
#
#
# Jerry = Student('Jerry', 90)
#
# # print(Jerry.__name)
# # Jerry.__name = 'test'
# # tip 当属性前面添加 __ 后，它就变成了一个私有变量，只能在内部访问，不能在外部访问
# # print("修改后的 jerry name", Jerry.__name)
# print(Jerry.get_grade())
# Jerry.set_score(100)


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender != 'male' and gender != 'female':
            return
        else:
            self.__gender = gender


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
