# https://so1n.me/2019/04/15/%E7%BB%99python%E6%8E%A5%E5%8F%A3%E5%8A%A0%E4%B8%8A%E4%B8%80%E5%B1%82%E7%B1%BB%E5%9E%8B%E6%A3%80/
# 给 python 实现的 web 框架添加参数类型校验
import ast
from functools import wraps
from typing import Callable, Type


import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


class Model:
    """创建一个Model类, 类属性是{参数}={参数类型}"""
    def __init__(self):
        """这里把类属性的值设置到__dict__"""
        for key in self.__dir__():
            # 屏蔽自带方法,或其他私有方法
            if key.startswith('_'):
                continue
            value = getattr(self, key, None)
            # 值不是python type的也是错的
            if not isinstance(value, type):
                continue
            self.__dict__[key] = value

    def to_dict(self):
        """把{参数}={类型}转为dict"""
        return self.__dict__


class CustomModel(Model):
    # 这个是实际使用的Model, 看得出需要的uid参数类型是int
    uid = int
    timestamp = int
    user_info = dict
    user_name = str


def params_verify(model: Type[Model]):
    """装饰器"""
    def wrapper(func: Callable):
        @wraps(func)
        async def request_param(request: Request, *args, **kwargs):
            # 获取参数, 这里只做简单演示, 只获取url和json请求的数据
            param_dict: dict = dict(request.query_params)
            if request.method == "POST":
                param_dict.update(await request.json())
            instance_model: Model = model()
            try:
                # 通过model了解到了需要获取什么参数, 参数的类型是什么
                for key, key_type in instance_model.to_dict().items():
                    if key in param_dict:
                        # 通过ast进行安全的类型转换
                        # ast.literal_eval 类似于 eval 的功能：解析并执行一个包含 Python 文字字面值的抽象语法树（AST
                        value = ast.literal_eval(param_dict[key])
                        param_dict[key] = key_type(value)
                # 把转化好的参数放到'param_dict'
                request.state.param_dict = param_dict
                # 处理响应
                return await func(request, *args, **kwargs)
            except Exception as e:
                # 这里为了示范,把错误抛出来
                return JSONResponse({'error': str(e)})
        return request_param
    return wrapper


@params_verify(CustomModel)
async def demo_post(request):
    return JSONResponse({'result': request.state.param_dict})


@params_verify(CustomModel)
async def demo_get(request):
    return JSONResponse({'result': request.state.param_dict})


app = Starlette(
    routes=[
        Route('/api', demo_post, methods=['POST']),
        Route('/api', demo_get, methods=['GET']),
    ]
)


if __name__ == "__main__":
    uvicorn.run(app)