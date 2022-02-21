# python_prac

## 类型
- 字符串
  - 字符串换行 '''...'''
  - Python3 中字符串以 Unicode 编码，一个字符对应若干个字节，如果要在网络中传输，或者保存在磁盘上，那么就需要把 str 变成以字节为单位的 `bytes` 类型
  - 字符串格式化
    - `%` 运算符是用来格式化字符串的，字符串内部 `%s` 表示用字符串替换，如果只有一个 `%?`, 那么字符串外部的括号可以省略
      - '%2d-%02d' % (3,1)   即为 `' 3-01'` 
      - '%.2f' % 3.1415 即为 `'3.14'` 
    - format()
      - 'hello, {0}, its me {1}, im {2:.2f}%'.format('test', 'test1', 3.1415)
    - f-string
      - pi = 3.1415 f'hello its me {pi:.2f}'
- 数据类型
- 字典 dict: key 必须是不可变对象
  - 查找和插入的速度极快，不会随着 key 的增加而变慢，而 list 类型随着元素的增加查找和插入的时间会变慢
  - 需要占用大量的内存，内存浪费多，这和 list 类型相反
- 类型转换
  - 字符串转整数 int(str),注意当它发现字符串不是一个合法的数字的时候，程序就会退出了
  - float()
  - str()
- 数据类型检
  - isinstance() 检查

## 其他

### 不可变对象
在 Python 中字符串、整数等式不可变的，因此可以放心作为 dict set 的 key，而像 list 就是可变的，也就是 unhashable type

需要注意的是：

不可变对象而言，调用对象自身的任意方法，都不会改变对象自身的内容，相反这些方法会创建新的对象并返回，这样就保证了不可变对象本身永远不可变。


## Q&A
1. python 中是否区分基本数据类型和引用数据类型
2. 什么是 Python 解释器，为什么需要 docker
3. python 中没有 ++ 或者 -- 这种操作吗


## 知识
计算机内存中，统一使用 Unicode 编码，当需要保存到硬盘或者需要传输的时候就会转换为 UTF-8 编码。

- ASCII 编码只能表示英语，只使用一个字节
- Unicode 编码将所有语言统一到一套编码中，从此再也不会出现不同语言（主要是非英语）乱码的问题了
  - 无论是汉字还是英语，通常是两个字节
- UTF-8 是可变长编码，本着节约 Unicode 浪费的空间的思想
  - 常用的英文字幕是 1 个字节，汉字通常是 3 个字节

## todo
1. 关于 hashtable  https://www.liaoxuefeng.com/wiki/1016959663602400/1017104324028448#0