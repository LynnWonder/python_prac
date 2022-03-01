# object relational mapping 即对象关系映射，就是把关系数据库中的一行映射为一个对象，也就是一个类对应一个表，这样写代码很简单，不用直接操作 sql 语句。
# 要编写一个 ORM 框架，所有类都只能动态定义，这时候就用到了元类

# Field 类 负责保存数据库表的字段名和字段类型
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        # 使用父类的方法来初始化
        super(IntegerField, self).__init__(name, 'bigint')


# tip
#  metaclass 可以用来控制类的创建行为
#  因为 metaclass 是类的模板，所以必须从 type 类型派生
#  ModelMetaclass 做了如下几个事情：
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        # tip 1.在当前类中查找定义的类的所有属性，就把它保存到一个__mappings__的dict中，
        #  同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        # tip 2. 将表名保存在 __table__ 中，假设表名和类名一致
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


# tip 当传入关键字参数metaclass时，表示创建 model 的时候要通过 ModelMetaclass.__new__() 来创建
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
