import hmac
import hashlib
import json


def signature(access_key_secret: str, method: str, uri: str, body: str) -> str:
    """
    参数同 golang 示例
    """
    hash_func = hashlib.sha256  # 默认使用 sha256 作为 hash 函数
    key = access_key_secret.encode('utf-8')
    msg = (method + uri + body).encode('utf-8')
    return hmac.new(key, msg, hash_func).hexdigest()


if __name__ == '__main__':
    test = ""
    body = ""
    zz = [{"a": 'b'}]
    for z in zz:
        print(z["a"])
    # print(signature('WXpCbE5Ua3pObUV5TmpReU5HRTFabUZqTUdZNFpUQmxObUUzWVRrMk1HTQ==', 'POST', 'api/v1/cloudenv/account',
    #                 str(test)))
    print(signature('pD56HNV9B3DF8DsYqIHGbg4OFjKTS9xTjHhNwYgnxvAOajMuHGqBjMwWaTMeJe6D', 'POST',
                    '/api/v1/compute/vm/create_instances',
                    json.dumps(test, indent=4)))
