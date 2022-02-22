# Django_prac
> 项目内容是根据 https://docs.djangoproject.com/zh-hans/3.2 示例 demo 做的一个投票应用
## 项目目录
```shell
mysite/
    manage.py # 一个让你用各种方式管理 Django 项目的命令行工具
    mysite/
        __init__.py # 一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包
        settings.py # Django 项目的配置文件
        urls.py # Django 项目的 URL 声明，就像你网站的“目录”，可以理解成路由目录
        asgi.py # 
        wsgi.py
    polls/ #跟业务相关的：创建一个投票应用    
```

## MTV 设计模式
[关于 MTV 模式](https://blog.csdn.net/dbanote/article/details/11338953)

M: Model 负责业务对象和数据库的关系映射([ORM](https://zhuanlan.zhihu.com/p/27188788)，对象关系映射，
直白来说就是我在程序中定义一个对象就对应一个表，这个对象的一个实例即对应表中的一条记录)。

T: Template 负责如何把页面展示给用户

V: View 负责业务逻辑，视图函数的执行结果只可能有两种，返回一个可以是任何内容的 HttpResponse 对象，另一个就是 Http404 这类的异常。

### 改变模型
改变模型需要这三步：

- 编辑 models.py 文件，改变模型。
- 运行 python manage.py makemigrations 为模型的改变生成迁移文件。（通过运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 迁移。）
- 运行 python manage.py migrate 来应用数据库迁移。

数据库迁移被分解成生成和应用两个命令是为了让你能够在代码控制系统上提交迁移数据并使其能在多个应用里使用； 
这不仅仅会让开发更加简单，也给别的开发者和生产环境中的使用带来方便。

admin 123456
## Q&A
2. on_delete=models.CASCADE 什么意思
3. 如何返回 json 类型数据，而不是字符串

