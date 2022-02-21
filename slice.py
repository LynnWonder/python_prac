ll = []
n = 0
# while n < 20:
#     ll.append(n)
#     n = n + 2
for v in range(0, 20, 2):
    ll.append(v)

print(ll)

# 切片使用
print("ll 切片", ll[0:3])
print("切片后的 ll", ll)


# def trim(s):
#     # return s.strip()
#     ll = list(s)
#     tmp = len(ll) - 1
#     start = 0
#     end = 0
#     for val in ll:
#         if val == ' ':
#             start += 1
#         else:
#             break
#     while tmp > 0:
#         if ll[tmp] == ' ':
#             end += 1
#             tmp -= 1
#         else:
#             break
#
#     res1 = s[start:]
#     if end > 0:
#         return res1[:len(res1) - end]
#     else:
#         return res1


# 经典的使用递归来进行字符串 trim 问题
def trim(s):
    if s == '':
        return s
    elif s[0].isspace():
        return trim(s[1:])
    elif s[-1].isspace():
        # tip 使用负数可以获取从开始到倒数第 x 个元素
        return trim(s[:-1])
    else:
        return s


print(trim('hello   '))
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
