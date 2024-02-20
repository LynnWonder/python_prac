"""
需求：实现一个迁移功能，能对大盘、告警规则这两类数据进行注册（增）、升级（增、删、改）操作
比如 Django 使用的是维护 migrations 文件，在其中对数据表进行操作
再比如 golang-migrate 通过顺序执行迁移文件实现对数据库的更改，因此我们可以通过定义 migration 文件来实现功能
拆解需求点：
1. 顺序执行 migration 文件，
2. 文件内容：根据文件名称执行对应的操作（规范文件名）此时一个文件中内容是规范好的，或在一个文件中

大盘的增删改和告警规则的增删改不一样，但又都有类似的结构，所以我们可以创建一个抽象基类，抽象方法主要是 upsert 和 delete
普通方法是：执行动作
"""

from abc import ABC, abstractmethod
import os


class BaseMigration(ABC):
    def __init__(self, path):
        self.root_path = path
        pass

    @abstractmethod
    def upsert(self):
        """
        新增和更新操作
        """
        pass

    @abstractmethod
    def delete(self):
        """
        删除操作
        """
        pass

    def execute(self):
        """
        遍历 root_path 根据文件名不同执行不同的操作
        """
        for path, dir_list, file_list in os.walk(self.root_path):
            for file in file_list:
                if 'U' in file:
                    self.upsert(os.path.join(path, file))
                elif 'D' in file:
                    self.delete(os.path.join(path, file))


class DashboardMigration(BaseMigration):
    def upsert(self, path):
        print('===>dashboard upsert')

    def delete(self, path):
        print('===>dashboard delete')


class RuleMigration(BaseMigration):
    def upsert(self, path):
        print('===>rule upsert')

    def delete(self, path):
        print('===>rule delete')


class Migrate:
    def __init__(self, path):
        self.dir = path

    def run(self):
        # 扩展性差，如果新增了一个别的 migration 该怎么弄？
        for filepath, dirnames, filenames in os.walk(self.dir):
            for dirname in dirnames:
                if 'dashboard' in dirname:
                    d = DashboardMigration(os.path.join(filepath, dirname))
                    d.execute()
                elif 'rule' in dirname:
                    r = RuleMigration(os.path.join(filepath, dirname))
                    r.execute()


if __name__ == '__main__':
    m = Migrate('./test_migrate')
    m.run()
