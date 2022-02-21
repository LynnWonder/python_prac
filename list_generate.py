# tip 本节关于 「列表生成式」
# 生成 [A,B,C] 和 [a,b,c] 随机组合形成的字符串
print([m + n for m in ["A", "B", "C"] for n in ["a", "b", "c"]])

# python 简直太智能了
# 打印 1-10 的数的平方组成的列表
print([x * x for x in range(1, 11)])
# 打印 1-10 中的偶数的平方组成的列表
# tip 列表生成式可以使用 if 但在 for 后面 不能 if else 同时使用
# 在 for 前面必须 if else 同时使用
print([x * x for x in range(1, 11) if x % 2 == 0])

print([x if x % 2 == 0 else -x for x in range(1, 11)])

L1 = ['Hello', 'World', 18, 'Apple', None]

# print([x if !isinstance(x, str) else x.lower() for x in range(1,10)])
# L2 = [x if not isinstance(x, str) else x.lower() for x in L1]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)
