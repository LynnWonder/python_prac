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
import re
from abc import ABC, abstractmethod
import os
from enum import Enum


class Operation(Enum):
    UPSERT = "upsert"
    DELETE = "delete"


class Action:
    def __init__(self, op, path):
        self.op = op
        self.filepath = path


class FileNameParser:
    def __init__(self, name):
        self.filename = name
        self.op = None
        self.index = 0
        # 可以在构造函数中执行本类的方法
        self.parse(name)

    def __lt__(self, other):
        return self.index < other.index

    def parse(self, name):
        regex = r'^([0-9]+)([U|D]){1}_[0-9a-zA-Z_]+\.json$'
        res = re.match(regex, name)
        try:
            self.index = int(res.group(1))
            if res.group(2) == "U":
                self.op = Operation.UPSERT.value
            elif res.group(2) == "D":
                self.op = Operation.DELETE.value
        except Exception as e:
            raise Exception("filename {} is invalid! error {}".format(name, e))


class BaseMigration(ABC):
    def __init__(self, dirname):
        self.base_dir = None
        self.migrate_dir = dirname
        self.switch = {
            Operation.UPSERT.value: self.upsert,
            Operation.DELETE.value: self.delete,
        }

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

    # 通过这种方式将 base_dir 传进来，实例化 Migration 的时候并不知道 base_dir,
    # 只有在使用 Migrate 框架的时候才知道
    def base_info(self, base_dir):
        self.base_dir = base_dir

    def get_actions(self) -> [Action]:
        actions = []
        for path, dir_list, file_list in os.walk(os.path.join(self.base_dir, self.migrate_dir)):
            file_names = []
            for file in file_list:
                try:
                    fileParser = FileNameParser(file)
                    file_names.append(fileParser)
                except Exception as e:
                    raise e
            # 对 file 按照名称排序
            file_names.sort()
            for file in file_names:
                filepath = os.path.join(path, file.filename)
                action = Action(file.op, filepath)
                actions.append(action)
        return actions

    def execute(self):
        """
        遍历 root_path 根据文件名不同执行不同的操作
        可以通过区分文件名称来指向对应的操作，但如果想扩展就又要写 elif
        因此通过收取所有 action 的方式，每个 action 对应 upsert 或 delete 方法
        """
        actions = self.get_actions()
        for a in actions:
            func = self.switch.get(a.op, None)
            if func:
                func(a.filepath)
            else:
                # todo add log
                pass


class DashboardMigration(BaseMigration):
    def upsert(self, path):
        print(f'===>dashboard {path} upsert')

    def delete(self, path):
        print(f'===>dashboard {path} delete')


class RuleMigration(BaseMigration):
    def upsert(self, path):
        print(f'===>rule {path} upsert')

    def delete(self, path):
        print(f'===>rule {path} delete')


class Migrate:
    def __init__(self, dirname):
        self.dir = dirname
        # 保存所有有必要执行的 migration 实例
        self.migrations = []

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

    # tip 针对扩展性差的问题，通过每写一类 migration 都向 Migrate 注册的方式
    #   同时通过在每个 migration 中自行定义对应的文件夹（路径）名称来避免 hardcode
    def register_migration(self, migration: BaseMigration):
        migration.base_info(self.dir)
        self.migrations.append(migration)

    # tip 将原先的 run 方法改成 migrate 方法，来执行所有的 migration
    def migrate(self):
        for m in self.migrations:
            try:
                m.execute()
            except Exception as e:
                raise e


if __name__ == '__main__':
    m = Migrate('./test_migrate')
    dashboard_migration = DashboardMigration('dashboard')
    rule_migration = RuleMigration('rule')
    m.register_migration(dashboard_migration)
    m.register_migration(rule_migration)
    m.migrate()
