"""
日志打印装饰器
"""
import logging
from functools import wraps

logger = logging.getLogger("apps")


class Logger:
    def __init__(self, level, module):
        self.level = level
        self.module = module

    def __call__(self, func):
        # tip: wraps本身也是一个装饰器，它能把原函数的元信息拷贝到装饰器里面的 func 函数中
        #  这使得装饰器里面的 func 函数也有和原函数 foo 一样的元信息了
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.level == 'warn':
                logger.warning(f'{self.module}-{func.__name__} is running')
            elif self.level == 'critical':
                logger.critical(f'{self.module}-{func.__name__} is running')
            elif self.level == 'error':
                logger.error(f'{self.module}-{func.__name__} is running')
            else:
                logger.info(f'{self.module}-{func.__name__} is running')
            res = func(*args, **kwargs)
            print(f'end of the {func.__name__}')
            return res

        return wrapper


# @logger(level='info') 等价于 @decorator
# tip: 装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
#  使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。
@Logger(level='info', module="foo")
def foo():
    print("===>foo")
