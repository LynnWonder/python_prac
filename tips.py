# 本文件涉及 Python3 一些语法提示
# 表示 Python 中的最大数
import sys

max_val = float('inf')
max_val1 = sys.maxsize

# 仅排序数组中的某一个部分
ll = [7, 4, 6, 5, 1, 3, 6]
ll[0:3] = sorted(ll[0:3])

# 填充数组
ll1 = [1]*5
if __name__ == "__main__":
    print(max_val)
    print(max_val1 < max_val)
    print(ll)
    print(ll1)
