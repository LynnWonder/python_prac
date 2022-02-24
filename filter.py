from collections.abc import Iterator

sss = "testssss"
ss2 = '0123456789'
print(ss2[::-1])

# tip python 实现字符串翻转的方式
# str[::-1]
# ''.join(reversed(str))

ll = [1, 2, 3]
print(list(reversed(ll)))
# tip 由此可见 reversed 函数返回的值是一个 Iterator
print(isinstance(reversed(ll), Iterator))


def is_palindrome(n):
    return str(n) == str(n)[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
