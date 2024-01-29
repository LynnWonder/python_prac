from packaging import version


class MyVersion:
    """
    自定义 version，借用 Version 中的比较方式
    """

    def __init__(self, product, component, version_val):
        self.product = product
        self.component = component
        self._version = version.Version(version_val)

    def __eq__(self, other):
        if isinstance(other, MyVersion):
            return self.product == other.product and self.component == other.component \
                   and self._version.__eq__(other._version)
        return False

    # TIP If a class does not define an __eq__() method it should not define a __hash__() operation either;
    #  if it defines __eq__() but not __hash__(), its instances will not be usable as items in hashable collections.
    #  所以定义了 __eq__ 方法建议也重写一下 __hash__ 方法
    def __hash__(self):
        return hash("{}-{}-{}-{}".format(self.product, self.component, self._version.__str__()))

    def __lt__(self, other):
        return self._version.__lt__(other._version)

    # 自定义一些实例方法
    def after(self, other) -> bool:
        return self._version > other._version

    def before_equal(self, other) -> bool:
        return self._version <= other._version

    def get_version_val(self) -> str:
        return self._version.__str__()


if __name__ == "__main__":
    a = MyVersion(product="p", component="c", version_val="1.0.1")
    b = MyVersion(product="p", component="c", version_val="1.0.2")
    print(a == b)  # False
    print(a.after(b))  # False
    print(a.before_equal(b))  # True
