# 练习实现一个类
# 它有 upsert 方法，有 delete 方法
# 它遍历所有文件夹来控制版本，升级到最新的版本

from abc import ABCMeta, abstractmethod


class BaseMigration(metaclass=ABCMeta):
    def __init__(self, target_version, file_path):
        self.target_version = target_version
        self.file_path = file_path

    @abstractmethod
    def upsert(self, file):
        # 实现对一个子文件进行 upsert
        pass
