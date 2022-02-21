# tip 本节主要介绍生成器
# 一边循环一边计算的机制即生成器 generator，实现方式是将列表生成器的 [] 换成是 ()
# tip generator 是可迭代对象，其保存的是算法

g = (x * x for x in range(10))
# print(g)
# print(next(g))
# tip 可以发现我们在遍历 g 之前已经调用过 next，它是从上次 next 之后的结果往后 next 的
print(next(g))
print(next(g))
for n in g:
    print('关于 g 中的每一个值', n)

