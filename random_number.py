# python3 生成随机数
import random

ll = []
for v in range(0, 20):
    ll.append(random.randint(0, 20))


# print(ll)


# tip python3 新增的标识参数类型和返回类型的方式
def greeting(name: str) -> str:
    return name

# print(greeting(1.1))ß
