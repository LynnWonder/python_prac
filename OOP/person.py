class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print("===get_name===", self.name)


class Student(Person):
    def get_name(self):
        print("===student_get_name===", self.name)

    # TIP: @property 将一个属性变成可读属性
    @property
    def gender(self):
        return self.gender

    # TIP: @${property}.setter 将为属性赋值
    @gender.setter
    def gender(self, g):
        if g == "male":
            self.gender = "male"
        elif g == "female":
            self.gender = "female"
        else:
            raise Exception("Invalid gender")


if __name__ == "__main__":
    s = Student("s", 0)
    # 报错，当只有 @property 而没有 setter 时该变量将变成只读变量
    # s.gender = "bi"
