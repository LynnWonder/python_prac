# 由于 python 中类的属性可以直接暴露出去，这就导致了一个属性可能会被随意更改掉
# 因此为了实现属性可以校验又同时保证这个属性可以方便地修改，python 提供了 @property

class Student(object):

    # def get_score(self):
    #     return self._score
    #
    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('score must be an integer')
    #     if value < 0 or value > 150:
    #         raise ValueError('score must between 0 and 150')
    #     self._score = value

    # property 将 score 直接变成了一个属性
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score value must be an integer')
        if value < 0 or value > 150:
            raise ValueError('score must be between 0 and 150')
        self._score = value


# 这种方式不失为一种校验属性的方式，但这种方式比较笨重
s = Student()
# s.set_score(130)
# 现在我们直接赋值
s._score = 140
print(s._score)


# 这样赋值的话就会报错
# s.score=-10


# 好的，下面我们做一道题来练习一下 @property
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
