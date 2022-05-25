# python 加解密
import base64
import secrets
import string
from typing import Optional, Union

from cryptography.fernet import Fernet

RANDOM_STRING_CHARS = string.ascii_letters + string.digits + '@#$%^&*()_+-='

# python 生成随机字符串的函数
def get_random_string(length=50, allowed_chars=RANDOM_STRING_CHARS):
    """
    生成随机字符串
    """
    return ''.join(secrets.choice(allowed_chars) for _ in range(length))


class Crypto:
    """
    加密解密

    >>> c = Crypto()
    >>> message = 'hello world!'
    >>> encrypted = c.encrypt(message)
    >>> c.decrypt(encrypted)
    >>> 'hello world!'
    """

    # 设置一个 default "Fernet key must be 32 url-safe base64-encoded bytes."
    default_key = ''

    def __init__(self, key=None):
        # 创建实例时将 _key _handler 绑定到实例上
        self._key = self.generate_key(key)
        self._handler = Fernet(self._key)

    def generate_key(self, key: Optional[str] = None) -> bytes:
        if not key:
            return self.default_key

        placeholder = '0'
        data = ''.join([key, placeholder * 32])[:32]
        return base64.urlsafe_b64encode(data.encode('utf8'))

    def encrypt(self, data: Union[str, bytes], return_bytes=False) -> Union[str, bytes]:
        print('====str:', isinstance(data, str))
        data = data.encode('utf8') if isinstance(data, str) else data
        encrypted = self._handler.encrypt(data)
        return encrypted if return_bytes else encrypted.decode('utf8')

    def decrypt(self, data: Union[str, bytes], return_bytes=False) -> Union[str, bytes]:
        data = data.encode('utf8') if isinstance(data, str) else data
        decrypted = self._handler.decrypt(data)
        return decrypted if return_bytes else decrypted.decode('utf8')


if __name__ == '__main__':
    c = Crypto()
    # message = 'hello world!'
    # encrypted = c.encrypt(message)
    # print('====加密后：', encrypted)
    # decrypted = c.decrypt(encrypted)
    # print('====解密后：', decrypted)
    random_str = get_random_string()
    print('=======>', random_str)

