from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# 使用 Python 枚举类来定义常量
class Weekday(Enum):
    Sun = "sunday"
    Mon = "monday"
    Tues = "tuesday"
    Wednes = "Wednesday"
    Thurs = "Thursday"
    Fri = "Friday"
    Sat = "Saturday"


if __name__ == "__main__":
    # value 默认是 int，从 1 开始计数
    print("get Month.Jan====>", Month.Jan.value)
    print(Weekday.Sun.value)
